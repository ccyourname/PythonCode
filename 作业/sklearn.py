#coding=gbk
#__author__ ="谢飞" 
#lesson4 homework
from sklearn import svm,datasets

class DataSet:
    #DataSet类，下载相关的数据集
    #并分类好x,y
    def __init__(self,name):
        #告诉类用哪种数据集
        #一个是“iris”另一个“digits”
        self.name=name
    def download_data(self):
        #从sklearn的自带集中下载指定的数据集
        if self.name=='iris':
            self.downloaded_data=datasets.load_iris()
        elif self.name=='digits':
            self.downloaded_data=datasets.load_digits()
        else:
            print("Dataset Error: 没有该name的数据集")
    def generate_xy(self):
        #把下载的数据集分解为原始数据及他们的label
        self.download_data()#下载数据集
        x=self.downloaded_data.data #原始数据
        y=self.downloaded_data.target#label
        print("原始数据：%s"%x)
        print("x:",len(x),len(x[0]))
        print("Lable:%s"%y)
        print("y:",len(y))
        return x,y
    def get_train_test_set(self,ratio):
        #把数据分为训练集和测试集
        #参数ratio 确定以多少比例来分割训练集和测试集
        x,y=self.generate_xy()#获取原始数据和label
        #获知得到了多少数据
        n_samples=len(x)
        #根据tatio来得知多少数据是训练集多少数据是测试集
        n_train=n_samples*ratio
        #开始分割数据
        x_train=x[:n_train]
        y_train=y[:n_train]
        x_test=x[n_train:]
        y_test=y[n_train:]
        return x_train,y_train,x_test,y_test
        #类DataSet创建结束

if  __name__=="__main__":
    data = DataSet('digits')#穿件类对象
    #用raito比例分割数据集
    x_train,y_train,x_test,y_test=data.get_train_test_set(0.7)
    clf=svm.SVC()
    print(clf.fit(x_train,y_train))
    test_point=x_test[12]
    y_true=y_test[12]
    print(clf.predict(test_point))
    print(y_true)