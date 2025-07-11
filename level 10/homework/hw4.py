a = "5"
b = int(a)       # str → int
print(b + 2)     # 7

x = 10.6
y = int(x)       # float → int
print(y)         # 10

age = 25
text = "Your age is " + str(age)   # int → str
print(text)

flag = "True"
converted = bool(flag)     # str → bool
print(converted)           # True

num_list = "123"
print(list(num_list))      # str → list → ['1', '2', '3']
