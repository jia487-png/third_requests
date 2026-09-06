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
