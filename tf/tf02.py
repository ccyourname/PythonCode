#coding=utf-8
#__author__ ="Charles.Xie"
import tensorflow as tf
#构建图
#创建个3*3矩阵  数据后面的点代表这个数据是浮点型，如果不加则数据是整形
matrix1=tf.constant([[1.,2.,3.],[4.,5.,6.]])
#创建个2*3矩阵
matrix2=tf.constant([[1.,4.],[2.,5.],[3.,6.]])
#矩阵乘法 product返回值是一个tensor
product = tf.matmul(matrix1,matrix2)
# print(product)
#在一个会话中启动图
# sess=tf.Session()
# resulte=sess.run(product)
# sess.close()#释放sess资源
# print(resulte)
# 调用 sess 的 'run()' 方法来执行矩阵乘法 op, 传入 'product' 作为该方法的参数.
# 上面提到, 'product' 代表了矩阵乘法 op 的输出, 传入它是向方法表明, 我们希望取回
# 矩阵乘法 op 的输出.
# 整个执行过程是自动化的, 会话负责传递 op 所需的全部输入. op 通常是并发执行的.
# 函数调用 'run(product)' 触发了图中三个 op (两个常量 op 和一个矩阵乘法 op) 的执行.
# 返回值 'result' 是一个 numpy `ndarray` 对象.
#更优质的实现方式·
with tf.Session() as sess:
    resulte=sess.run(product)
    print(resulte)
# #可以使用 InteractiveSession 代替 Session 类, 使用 Tensor.eval() 和 Operation.run() 方法代替 Session.run()
# sess = tf.InteractiveSession()
# x=tf.Variable([[1.],[2.]])
# a=tf.constant([[3.,6.]])
# # 使用初始化器 initializer op 的 run() 方法初始化 'x'
# x.initializer.run()
# m=tf.matmul(x,a)
# print(m.eval())