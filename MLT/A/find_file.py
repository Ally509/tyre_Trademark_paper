import os

#input： 待查找文件夹（path路径前边加一个r，防止将路径中的\识别为转义字符）， 指定后缀(没有写0)
#otput: 返回一个字符串列表
def find(path, la = ''):
    list = []
    num = 0
    for i in os.listdir(path):
        path2 = os.path.join(path, i)
        #print(len(la))
        #print(path2)
        #print(type(path2))
        if la == '':
            num = num + 1
            list.append(path2)
            print('文件{}路径已保存'.format(path2))
        else:
            if path2[len(path2)-len(la):] == la:
                num = num + 1
                list.append(path2)
                print('文件{}路径已保存'.format(path2))
    print('共检测到{}个{}文件，路径均已提取'.format(num, la))
    return list

if __name__ == '__main__':
    list = find(r'C:\Users\多发SCI\Desktop\qqq', 'txt')
