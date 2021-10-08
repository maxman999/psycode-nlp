def dataSetter(user_email):
    import pymysql
    import pandas as pd
    from collections import Counter

    # db pass 설정a
    f = open("db_info.txt", 'r')
    lines = f.readlines()
    user = lines[0][:-1]
    passwd = lines[1][:-1]
    host = lines[2][:-1]
    f.close()
    
    conn = pymysql.connect(
    user=user,
    passwd=passwd,
    host=host,
    db='psycode_webservice',
    charset='utf8'
    )

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql4posts = "SELECT title, description FROM `posts` WHERE user_email='"+user_email+"';"
    cursor.execute(sql4posts)
    result1 = cursor.fetchall()
    dataframe = pd.DataFrame(result1)
    # dataframe.to_csv("dataset.csv", index=False)

    sql4keywords = "SELECT keyword1_user,keyword2_user,keyword3_user FROM `keywords` WHERE user_email='"+user_email+"';"
    user_keywords = [];
    cnt = cursor.execute(sql4keywords)
    if cnt > 0:
        result2 = cursor.fetchall()
        user_keywords += list(result2[0].values()) 

    conn.close()
    return dataframe, user_keywords
