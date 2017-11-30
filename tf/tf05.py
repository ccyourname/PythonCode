#coding=utf-8
#__author__ ="Charles.Xie"
import tensorflow as tf
# ......读取mnist数据-start
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./MNIST_Data", one_hot=True)
# ......读取mnist数据-end
x=tf.placeholder(tf.float32,[None,784])
# x不是一个特定的值，而是一个占位符placeholder，我们在TensorFlow运行计算时输入这个值。
# 我们希望能够输入任意数量的MNIST图像，每一张图展平成784维的向量。我们用2维的浮点数张量来表示这些图，
# 这个张量的形状是[None，784 ]。（这里的None表示此张量的第一个维度可以是任何长度的。）
w=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.zeros([10]))
# 注意，W的维度是[784，10]，因为我们想要用784维的图片向量乘以它以得到一个10维的证据值向量，
# 每一位对应不同数字类。b的形状是[10]，所以我们可以直接把它加到输出上面。

# 实现公式
y=tf.nn.softmax(tf.matmul(x,w)+b)
#占位符-用于输入正确值
y_=tf.placeholder('float',[None,10])
#计算交叉熵
cross_entory=-tf.reduce_sum(y_ * tf.log(y))
# 用梯度下降算法（gradient descent algorithm）以0.01的学习速率最小化交叉熵
train_step=tf.train.GradientDescentOptimizer(0.01).minimize(cross_entory)
#模型设计结束，运算之前先初始化设置的变量
init=tf.initialize_all_variables()
#启动图
with tf.Session() as sess:
    sess.run(init)#变量初始化
    for i in range(1000):
        batch_xs,batch_ys=mnist.train.next_batch(200)
        sess.run(train_step,feed_dict={x:batch_xs,y_:batch_ys})
        # 该循环的每个步骤中，我们都会随机抓取训练数据中的100个批处理数据点，
        # 然后我们用这些数据点作为参数替换之前的占位符来运行train_step。
        # 使用一小部分的随机数据来进行训练被称为随机训练（stochastic
        # training）- 在这里更确切的说是随机梯度下降训练。在理想情况下，
        # 我们希望用我们所有的数据来进行每一步的训练，因为这能给我们更好的训练结果，
        # 但显然这需要很大的计算开销。所以，每一次训练我们可以使用不同的数据子集，
        # 这样做既可以减少计算开销，又可以最大化地学习到数据集的总体特性。

    # 如何评估模型
    # 首先让我们找出那些预测正确的标签。tf.argmax 是一个非常有用的函数，
    # 它能给出某个tensor对象在某一维上的其数据最大值所在的索引值。
    # 由于标签向量是由0,1组成，因此最大值1所在的索引位置就是类别标签，
    # 比如tf.argmax(y,1)返回的是模型对于任一输入x预测到的标签值，
    # 而 tf.argmax(y_,1) 代表正确的标签，我们可以用 tf.equal
    # 来检测我们的预测是否真实标签匹配(索引位置一样表示匹配)。
    correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
    # 这行代码会给我们一组布尔值。为了确定正确预测项的比例，我们可以把布尔值转换成浮点数，
    # 然后取平均值。例如，[True, False, True, True] 会变成 [1,0,1,1] ，取平均值后得到 0.75.
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    # 最后，我们计算所学习到的模型在测试数据集上面的正确率。
    print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))