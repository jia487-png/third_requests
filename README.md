# third_requests
第三方库REQUESTS
#  requests_GET.PY
~~~~~
import requests    # 导入网络请求模块requests

# 发送网络请求
response = requests.get('https://www.baidu.com')
print('响应状态码为：',response.status_code)  # 打印状态码
print('请求的网络地址为：',response.url)          # 打印请求url
print('头部信息为：',response.headers)      # 打印头部信息
print('cookie信息为：',response.cookies)      # 打印cookie信息
~~~~~

# 输出结果    
响应状态码为： 200
请求的网络地址为： https://www.baidu.com/
头部信息为： {'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Content-Encoding': 'br', 'Content-Type': 'text/html', 'Date': 'Sun, 06 Sep 2026 11:13:36 GMT', 'Pragma': 'no-cache', 'Server': 'BWS/1.1', 'Set-Cookie': 'BIDUPSID=25FB7C053F73ACB5C4893C5D7E809EBA; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com, PSTM=1788693216; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com, BAIDUID=25FB7C053F73ACB5C4893C5D7E809EBA:FG=1; Path=/; Domain=baidu.com; Max-Age=31536000, BAIDUID_BFESS=25FB7C053F73ACB5C4893C5D7E809EBA:FG=1; Path=/; Domain=baidu.com; Max-Age=31536000; Secure; SameSite=None', 'Tr_id': 'pr_0x983db3e403267e0b', 'Traceid': '178869321614219484265679309773288938567', 'Vary': 'Accept-Encoding', 'X-Ua-Compatible': 'IE=Edge,chrome=1', 'X-Xss-Protection': '1;mode=block', 'Transfer-Encoding': 'chunked'}
cookie信息为： <RequestsCookieJar[<Cookie BIDUPSID=25FB7C053F73ACB5C4893C5D7E809EBA for .baidu.com/>, <Cookie PSTM=1788693216 for .baidu.com/>, <Cookie BAIDUID=25FB7C053F73ACB5C4893C5D7E809EBA:FG=1 for .baidu.com/>, <Cookie BAIDUID_BFESS=25FB7C053F73ACB5C4893C5D7E809EBA:FG=1 for .baidu.com/>]>   

#  requests_POST.PY
~~~~~
import requests    # 导入网络请求模块requests
import json        # 导入json模块

# 字典类型的表单参数
data = {'1': '能力是有限的，而努力是无限的。',
        '2':'星光不问赶路人，时光不负有心人。'}
# 发送网络请求
response = requests.post('http://httpbin.org/post',data=data)
response_dict = json.loads(response.text)      # 将响应数据转换为字典类型
print(response_dict)                             # 打印转换后的响应数据
~~~~~
# 输出结果   
{'args': {}, 'data': '', 'files': {}, 'form': {'1': '能力是有限的，而努力是无限的。', '2': '星光不问赶路人，时光不负有心人。'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Content-Length': '284', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.5', 'X-Amzn-Trace-Id': 'Root=1-6a9d4d4f-13cde91b2cb1ec390a2eb1ab'}, 'json': None, 'origin': '111.60.88.224', 'url': 'http://httpbin.org/post'}   

#  requests_session.py 创建会话   
~~~~
import requests        # 导入requests模块
s = requests.Session()  # 创建会话对象
data={'username': 'mrsoft', 'password': 'mrsoft'}  # 创建用户名、密码的表单数据
# 发送登录请求
response =s.post('http://site2.rjkflm.com:666/index/index/chklogin.html',data=data)
response2=s.get('http://site2.rjkflm.com:666')   # 发送登录后页面请求
print('登录信息：',response.text)                # 打印登录信息
print('登录后页面信息如下:\n',response2.text)    # 打印登录后的页面信息
~~~~
