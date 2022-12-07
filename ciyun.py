from wordcloud import WordCloud   #词云图
import jieba
from nltk import *

def CY(t,file):
    ls = jieba.lcut(t)
    #词云图
    fdist = FreqDist(ls)
    fd_sort = sorted(fdist.items(), key=lambda d: d[1],reverse=True)

    wc1 = WordCloud(
        background_color="white",width=600,
        height=300,max_words=50,
        font_path="C:\\Windows\\Fonts\\STFANGSO.ttf",#不加这一句显示口字形乱码
    )
    wc2 = wc1.generate(' '.join(ls))
    #显示词云图
    #plt.imshow(wc2)
    #plt.axis("off")
    #plt.savefig(file, dpi=750, bbox_inches = 'tight')
    wc2.to_file(file + '.png')



