import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
import numpy as np
import os

# Set the path to your dataset
train_path = './train'
test_path='./test'
# Parameters
image_height = 64
image_width = 64
num_channels = 3
num_classes = 10
batch_size = 32
num_epochs = 30

# 1. Prepare your dataset
# Assuming your dataset is organized with separate folders for each class
class_names = sorted(os.listdir(train_path))
num_train_samples = sum(len(files) for _, _, files in os.walk(train_path))

# 2. Data preprocessing
train_data = np.zeros((num_train_samples, image_height * image_width * num_channels), dtype=np.float32)
train_labels = np.zeros(num_train_samples, dtype=np.int32)

idx = 0
for class_index, class_name in enumerate(class_names):
    class_path = os.path.join(train_path, class_name)
    for image_name in os.listdir(class_path):
        image_path = os.path.join(class_path, image_name)
        image = tf.keras.preprocessing.image.load_img(image_path, target_size=(image_height, image_width))
        image_array = tf.keras.preprocessing.image.img_to_array(image)
        train_data[idx] = image_array.flatten()
        train_labels[idx] = class_index
        idx += 1

# Normalize the pixel values to the range of [0, 1]
train_data /= 255.0


class_names = sorted(os.listdir(test_path))
num_test_samples = sum(len(files) for _, _, files in os.walk(test_path))

# 2. Data preprocessing
test_data = np.zeros((num_test_samples, image_height * image_width * num_channels), dtype=np.float32)
test_labels = np.zeros(num_test_samples, dtype=np.int32)

idx = 0
for class_index, class_name in enumerate(class_names):
    class_path = os.path.join(test_path, class_name)
    for image_name in os.listdir(class_path):
        image_path = os.path.join(class_path, image_name)
        image = tf.keras.preprocessing.image.load_img(image_path, target_size=(image_height, image_width))
        image_array = tf.keras.preprocessing.image.img_to_array(image)
        test_data[idx] = image_array.flatten()
        test_labels[idx] = class_index
        idx += 1

# Normalize the pixel values to the range of [0, 1]
train_data /= 255.0
test_data /= 255.0

# 3. Split the dataset

# 4. Build the model - MLP
model = keras.Sequential([
    keras.layers.Dense(256, activation='relu', input_shape=(image_height * image_width * num_channels,)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(64,activation='relu'),
    keras.layers.Dense(32,activation='relu'),
    keras.layers.Dense(num_classes, activation='softmax')
])

# 5. Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 6. Train the model
model.fit(train_data, train_labels, epochs=num_epochs, batch_size=batch_size)

# 7. Evaluate the model
test_loss, test_accuracy = model.evaluate(test_data, test_labels)
print("Test Loss:", test_loss)
print("Test Accuracy:", test_accuracy)

# 8. Make predictions
predictions = model.predict(test_data)