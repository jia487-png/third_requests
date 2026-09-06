import requests    # 导入网络请求模块requests

# 发送网络请求
response = requests.get('https://www.baidu.com/img/bd_logo1.png?where=super')
print(response.content)                # 打印二进制数据
with open('bdlogo.png','wb')as f:   # 通过open函数将二进制数据写入本地文件
    f.write(response.content)          # 写入


