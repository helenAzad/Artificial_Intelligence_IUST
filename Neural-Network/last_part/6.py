import numpy as np
import os
from PIL import Image
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt

# path of train and test data
train_path = './train'
test_path = './test'

# create list of dataset
X_train = []
X_test = []

# add image array to X_train
for folder in os.listdir(train_path):
    for file in os.listdir(os.path.join(train_path, folder)):
        image = Image.open(os.path.join(train_path,folder, file))
        image_array = np.array(image)
        image_array = image_array.reshape(256)
        X_train.append(image_array)

# add image array to X_test
for folder in os.listdir(test_path):
    for file in os.listdir(os.path.join(test_path, folder)):
        image = Image.open(os.path.join(test_path,folder, file))
        image_array = np.array(image)
        image_array = image_array.reshape(256)
        X_test.append(image_array)

# Convert list of dataset to numpy array
X_train = np.array(X_train)
X_test = np.array(X_test)

# add noise to dataset
noise_train = np.random.normal(scale=30, size=X_train.shape)
y_train = X_train
X_train = X_train + noise_train

noise_test = np.random.normal(scale=30, size=X_test.shape)
y_test = X_test
X_test = X_test + noise_test

# create MLP
mlp = MLPRegressor(hidden_layer_sizes=(20, 20, 20, 20), max_iter=20000)

# train the model
mlp.fit(X_train, y_train)

# test the model
y_pred = mlp.predict(X_test)
pred_list = [arr.reshape(256) for arr in y_pred]

# show the resault
for i in range (10):
    # reshape the vector into a 16*16 array
    train_arr = y_test[i].reshape((16, 16))
    plt.imshow(train_arr, cmap='gray')
    plt.show()

    test_arr = X_test[i].reshape((16, 16))
    plt.imshow(test_arr, cmap='gray')
    plt.show()

    pred_arr = pred_list[i].reshape((16, 16))
    plt.imshow(pred_arr, cmap='gray')
    plt.show()

    print("*************************************************")