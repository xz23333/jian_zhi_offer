"""
面试题5：替换空格
题目：请实现一个函数，把字符串中的每个空格替换成"%20"。例如输入“We are happy.”，
则输出“We%20are%20happy.”。
"""

'''
# s 源字符串
def replaceSpace(s):
    s_len = len(s)
    count = 0
    # 遍历字符串，数出空格个数。
    if s_len == 0:
        return
    for i in range(s_len):
        if s[i] == ' ':
            count += 1
    print(count)
    #新建一个字符串，从后往前复制，遇到空格替换成%20
    newlen = s_len + count * 2
    newstring = [" "] *newlen
    while newlen >= 0:
        if s[s_len-1] != ' ':
            newstring[newlen-1] = s[s_len-1]
            newlen -= 1
        else:
            newstring[newlen-1] = '0'
            newstring[newlen-2] = '2'
            newstring[newlen-3] = '%'
            newlen -= 3
        s_len -= 1
    return ''.join(newstring)
'''

def replaceSpace(s):
    s = list(s)
    count=len(s)
    for i in range(count):
        if s[i] == ' ':
            s[i] = '%20'
    return ''.join(s)

print(replaceSpace("we are family"))




