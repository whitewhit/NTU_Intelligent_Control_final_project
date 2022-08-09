import tensorflow as tf
import os
os.environ[ " CUDA_VISIBLE_DEVICES " ]= " 0 " 
tf.compat.v1.disable_eager_execution()
hello=tf.constant(' Hello,TensorFlow ' )
config= tf.compat.v1.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.9
sess=tf.compat.v1.Session(config= config)
print (sess.run(hello))