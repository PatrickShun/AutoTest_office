import os

filePath = "C:\\AllProject\\AutoAsterixPython\\ChangeName\\TestFile\\"

baseNameList = []
changeNameList = []
num = 0

qian = input("请输入前缀：")
hou = input("请输入后缀：")


for i,j,k in os.walk(filePath):
    # print(i)
    # print(j)
    # print(k)
    baseNameList = k

print(baseNameList)

for n in range(1,len(baseNameList)+1):
    if str(n) in baseNameList[n-1]:
        num = "{:0>2d}".format(n)

        valueName = qian + str(num) + hou

        changeNameList.append(valueName)
    else:
        print("Null")

print(changeNameList)

# print("{:0>2d}".format(num))

# if len(baseNameList) == len(changeNameList):
#     for z,p in zip(baseNameList,changeNameList):
#         oldname = filePath + z
#         newname = filePath + p
#         os.rename(oldname,newname)
#         print(oldname,"-->",newname)
