import requests    # 导入网络请求模块requests

# 发送网络请求
response = requests.get('https://www.baidu.com')
print('响应状态码为：',response.status_code)  # 打印状态码
print('请求的网络地址为：',response.url)          # 打印请求url
print('头部信息为：',response.headers)      # 打印头部信息
print('cookie信息为：',response.cookies)      # 打印cookie信息
