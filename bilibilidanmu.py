import requests
import re


#爬b站弹幕的话。首先需要抓包，在浏览器中检查元素找到一个.xml的响应信息，因为弹幕是以xml文件动态加载到页面的，把鼠标放上面应该可以看到xml的链接接下就可以爬了。 在开始的时候我在能不能直接在它本页面找到弹幕地址，不去抓他的xml地址，没办到。有大神的话麻烦指点一下。

# url='https://www.bilibili.com/bangumi/play/ep115929/'    #弹幕所属视频链接
url = 'https://comment.bilibili.com/38148051.xml'    #xml的地址，只需改动数字部分就可改变不同视频弹幕文件

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'referer': 'https://www.bilibili.com/bangumi/play/ep115929/',
    'origin': 'https://www.bilibili.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9'
}

response = requests.get(url,headers)    #获取的响应对象
# print(response)
html = response.text   #获取的是页面以字符串形式
# print(html)
pattern = re.compile('<d p=".*?">(.*?)</d>',re.S)   #正则匹配
data = re.findall(pattern, html)
pinlun_data = str(data).replace(',','\n')    #拆分一下数据，清晰一点
# print(data)
filename = url.split('/')[-1].split('.')[0]+'.txt'
# print(filename)
with open(filename,'w',encoding='utf-8') as f:     #写入数据
    f.write(pinlun_data)
