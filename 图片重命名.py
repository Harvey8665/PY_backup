import os
path = './o' #源文件的路径
filelist = os.listdir(path) #该文件夹下所有的文件（包括文件夹）
a = 0
for file in filelist:
    print(file)
for file in filelist: #遍历所有文件
    Olddir=os.path.join(path,file) #原来的文件路径
    if os.path.isdir(Olddir): #如果是文件夹则跳过
        continue
    filename=os.path.splitext(file)[0] #分离文件名与扩展名;得到文件名
    filetype=os.path.splitext(file)[1] #文件扩展名
    Newdir=os.path.join(path,str(a)+str('.jpg')) #得到路径+后面需要跟的命名
    a += 1
    os.rename(Olddir,Newdir)#重命名
