import urllib.request
import urllib.parse
import json

content = input('请输入需要翻译的内容：')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}
data['i']=content
data['from']= 'AUTO'
data['to']='AUTO'
data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']='15613905916475'
data['sign']='3126e352d5fecbc8137ac3ae51f589b8'
data['ts']='1561390591647'
data['bv']='3a019e7d0dda4bcd253903675f2209a5'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_CLICKBUTTION'

data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')

target = json.loads(html)
print("翻译结果： %s"%(target['translateResult'][0][0]['tgt']))