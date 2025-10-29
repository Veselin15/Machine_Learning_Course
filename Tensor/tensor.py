import tensorflow as tf

tensor1 = tf.ones([1,2,3])
tensor2 = tf.reshape(tensor1,[1,1,6])
print(tf.rank(tensor1))
print(tensor1)
print(tensor2)
