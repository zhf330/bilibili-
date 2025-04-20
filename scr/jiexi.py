from re import findall   #解析提取弹幕
def anly(path):
    with open('../data/sample.xml', 'r', encoding='utf-8') as f: #打开xml文件
        words_lst=findall('p=".*?">(.*?)</d><d',f.read())     #正则表达式找出所有弹幕
        words=''.join(words_lst)  #换成字符串形式
        return words