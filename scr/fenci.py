import jieba
def fre(words,stop_words_path='中文stopwords.txt'):
    stop_words = set()
    with open(stop_words_path, 'r', encoding='utf-8') as f:
        for line in f:
                stop_words.add(line.strip())   #生成stop_word列表
    lst = jieba.lcut(words)    #分词
    lst2=[]
    for i in lst:
        if i not in stop_words:   #去除停用词
            lst2.append(i)
    sets = set(lst2)
    d = {}
    for i in sets:
        if len(i) > 1:  # 词长度大于2就统计
            d[i] = 0
    for i in lst:
        if i in d:
            d[i] += 1
    lst2 = []
    for i in d:
        lst2.append([i, d[i]])
    lst2.sort(key=lambda x: x[1], reverse=True)  #词频排序
    return lst2