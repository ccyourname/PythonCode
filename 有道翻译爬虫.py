import urllib.request
import json
import urllib.parse
while 1:
    i = input("请输入要翻译的文字：")
    if i=='!q':
        print("退出")
        break
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom="
    data ={}
#方案一
#head={}
#head["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
#方案二
    head="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
# From Data 全部属性
    data["i"]=i
    data["from"]="AUTO"
    data["to"]="AUTO"
    data["smartresult"]="dict"
    data["client"]="fanyideskweb"
    data["salt"]="502865709143"
    data["sign"]="e7b725d55dd02ab7b3a17c44170950ad"
    data["doctype"]="json"
    data["version"]="2.1"
    data["keyfrom"]="fanyi.web"    
    data["action"]="FY_BY_CLlCKBUTTON"
    data["typoResult"]="true"
#转码
    data =urllib.parse.urlencode(data).encode("utf-8")
#打开链接
#方案一
#req = urllib.request.Request(url,data,head)#Request设置
#方案二
    req = urllib.request.Request(url,data)
    req.add_header("User-Agent",head)
    response = urllib.request.urlopen(req)
#转为Unicode
    html=response.read().decode("utf-8") #输出为json格式
#json文件读取
    target = json.loads(html)
#最终字典列表输出
    print(target["translateResult"][0][0]["tgt"])
