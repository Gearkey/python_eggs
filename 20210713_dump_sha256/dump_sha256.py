import os
import hashlib

def main():
    path = input('需要生成校验文件的目录：')
    with os.scandir(path) as files:
        for file in files:
            with open(os.path.join(path, file.name)+'.sum', 'w') as f:
                f.write(file.name + '\n')
                f.write(get_sha256(os.path.join(path, file.name)))

def get_sha256(path):
    with open(path, 'rb') as f:
        sha256_obj = hashlib.sha256()
        sha256_obj.update(f.read())
        return sha256_obj.hexdigest()

if __name__ == '__main__':
    main()