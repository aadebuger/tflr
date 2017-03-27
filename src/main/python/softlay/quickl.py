'''
Created on 27 Mar 2017

@author: aadebuger
'''

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
sess.run(hello)
a = tf.constant(10)
b = tf.constant(32)
print( sess.run(a+b) )

def avg():
    a = tf.placeholder(tf.float32)
    b = tf.placeholder(tf.float32)
    adder_node =  (a + b)/2
    print(sess.run(adder_node, {a: 3, b:4.5}))


if __name__ == '__main__':
    avg()