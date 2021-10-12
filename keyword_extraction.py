#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import re
from konlpy.tag import Kkma
from collections import Counter

def extractor(news_df, user_keywords):
    kkma = Kkma()
    stopwords = []
    stopwords += user_keywords

    # title과 desciption을 합친 pandas.Series 데이터 셋(length = 수집한 news의 개수)
    data = news_df.get("title") + " " + news_df.get("description")
    word_list = data

    content_list = [] # pandas.Series 데이터 셋을 list로 변환
    for i in range(len(data)):
        content_list.append(data.iloc[i])
    
    content_result = [] # 의미 없는 문자들이 제거 된 데이터 셋
    only_BMP_pattern = re.compile("["
            u"\U00010000-\U0010FFFF" 
                              "]+", flags=re.UNICODE)
    han = re.compile(r'[ㄱ-ㅎㅏ-ㅣ!?~,".\n\r#\ufeff\u200d]')
    mypattern = re.compile(u'\u200b')

    for j in range(len(word_list)):
        target = re.sub(only_BMP_pattern,"",str(word_list[j]))
        target = re.sub(han,"",target)
        target = re.sub(mypattern,"",target)
        content_result.append(target)

    sentences_tag = [] # 말뭉치를 형태소 별로 분류
    for k in content_result:
        try:
            morph = kkma.pos(k)
            sentences_tag.append(morph)
        except:
            pass

    noun_list = [] # 불용어가 제거된 명사들만 수집
    for sentence in sentences_tag:
        for word, tag in sentence:
            if tag in ['NNG'] and len(word) > 1 and word not in stopwords:
                noun_list.append(word)
    counts = Counter(noun_list)
    tags = counts.most_common(60)

    return tags[0:3]

