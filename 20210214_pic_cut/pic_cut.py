import os
from PIL import Image

def main():
    # 开始
    print('\n-- Pic_cut v0.2b --\n')

    # 默认数值
    path = 'D:\\temp\\piccut\\pic\\'
    path_out = 'D:\\temp\\piccut\\pic_out\\'
    row_num = 1
    column_num = 2

    path = input('操作路径：')
    path_out = input('输出路径：')
    row_num = int(input('切割行数：'))
    column_num = int(input('切割列数：'))
    print('')

    with os.scandir(path) as pics:
        for pic in pics:
            pic_cut(path + pic.name, path_out + pic.name, row_num, column_num)
            print('已处理：' + pic.name)
    
    print("\n图片已生成至指定目录\n")
    return 0

def pic_cut(path, path_out, row_num, column_num):
    pic = Image.open(path)

    # 宽高处理
    width, height = pic.size
    w = width / column_num
    h = height / row_num

    # 路径拆分为文件夹路径、文件名和后缀
    p = os.path.split(path_out)
    pic_name = p[1].split('.')

    num = 1
    for i in range(row_num):
        for j in range(column_num):
            x = w * j
            y = h * i
            
            # 左上右下
            box = (x, y, x + w, y + h)
            pic.crop(box).save(p[0] + '\\' + pic_name[0] + '_' + str(num) + '.' + pic_name[-1])
            num += 1
    
    return 0

if __name__ == '__main__':
    main()