import os
from 项目2.scr.jiexi import *
from 项目2.scr.fenci import *
from 项目2.scr.tubiao import *
if not os.path.exists('output'):
    os.mkdir('output')
words=anly('../项目1/data/sample.xml')
lst2=fre(words)
mk_pie(lst2)
mk_bar(lst2)
mk_cloud(lst2)