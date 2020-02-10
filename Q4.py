'''
面试题4：二维数组中的查找
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按
照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个
整数，判断数组中是否含有该整数。
'''
array = [
    [1, 2, 4, 6, 8],
    [4, 4, 6, 7, 9],
    [5, 7, 8, 9, 11]
]


def findX(x, array):
    i = 0
    j = len(array[0]) - 1
    while j >= 0 and i < len(array) :
        if x < array[i][j]:
            j -= 1
        elif x == array[i][j]:
            return True
        else:
            i += 1
    return False


x = 0
while True:
    x = input("请输入：")
    if x.isdigit():
        a = int(x)
        print(findX(a, array))
        continue
    elif x == '-1':
        break
    else:
        print("输入错误，只能输入整数")
