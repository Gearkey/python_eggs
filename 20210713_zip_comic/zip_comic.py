import os
import zipfile

def main():
    path = input('漫画根目录：')
    with os.scandir(path) as dirs:
        for dir in dirs:
            print('正在进行：' + dir.name + '...')
            dir2zip(os.path.join(path, dir.name))
    print('已完成')

def dir2zip(path):
    f = zipfile.ZipFile(path+'.zip', 'w' ,zipfile.ZIP_STORED)
    with os.scandir(path) as pics:
        for pic in pics:
            f.write(os.path.join(path, pic.name), pic.name)
    f.close()

if __name__ == '__main__':
    main()