import os
from datetime import datetime

def main():
    print("--- Soft_renamer_v0.1 ---\n")
    work_path = os.path.normpath(input("工作目录："))

    for soft_source in os.scandir(work_path):
        for file in os.scandir(os.path.abspath(soft_source)):
            modified_time = datetime.strftime(datetime.fromtimestamp(os.path.getmtime(file)), "%Y%m%d")
            
            old_name = os.path.abspath(file)
            new_name = os.path.splitext(old_name)[0] + "_" + soft_source.name + "_" + modified_time + os.path.splitext(old_name)[1]
            os.renames(old_name, new_name)

            print("已处理：" + new_name)
    
    print("\n处理完毕")

if __name__ == "__main__":
    main()