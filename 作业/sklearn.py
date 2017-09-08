#coding=gbk
#__author__ ="л��" 
#lesson4 homework
from sklearn import svm,datasets

class DataSet:
    #DataSet�࣬������ص����ݼ�
    #�������x,y
    def __init__(self,name):
        #���������������ݼ�
        #һ���ǡ�iris����һ����digits��
        self.name=name
    def download_data(self):
        #��sklearn���Դ���������ָ�������ݼ�
        if self.name=='iris':
            self.downloaded_data=datasets.load_iris()
        elif self.name=='digits':
            self.downloaded_data=datasets.load_digits()
        else:
            print("Dataset Error: û�и�name�����ݼ�")
    def generate_xy(self):
        #�����ص����ݼ��ֽ�Ϊԭʼ���ݼ����ǵ�label
        self.download_data()#�������ݼ�
        x=self.downloaded_data.data #ԭʼ����
        y=self.downloaded_data.target#label
        print("ԭʼ���ݣ�%s"%x)
        print("x:",len(x),len(x[0]))
        print("Lable:%s"%y)
        print("y:",len(y))
        return x,y
    def get_train_test_set(self,ratio):
        #�����ݷ�Ϊѵ�����Ͳ��Լ�
        #����ratio ȷ���Զ��ٱ������ָ�ѵ�����Ͳ��Լ�
        x,y=self.generate_xy()#��ȡԭʼ���ݺ�label
        #��֪�õ��˶�������
        n_samples=len(x)
        #����tatio����֪����������ѵ�������������ǲ��Լ�
        n_train=n_samples*ratio
        #��ʼ�ָ�����
        x_train=x[:n_train]
        y_train=y[:n_train]
        x_test=x[n_train:]
        y_test=y[n_train:]
        return x_train,y_train,x_test,y_test
        #��DataSet��������

if  __name__=="__main__":
    data = DataSet('digits')#���������
    #��raito�����ָ����ݼ�
    x_train,y_train,x_test,y_test=data.get_train_test_set(0.7)
    clf=svm.SVC()
    print(clf.fit(x_train,y_train))
    test_point=x_test[12]
    y_true=y_test[12]
    print(clf.predict(test_point))
    print(y_true)