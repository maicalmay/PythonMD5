import hashlib

print("输入加密内容")
message = input()
md5 = hashlib.md5(message.encode())
print("%s md5 加密结果是： %s" % (message, md5.hexdigest()))
input("Press <enter>")