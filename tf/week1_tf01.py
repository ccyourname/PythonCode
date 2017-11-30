#coding=utf-8
#__author__ ="Charles.Xie" 
import tensorflow as tf
# 使⽤用tf计算下⾯面算式的值：
# x=2 ,y=3,z=7 求解：res=x*y+z的结果
x=tf.constant(2)
y=tf.constant(3)
z=tf.constant(7)
# tf.mul, tf.sub and tf.neg are deprecated in favor of tf.multiply, tf.subtract and tf.negative.
res=  tf.add( tf.multiply(x,y),z)
with tf.Session() as sess:
    print(sess.run(res))