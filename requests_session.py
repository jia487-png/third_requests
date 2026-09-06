import requests        # 导入requests模块
s = requests.Session()  # 创建会话对象
data={'username': 'mrsoft', 'password': 'mrsoft'}  # 创建用户名、密码的表单数据
# 发送登录请求
response =s.post('http://site2.rjkflm.com:666/index/index/chklogin.html',data=data)
response2=s.get('http://site2.rjkflm.com:666')   # 发送登录后页面请求
print('登录信息：',response.text)                # 打印登录信息
print('登录后页面信息如下:\n',response2.text)    # 打印登录后的页面信息