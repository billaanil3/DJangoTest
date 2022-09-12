# open() ---> Read, write, append-->(Mode)
# # r, w, a
# 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors',
# 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name',
# 'newlines', 'read', 'readable', 'readline', 'readlines', 'seek',
# 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines'
"""
data = open("files_ex.txt", "r")
# print(data.read())
# print(data.readlines())
lines = data.readlines()
for line in lines:
    if 'you' in line.split():
        print(line)
# print(data.readline())
# print(data.readline())
# print(data.tell())
# data.seek(45)
# print(data.tell())
"""

data = open("files_ex1.txt", "w")
# print(dir(data))
data.write("Anil\nBilla\nKumar")
# print(data.read())

# lists = ["Hii", "Hello", "How are you", "Bye"]
# data = open("files_ex3.txt", "a")
# for lst in lists:
#     data.write(lst)
#     data.seek(5)
#     data.write("\n")
