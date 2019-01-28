################################## 字符串类型 #################################
# 单引号、双引号、三引号
print('hello world')
print("hello world")
print('''hello world''')
print("""hello world""")

# 类型是str
print(type('hello world'))

# 单引号、双引号为了嵌套方便
print("Let's go!")
print('I like "python".')

# 转义字符\'，'"
print('Let\'s go!')
print("I like \"python\".")

# 其他转义字符
print('line1\nline2')   # 换行
# \r 回车
print('table\ttable')   # 制表符
print('C:\\Windows\\System32')  # \转义字符
print(r'C:\Windows\System32')      # r表示原始字符串，不是普通字符串，大写R也可以

# 三引号支持多行，每行长度不超过80个字符
print('Are you going to Scarborough Fair\nParsley, sage, rosemary and thyme\nRemember me to one who lives there\nShe once was a true love of mine')

print('''
Are you going to Scarborough Fair
Parsley, sage, rosemary and thyme
Remember me to one who lives there
She once was a true love of mine
''')

# 多行字符串拼接
print('Hello \
world')


############################ 字符串运算 #################################3
# 字符串拼接
print('Hello ' + 'World')
print('Hello ' * 3)
# 'Hello' * 'World' error

# 取字符
print('Hello World'[0])
print('Hello World'[-1])
# 取子字符串
print('Hello World'[0:4])
print('Hello World'[0:5])
print('Hello World'[6:])