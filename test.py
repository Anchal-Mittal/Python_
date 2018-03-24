import tensorflow as tf

with tf.device('/gpu:0'):
     x=tf.Variable(tf.random_uniform([100,100],-1,1),name="x")

init=tf.global_variables_initializer()
sess.run(init)

sess=tf.Session(config=tf.ConfigProto(log_device_placement=True,allow_soft_placement=True))

print(sess.run(x))
