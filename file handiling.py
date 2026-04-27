#0pen - read  write  append = close
'''
try:
    file = open('student.txt','r')
except filenotefoundError:
    print("file is not present")
else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()'''

with open('student.txt','w+') as file:
    file.write('rajesh')
    file.write('\nsujith')
    file.seek(0)
    print(file.read())


