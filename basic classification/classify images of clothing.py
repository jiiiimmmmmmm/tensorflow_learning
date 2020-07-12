# TensorFlow and tf.keras
import tensorflow as tf
from pandas import DataFrame
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print('First of all, let us explore the data.')
print('the shapes of train images', train_images.shape)
print('the lengths of train lables', len(train_labels))
temp = DataFrame(train_labels)
# question: I want to sort the unique data of train labels.
# What should I do?
print('train_labels.unique()', temp[0].unique())
print('the shapes of test images', test_images.shape)
print('the lengths of train labels', len(test_labels))
temp = DataFrame(test_labels)
print('test_labels.unique()', temp[0].unique())

print('Then, let us preprocess the data')
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

train_images = train_images / 255.0
test_images = test_images / 255.0

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()

print('OK! we can build the model now!')
# remember: the basic building block of a neural network is the layer
model = keras.Sequential([
    # flatten: transform the format of the images from 2D array to 1D array
    keras.layers.Flatten(input_shape=(28, 28)),
    # dense: 128 means there are 128 nodes in this layer
    keras.layers.Dense(128, activation='relu'),
    # dense: 10 nodes represent 10 classifying results respectively
    keras.layers.Dense(10)
])

# compile the model
# Loss function —This measures how accurate the model is during training.
# Optimizer —how to improve based on the data it sees and its loss function.
# Metrics —Used to monitor the training and testing steps.

# what's differences between loss function and metrics?
# why do they both relate to accuracy?
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)



# evaluate the accuracy
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('test loss:', test_loss)
print('Test accuracy:', test_acc)


probability_model = tf.keras.Sequential([model,
                                         tf.keras.layers.Softmax()])
predictions = probability_model.predict(test_images)
print(predictions[0])
print(np.argmax(predictions[0]))
print(test_labels[0])
def plot_image(i, predictions, true_label, img):
    predictions, true_label, img = predictions[i], true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                       100 * np.max(predictions),
                                       class_names[true_label]),
                                color=color)

def plot_value_array(i, preditions, true_label):
    preditions, true_label = preditions[i], true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), preditions, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(preditions)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')


def plot_muti_img_val(page = 0):
    """
    Plot the first X test images, their predicted labels, and the true labels.
    Color correct predictions in blue and incorrect predictions in red.
    :param page:
    :return:
    """
    num_rows = 5
    num_cols = 3
    num_images = num_rows*num_cols
    plt.figure(figsize=(2*2*num_cols, 2*num_rows))
    for i in range(num_images):
      plt.subplot(num_rows, 2*num_cols, 2*i+1)
      plot_image(i+page*num_images, predictions, test_labels, test_images)
      plt.subplot(num_rows, 2*num_cols, 2*i+2)
      plot_value_array(i+page*num_images, predictions, test_labels)
    plt.tight_layout()
    plt.show()


for i in range(len(test_labels)//15):
    plot_muti_img_val(i)