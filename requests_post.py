import requests    # 导入网络请求模块requests
import json        # 导入json模块

# 字典类型的表单参数
data = {'1': '能力是有限的，而努力是无限的。',
        '2':'星光不问赶路人，时光不负有心人。'}
# 发送网络请求
response = requests.post('http://httpbin.org/post',data=data)
response_dict = json.loads(response.text)      # 将响应数据转换为字典类型
print(response_dict)                             # 打印转换后的响应数据


