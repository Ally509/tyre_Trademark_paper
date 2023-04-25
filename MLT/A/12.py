from find_file import find

list = find('./train')
Note = open('x.txt', mode='w+')
for i in list:
    Note.writelines(i.split('\\')[1].split('.')[0]+'\n')
Note.close()