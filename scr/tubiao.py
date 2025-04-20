import matplotlib.pyplot as plt
from wordcloud import WordCloud
def mk_pie(lst2):
    lst3=lst2[:10] #取频率前十的词
    plt.rcParams['font.sans-serif'] = ['SimHei']  #防止中文乱码
    plt.figure(figsize=(10, 6))
    l=[item[0] for item in lst3]
    s=[item[1] for item in lst3]
    plt.pie(s, labels=l, autopct='%1.1f%%')  #生成饼图
    plt.axis('equal')
    plt.title('b站 top10弹幕统计图')  #标题
    #存到output文件
    dir= '../output'
    file_name='弹幕饼图'
    file_path=f'{dir}/{file_name}'
    plt.savefig(file_path)
def mk_bar(lst2):
    lst3 = lst2[:10]  # 取频率前十的词
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 防止中文乱码
    plt.figure(figsize=(10, 6))
    l = [item[0] for item in lst3]
    s = [item[1] for item in lst3]
    plt.bar(l,s)  #生成柱状图
    #标题，标签
    plt.title('b站 top10弹幕柱状图')
    plt.xlabel('高频词')
    plt.ylabel('次数')
    #存到output文件
    dir= '../output'
    file_name='弹幕柱状图'
    file_path=f'{dir}/{file_name}'
    plt.savefig(file_path)
def mk_cloud(lst2):
    lst3 = lst2[:40]
    txt=''
    for item in lst3:
        txt+=item[0]+','
    wordcloud=WordCloud(background_color="#DCDCDC",width=1000,height=600,font_path='simhei.ttf',max_words=200).generate(txt)
    plt.imshow(wordcloud)
    #存到output文件
    dir1='./output'
    file_name='弹幕词云图.png'
    file_path=f'{dir1}/{file_name}'
    wordcloud.to_file(file_path)