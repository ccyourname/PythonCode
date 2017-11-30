#coding=utf-8
#__author__ ="Charles.Xie" 
import tensorflow as tf
# 创建一个变量, 初始化为标量 0.
state=tf.Variable(0,name='count')
# 创建一个 op, 其作用是使 state 增加 1
x=tf.constant(1)
update_state=tf.add(state,x)
#assign是表达式的一部分，在run之前并不会真正的执行赋值
update=tf.assign(state,update_state)
# 启动图后, 变量必须先经过`初始化` (init) op 初始化,
# 首先必须增加一个`初始化` op 到图中.
state_op=tf.initialize_all_variables()
# 启动图，运行op
# with tf.Session() as sess:
#     sess.run(state_op)
#     print('初始化:',sess.run(state))
#     for i in range(5):
#         sess.run(update)
#         print('结果:',sess.run(state))
with tf.Session() as sess:
    sess.run(state_op)
    print('初始化:',sess.run(state))
    for i in range(1):
        state +=x
        print('结果:',sess.run(state))
#tf算法
input1=tf.constant(1.0)
input2=tf.constant(2.0)
input3=tf.constant(3.0)
flag=tf.add(input1,input2)
# tf.mul, tf.sub and tf.neg are deprecated in favor of tf.multiply, tf.subtract and tf.negative.
result=tf.multiply(flag,input3)
se=tf.Session()
print(se.run([result,flag]))
z=(input1+input2)*input3
print(se.run(z))

