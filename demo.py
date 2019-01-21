'''
    利用TextRank4ZH 来读取文本信息的摘要信息
'''

import sys
import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence


# try:
#     reload(sys)
#     sys.setdefaultencoding('utf-8')
# except:
#     pass



text = codecs.open("five.txt", 'r', 'utf-8').read()
tr4w = TextRank4Keyword()

tr4w.analyze(text=text, lower=True, window=2)

print ("\n关键词：")
for item in tr4w.get_keywords(10, word_min_len=2):
    print (item.word, item.weight)

print ("\n关键短语：")
for phrase in tr4w.get_keyphrases(keywords_num=25, min_occur_num= 1):
    print (phrase)

tr4s = TextRank4Sentence()
tr4s.analyze(text=text, lower=True, source = 'all_filters')

print ("\n摘要：")
for item in tr4s.get_key_sentences(num=5):
    print (item.index, item.weight, item.sentence)