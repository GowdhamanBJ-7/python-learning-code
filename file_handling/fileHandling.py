#w - write a content
with open("data.txt", "w") as f:
    f.write("Hello, Python!\n")
    f.write("File handling is easy.")

#read the file
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

f = open("C:\\Users\\GowdhamanBJ\\learning\\python\\data_structure\\tuple.py")
print(f.read())

with open("data.txt") as f:
  print(f.readline())           #return only first line

# import os
# if os.path.exists("data.txt"):
#   os.remove("data.txt")
# else:
#   print("The file does not exist")
