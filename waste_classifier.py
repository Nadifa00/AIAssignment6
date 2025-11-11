import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os

#SETUP DIRECTORIES
train_dir = "DATASET/TRAIN"
test_dir = "DATASET/TEST"

#DATA PREPROCESSING
img_size = (128, 128)
batch_size = 16

train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_data = train_datagen.flow_from_directory(
    train_dir,
    target_size=img_size,
    batch_size=32,
    class_mode='binary'
)

test_data = test_datagen.flow_from_directory(
    test_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='binary',
    shuffle=False
)

#BUILD LIGHTWEIGHT MODEL
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # binary classification
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#TRAIN MODEL
history = model.fit(train_data, validation_data=test_data, epochs=5)

#EVALUATE MODEL
loss, acc = model.evaluate(test_data)
print(f"Test Accuracy: {acc * 100:.2f}%")

#CONVERT TO TENSORFLOW LITE
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save model
os.makedirs("tflite_model", exist_ok=True)
with open("tflite_model/recycle_model.tflite", "wb") as f:
    f.write(tflite_model)

print("TensorFlow Lite model saved as 'tflite_model/recycle_model.tflite'")


#TEST WITH TFLITE INTERPRETER
interpreter = tf.lite.Interpreter(model_path="tflite_model/recycle_model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Get a few sample test images
x_test, y_test = next(iter(test_data))
sample_input = np.expand_dims(x_test[0], axis=0).astype(np.float32)

interpreter.set_tensor(input_details[0]['index'], sample_input)
interpreter.invoke()
output_data = interpreter.get_tensor(output_details[0]['index'])
prediction = (output_data[0][0] > 0.5).astype(int)

print(f"TFLite sample prediction: {prediction}, True label: {int(y_test[0])}")
