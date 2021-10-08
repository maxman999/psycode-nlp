from flask import Flask, request
from flask_cors import CORS

import json
import pandas as pd
import random

from dataSetting import dataSetter
from keyword_extraction import extractor


app = Flask(__name__)
CORS(app, resources={r'*': {'origins': 'http://psy-code.com'}})

@app.route('/hello')
def hello():
    return "hello world!"

@app.route('/getKeyword')
def getKeyword():
    user_email = request.args.get('user_email')
    news_df, user_keyword = dataSetter(user_email)
    print(user_keyword)
    # 개발용 extractor
    # key_dict = mockExtractor(news_df, user_keyword) 
    # 배포용 extractor
    key_dict = extractor(news_df, user_keyword) 
    print(key_dict)
    keyword = {"keyword" : random.choice(list(key_dict))[0]} 
    keyword_json = json.dumps(keyword, ensure_ascii=False)
    print(keyword_json)
    
    return keyword_json

app.run(host = 'ec2-15-165-82-52.ap-northeast-2.compute.amazonaws.com', port=5000)

