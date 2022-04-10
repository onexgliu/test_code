import re  # 导入正则表达式re模块

pattern = r'[?|&]'  # 定义分割符
url = 'http://www.mingrisoft.com/login.jsp?username="mr"&pwd="mrsoft"'
result = re.split(pattern, url)  # 分割字符串
print(result)
