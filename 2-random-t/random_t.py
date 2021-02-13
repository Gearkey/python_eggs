import random

def main():
    # 开始
    print('\n-- 随机温度生成器 v0.2 --\n')

    # 数值设定
    lower = 35.9
    upper = 36.4
    number = 20

    # 重写数值
    # lower = float(input('下限：'))
    # upper = float(input('上限：'))
    number = int(input('数量：'))
    print('')

    # 输出列表
    print('序号', end='\t')
    print('上午', end='\t')
    print('下午')

    for i in range(number):
        print(i+1, end='\t')
        print(get_temperature(lower, upper), end='\t')
        print(get_temperature(lower, upper))

def get_temperature(lower, upper):
    return round(random.uniform(lower, upper),1)

if __name__ == "__main__":
    main()