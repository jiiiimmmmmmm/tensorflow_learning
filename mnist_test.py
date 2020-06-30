import tensorflow.compat.v1 as tf

import input_data



tf.compat.v1.disable_eager_execution()

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

x = tf.placeholder("float",[None,784])
w = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x,w)+b)
