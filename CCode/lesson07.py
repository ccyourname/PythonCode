import urllib.request
import re

# 打开网址（1）
def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    return html

# 获取图片网址(2)
def get_img(html):
    p = r' src="([^"]+\.jpg-550)"' #正则表达式
    imglist = re.findall(p,html)
    filename=1
    for each in imglist:
        print(each)
        try:
            urllib.request.urlretrieve(each,str(filename)+'.jpg',None)#保存链接
            #urllib.request.urlretrieve(each,filename,None)
        except:
            print("保存失败")
        filename+=1

# 调用函数（3）
if __name__ == '__main__':
    #网页地址
    url = "http://baozoumanhua.com/all/hot?page=2&sv=1510192202"
    get_img(open_url(url))
