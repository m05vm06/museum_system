# import pandas as pd
# import numpy as np
import mysql.connector
import streamlit as st
from datetime import datetime

def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False

def login():
    global member_login
    member_login = True

def memberName(name):
    return name
connection = mysql.connector.connect(host = 'localhost',
                                        port='3306',
                                        user = 'root',
                                        password = 'samery123',
                                        database = 'demo')

cursor = connection.cursor()
cursor.execute('SELECT `email`, `password` FROM `member`;')


records = cursor.fetchall()
# print(type(records))
# for r in records:
#     print(r)
    

member_login =False

memName = ""
password = ""
st.sidebar.header('博物館系統')
item = st.sidebar.selectbox('目錄',['首頁', '瀏覽活動', '瀏覽展覽', '查詢文物', '登入會員', '修改會員資料', '註冊會員', '報名展覽', '報名活動'])
if item == '首頁':
    st.header('博物館')
    st.image('./國立故宮博物院.jpg')
    st.markdown('### 院史')
    st.markdown('##### 文物因緣際會來到臺灣，成為臺灣多元文化源流極重要的一部分。回溯歷史，其承繼數千年中國文化之珍稀，肩負開物成務的重大使命。國立故宮博物院庋藏文物，原屬中央博物院籌備處者，多係古物陳列所舊藏，為熱河、瀋陽行宮所有。今日國立故宮博物院典藏主體，實匯集北平、熱河、瀋陽三處清宮之文物。')
    st.markdown('### 館舍園區')
    st.markdown('##### 民國54年（1965）8月，臺北外雙溪新館竣工，蔣中正總統題署「中山博物院」門額以紀念國父孫中山先生。同年11月12日正式揭幕。正館為中國宮殿式建築，樓高四層，斗拱出踩、棟宇翬飛、綠瓦黃脊，後又經民國56年（1967）、民國58年（1969）兩次擴建，並於民國74年（1985）進行展場重新規畫整修，現於民國93年7月（2004）重新裝修，民國96年（2007）12月完工開展，一、二、三層為展覽陳列空間，四樓為休憩茶座「三希堂」。院區左側「至善園」民國73年（1984）動工；園內融合中國傳統園林理念，樓臺入畫，片石生情，小橋流水，靈沼曲徑，表現樸實悠閒的情趣。亭台樑柱，鐫刻古賢法書聯句，翰逸神飛，更增遊賞雅致。院區右側畸零地闢建開放性庭園──「至德園」，園中曲橋池沼、小亭憑望。每逢秋夜清涼，桂馥荷香，迎風飄送，更令人神馳嚮往，久久不已。附帶一提的是，民國72年（1983）5月，張大千先生的家屬將張大千生前的住所「摩耶精舍」，捐贈歸故宮管理；故宮因此成立「張大千先生紀念館」，供民眾申請參觀。館臨雙溪茅亭垂蔭，鶴鳴猿啼，書齋有張先生蠟像，更增幽情。')
    st.markdown('##### 至善園  蘭亭')
    st.image('./蘭亭.jpg')
    st.markdown('##### 至善園  碧橋西水榭')
    st.image('./碧橋西水榭.jpg')
    st.markdown('##### 至善園  羲之書換籠鵝造像')
    st.image('./羲之書換籠鵝造像.jpg')
    st.markdown('##### 至善園  龍池')
    st.image('./龍池.jpg')

if item == '瀏覽活動' :
    cursor = connection.cursor()
    cursor.execute('SELECT `aName` FROM `activity`;')
    records = cursor.fetchall()
    listrecords = []
    for i in records:
        listrecords.append(''.join(i))
    st.header('活動目錄')
    aName = st.selectbox('選擇活動項目', listrecords)
    if aName == listrecords[0]:
        cursor = connection.cursor()
        sql = 'SELECT `content` FROM `activity` where `aName` = %s;'
        name = (listrecords[0],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 = '##### ' + content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            
            sql = 'SELECT `url` FROM `activity` where `aName` = %s;'
            name = (listrecords[0],)
            sql2 = 'SELECT `price` FROM `activity` where `aName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            sql1 = 'SELECT `pName` FROM `activity` where `aName` = %s;'
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            pName = []
            for i in records:
                pName.append(''.join(i))
            pName1 = "活動場地 : " + pName[0]
            st.write(pName1)
            aNo = ('a0001',)
            cursor.execute('SELECT `aTime` FROM `atime` where `aNo` = %s;', aNo)
            records = cursor.fetchall()
            atime = []
            for i in records:
                atime.append(''.join(i))
            atime1 = "活動時間 : " + atime[0]
            st.write(atime1)
            cursor.execute(sql, name)
            records = cursor.fetchall()
            url = []
            for i in records:
                url.append(''.join(i))
            url1 = '參考網址:[link]('+url[0]+')'
            st.write(url1)
    if aName == listrecords[1]:
        cursor = connection.cursor()
        sql = 'SELECT `content` FROM `activity` where `aName` = %s;'
        name = (listrecords[1],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 = '##### ' + content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            sql = 'SELECT `url` FROM `activity` where `aName` = %s;'
            name = (listrecords[0],)
            sql2 = 'SELECT `price` FROM `activity` where `aName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            sql1 = 'SELECT `pName` FROM `activity` where `aName` = %s;'
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            pName = []
            for i in records:
                pName.append(''.join(i))
            pName1 = "活動場地 : " + pName[0]
            st.write(pName1)
            aNo = ('a0002',)
            cursor.execute('SELECT `aTime` FROM `atime` where `aNo` = %s;', aNo)
            records = cursor.fetchall()
            atime = []
            for i in records:
                atime.append(''.join(i))
            atime1 = "活動時間 : " + atime[0]
            st.write(atime1)
            cursor.execute(sql, name)
            records = cursor.fetchall()
            url = []
            for i in records:
                url.append(''.join(i))
            url1 = '參考網址:[link]('+url[0]+')'
            st.write(url1)
    if aName == listrecords[2]:
        cursor = connection.cursor()
        sql = 'SELECT `content` FROM `activity` where `aName` = %s;'
        name = (listrecords[2],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 = '##### ' + content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            sql = 'SELECT `url` FROM `activity` where `aName` = %s;'
            name = (listrecords[0],)
            sql2 = 'SELECT `price` FROM `activity` where `aName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            sql1 = 'SELECT `pName` FROM `activity` where `aName` = %s;'
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            pName = []
            for i in records:
                pName.append(''.join(i))
            pName1 = "活動場地 : " + pName[0]
            st.write(pName1)
            aNo = ('a0003',)
            cursor.execute('SELECT `aTime` FROM `atime` where `aNo` = %s;', aNo)
            records = cursor.fetchall()
            atime = []
            for i in records:
                atime.append(''.join(i))
            atime1 = "活動時間 : " + atime[0]
            st.write(atime1)
            cursor.execute(sql, name)
            records = cursor.fetchall()
            url = []
            for i in records:
                url.append(''.join(i))
            url1 = '參考網址:[link]('+url[0]+')'
            st.write(url1)
    if aName == listrecords[3]:
        cursor = connection.cursor()
        sql = 'SELECT `content` FROM `activity` where `aName` = %s;'
        name = (listrecords[3],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 = '##### ' + content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            sql = 'SELECT `url` FROM `activity` where `aName` = %s;'
            name = (listrecords[0],)
            sql1 = 'SELECT `pName` FROM `activity` where `aName` = %s;'
            sql2 = 'SELECT `price` FROM `activity` where `aName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            pName = []
            for i in records:
                pName.append(''.join(i))
            pName1 = "活動場地 : " + pName[0]
            st.write(pName1)
            aNo = ('a0004',)
            cursor.execute('SELECT `aTime` FROM `atime` where `aNo` = %s;', aNo)
            records = cursor.fetchall()
            atime = []
            for i in records:
                atime.append(''.join(i))
            atime1 = "活動時間 : " + atime[0]
            st.write(atime1)
            cursor.execute(sql, name)
            records = cursor.fetchall()
            url = []
            for i in records:
                url.append(''.join(i))
            url1 = '參考網址:[link]('+url[0]+')'
            st.write(url1)
    if aName == listrecords[4]:
        cursor = connection.cursor()
        sql = 'SELECT `content` FROM `activity` where `aName` = %s;'
        name = (listrecords[4],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 = '##### ' + content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            sql = 'SELECT `url` FROM `activity` where `aName` = %s;'
            name = (listrecords[0],)
            sql1 = 'SELECT `pName` FROM `activity` where `aName` = %s;'
            sql2 = 'SELECT `price` FROM `activity` where `aName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            pName = []
            for i in records:
                pName.append(''.join(i))
            pName1 = "活動場地 : " + pName[0]
            st.write(pName1)
            aNo = ('a0005',)
            cursor.execute('SELECT `aTime` FROM `atime` where `aNo` = %s;', aNo)
            records = cursor.fetchall()
            atime = []
            for i in records:
                atime.append(''.join(i))
            atime1 = "活動時間 : " + atime[0]
            st.write(atime1)
            cursor.execute(sql, name)
            records = cursor.fetchall()
            url = []
            for i in records:
                url.append(''.join(i))
            url1 = '參考網址:[link]('+url[0]+')'
            st.write(url1)
    if aName == listrecords[5]:
        cursor = connection.cursor()
        sql = 'SELECT `content` FROM `activity` where `aName` = %s;'
        name = (listrecords[5],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 = '##### ' + content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            sql = 'SELECT `url` FROM `activity` where `aName` = %s;'
            name = (listrecords[0],)
            sql2 = 'SELECT `price` FROM `activity` where `aName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            sql1 = 'SELECT `pName` FROM `activity` where `aName` = %s;'
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            pName = []
            for i in records:
                pName.append(''.join(i))
            pName1 = "活動場地 : " + pName[0]
            st.write(pName1)
            aNo = ('a0006',)
            cursor.execute('SELECT `aTime` FROM `atime` where `aNo` = %s;', aNo)
            records = cursor.fetchall()
            atime = []
            for i in records:
                atime.append(''.join(i))
            atime1 = "活動時間 : " + atime[0]
            st.write(atime1)
            cursor.execute(sql, name)
            records = cursor.fetchall()
            url = []
            for i in records:
                url.append(''.join(i))
            url1 = '參考網址:[link]('+url[0]+')'
            st.write(url1)
    if aName == listrecords[6]:
        cursor = connection.cursor()
        sql = 'SELECT `content` FROM `activity` where `aName` = %s;'
        name = (listrecords[6],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 = '##### ' + content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            sql = 'SELECT `url` FROM `activity` where `aName` = %s;'
            name = (listrecords[0],)
            sql2 = 'SELECT `price` FROM `activity` where `aName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            sql1 = 'SELECT `pName` FROM `activity` where `aName` = %s;'
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            pName = []
            for i in records:
                pName.append(''.join(i))
            pName1 = "活動場地 : " + pName[0]
            st.write(pName1)
            aNo = ('a0007',)
            cursor.execute('SELECT `aTime` FROM `atime` where `aNo` = %s;', aNo)
            records = cursor.fetchall()
            atime = []
            for i in records:
                atime.append(''.join(i))
            atime1 = "活動時間 : " + atime[0]
            st.write(atime1)
            cursor.execute(sql, name)
            records = cursor.fetchall()
            url = []
            for i in records:
                url.append(''.join(i))
            url1 = '參考網址:[link]('+url[0]+')'
            st.write(url1)
    if aName == listrecords[7]:
        cursor = connection.cursor()
        sql = 'SELECT `content` FROM `activity` where `aName` = %s;'
        name = (listrecords[7],)
        sql2 = 'SELECT `price` FROM `activity` where `aName` = %s;'
        cursor.execute(sql2, name)
        records = cursor.fetchall()
        price = []
        for i in records:
            price.append(''.join(i))
        price1 = "價格 : " + price[0]
        st.write(price1)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 = '##### ' + content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            sql = 'SELECT `url` FROM `activity` where `aName` = %s;'
            name = (listrecords[0],)
            sql1 = 'SELECT `pName` FROM `activity` where `aName` = %s;'
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            pName = []
            for i in records:
                pName.append(''.join(i))
            pName1 = "活動場地 : " + pName[0]
            st.write(pName1)
            aNo = ('a0008',)
            cursor.execute('SELECT `aTime` FROM `atime` where `aNo` = %s;', aNo)
            records = cursor.fetchall()
            atime = []
            for i in records:
                atime.append(''.join(i))
            atime1 = "活動時間 : " + atime[0]
            st.write(atime1)
            cursor.execute(sql, name)
            records = cursor.fetchall()
            url = []
            for i in records:
                url.append(''.join(i))
            url1 = '參考網址:[link]('+url[0]+')'
            st.write(url1)
    if aName == listrecords[8]:
        cursor = connection.cursor()
        sql = 'SELECT `content` FROM `activity` where `aName` = %s;'
        name = (listrecords[8],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 = '##### ' + content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            sql = 'SELECT `url` FROM `activity` where `aName` = %s;'
            name = (listrecords[0],)
            sql2 = 'SELECT `price` FROM `activity` where `aName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            sql1 = 'SELECT `pName` FROM `activity` where `aName` = %s;'
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            pName = []
            for i in records:
                pName.append(''.join(i))
            pName1 = "活動場地 : " + pName[0]
            st.write(pName1)
            aNo = ('a0009',)
            cursor.execute('SELECT `aTime` FROM `atime` where `aNo` = %s;', aNo)
            records = cursor.fetchall()
            atime = []
            for i in records:
                atime.append(''.join(i))
            atime1 = "活動時間 : " + atime[0]
            st.write(atime1)
            cursor.execute(sql, name)
            records = cursor.fetchall()
            url = []
            for i in records:
                url.append(''.join(i))
            url1 = '參考網址:[link]('+url[0]+')'
            st.write(url1)
    if aName == listrecords[9]:
        cursor = connection.cursor()
        sql = 'SELECT `content` FROM `activity` where `aName` = %s;'
        name = (listrecords[9],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 = '##### ' + content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            name = (listrecords[0],)
            sql = 'SELECT `url` FROM `activity` where `aName` = %s;'
            sql1 = 'SELECT `pName` FROM `activity` where `aName` = %s;'
            sql2 = 'SELECT `price` FROM `activity` where `aName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            pName = []
            for i in records:
                pName.append(''.join(i))
            pName1 = "活動場地 : " + pName[0]
            st.write(pName1)
            aNo = ('a0010',)
            cursor.execute('SELECT `aTime` FROM `atime` where `aNo` = %s;', aNo)
            records = cursor.fetchall()
            atime = []
            for i in records:
                atime.append(''.join(i))
            atime1 = "活動時間 : " + atime[0]
            st.write(atime1)
            cursor.execute(sql, name)
            records = cursor.fetchall()
            url = []
            for i in records:
                url.append(''.join(i))
            url1 = '參考網址:[link]('+url[0]+')'
            st.write(url1)
    
if item == '瀏覽展覽' :
    cursor = connection.cursor()
    cursor.execute('SELECT `eName` FROM `exhibition`;')
    records = cursor.fetchall()
    listrecords = []
    for i in records:
        listrecords.append(''.join(i))
    st.header('展覽目錄')
    eName = st.selectbox('選擇展覽項目', listrecords)
    if eName == listrecords[0]:
        cursor = connection.cursor()
        sql = 'SELECT `theme` FROM `exhibition` where `eName` = %s;'
        name = (listrecords[0],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 = content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            sql1 = 'SELECT `gallery` FROM `gallery` where `eName` = %s;'
            sql2 = 'SELECT `eprice` FROM `exhibition` where `eName` = %s;'
            sql3 = 'SELECT cName FROM exhibit join collection WHERE exhibit.cId = demo.collection.cId and demo.exhibit.eName = %s;'
            sql4 = 'SELECT `dates` FROM `exhibition` where `eName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            cursor.execute(sql4, name)
            records = cursor.fetchall()
            date = []
            for i in records:
                date.append(''.join(i))
            date1 = "開始日期 : " + date[0]
            st.write(date1)
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            eName = []
            for i in records:
                eName.append(''.join(i))
            eName1 = "陳列室 : " + eName[0]
            st.write(eName1)
            cursor.execute(sql3, name)
            records = cursor.fetchall()
            collection = []
            for i in records:
                collection.append(''.join(i))
            collection1 = "相關文物 : "
            for j in  range(len(collection)):
                collection1 += (collection[j] + ', ')
            st.write(collection1)
    if eName == listrecords[1]:
        cursor = connection.cursor()
        sql = 'SELECT `theme` FROM `exhibition` where `eName` = %s;'
        name = (listrecords[1],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 = content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            sql1 = 'SELECT `gallery` FROM `gallery` where `eName` = %s;'
            sql2 = 'SELECT `eprice` FROM `exhibition` where `eName` = %s;'
            sql3 = 'SELECT cName FROM exhibit join collection WHERE exhibit.cId = demo.collection.cId and demo.exhibit.eName = %s;'
            sql4 = 'SELECT `dates` FROM `exhibition` where `eName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            cursor.execute(sql4, name)
            records = cursor.fetchall()
            date = []
            for i in records:
                date.append(''.join(i))
            date1 = "開始日期 : " + date[0]
            st.write(date1)
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            eName = []
            for i in records:
                eName.append(''.join(i))
            eName1 = "陳列室 : " + eName[0]
            st.write(eName1)
            cursor.execute(sql3, name)
            records = cursor.fetchall()
            collection = []
            for i in records:
                collection.append(''.join(i))
            collection1 = "相關文物 : "
            for j in  range(len(collection)):
                collection1 += (collection[j] + ', ')
            st.write(collection1)
    if eName == listrecords[2]:
        cursor = connection.cursor()
        sql = 'SELECT `theme` FROM `exhibition` where `eName` = %s;'
        name = (listrecords[2],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 =  content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            sql1 = 'SELECT `gallery` FROM `gallery` where `eName` = %s;'
            sql2 = 'SELECT `eprice` FROM `exhibition` where `eName` = %s;'
            sql3 = 'SELECT cName FROM exhibit join collection WHERE exhibit.cId = demo.collection.cId and demo.exhibit.eName = %s;'
            sql4 = 'SELECT `dates` FROM `exhibition` where `eName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            cursor.execute(sql4, name)
            records = cursor.fetchall()
            date = []
            for i in records:
                date.append(''.join(i))
            date1 = "開始日期 : " + date[0]
            st.write(date1)
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            eName = []
            for i in records:
                eName.append(''.join(i))
            eName1 = "陳列室 : " + eName[0]
            st.write(eName1)
            cursor.execute(sql3, name)
            records = cursor.fetchall()
            collection = []
            for i in records:
                collection.append(''.join(i))
            collection1 = "相關文物 : "
            for j in  range(len(collection)):
                collection1 += (collection[j] + ', ')
            st.write(collection1)
    if eName == listrecords[3]:
        cursor = connection.cursor()
        sql = 'SELECT `theme` FROM `exhibition` where `eName` = %s;'
        name = (listrecords[3],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 = content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            sql1 = 'SELECT `gallery` FROM `gallery` where `eName` = %s;'
            sql2 = 'SELECT `eprice` FROM `exhibition` where `eName` = %s;'
            sql3 = 'SELECT cName FROM exhibit join collection WHERE exhibit.cId = demo.collection.cId and demo.exhibit.eName = %s;'
            sql4 = 'SELECT `dates` FROM `exhibition` where `eName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            cursor.execute(sql4, name)
            records = cursor.fetchall()
            date = []
            for i in records:
                date.append(''.join(i))
            date1 = "開始日期 : " + date[0]
            st.write(date1)
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            eName = []
            for i in records:
                eName.append(''.join(i))
            eName1 = "陳列室 : " + eName[0]
            st.write(eName1)
            cursor.execute(sql3, name)
            records = cursor.fetchall()
            collection = []
            for i in records:
                collection.append(''.join(i))
            collection1 = "相關文物 : "
            for j in  range(len(collection)):
                collection1 += (collection[j] + ', ')
            st.write(collection1)
    if eName == listrecords[4]:
        cursor = connection.cursor()
        sql = 'SELECT `theme` FROM `exhibition` where `eName` = %s;'
        name = (listrecords[4],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 = content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            sql1 = 'SELECT `gallery` FROM `gallery` where `eName` = %s;'
            sql2 = 'SELECT `eprice` FROM `exhibition` where `eName` = %s;'
            sql3 = 'SELECT cName FROM exhibit join collection WHERE exhibit.cId = demo.collection.cId and demo.exhibit.eName = %s;'
            sql4 = 'SELECT `dates` FROM `exhibition` where `eName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            cursor.execute(sql4, name)
            records = cursor.fetchall()
            date = []
            for i in records:
                date.append(''.join(i))
            date1 = "開始日期 : " + date[0]
            st.write(date1)
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            eName = []
            for i in records:
                eName.append(''.join(i))
            eName1 = "陳列室 : " + eName[0]
            st.write(eName1)
            cursor.execute(sql3, name)
            records = cursor.fetchall()
            collection = []
            for i in records:
                collection.append(''.join(i))
            collection1 = "相關文物 : "
            for j in  range(len(collection)):
                collection1 += (collection[j] + ', ')
            st.write(collection1)
    if eName == listrecords[5]:
        cursor = connection.cursor()
        sql = 'SELECT `theme` FROM `exhibition` where `eName` = %s;'
        name = (listrecords[5],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 =  content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            sql1 = 'SELECT `gallery` FROM `gallery` where `eName` = %s;'
            sql2 = 'SELECT `eprice` FROM `exhibition` where `eName` = %s;'
            sql3 = 'SELECT cName FROM exhibit join collection WHERE exhibit.cId = demo.collection.cId and demo.exhibit.eName = %s;'
            sql4 = 'SELECT `dates` FROM `exhibition` where `eName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            cursor.execute(sql4, name)
            records = cursor.fetchall()
            date = []
            for i in records:
                date.append(''.join(i))
            date1 = "開始日期 : " + date[0]
            st.write(date1)
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            eName = []
            for i in records:
                eName.append(''.join(i))
            eName1 = "陳列室 : " + eName[0]
            st.write(eName1)
            cursor.execute(sql3, name)
            records = cursor.fetchall()
            collection = []
            for i in records:
                collection.append(''.join(i))
            collection1 = "相關文物 : "
            for j in  range(len(collection)):
                collection1 += (collection[j] + ', ')
            st.write(collection1)
    if eName == listrecords[6]:
        cursor = connection.cursor()
        sql = 'SELECT `theme` FROM `exhibition` where `eName` = %s;'
        name = (listrecords[6],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 =  content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            sql1 = 'SELECT `gallery` FROM `gallery` where `eName` = %s;'
            sql2 = 'SELECT `eprice` FROM `exhibition` where `eName` = %s;'
            sql3 = 'SELECT cName FROM exhibit join collection WHERE exhibit.cId = demo.collection.cId and demo.exhibit.eName = %s;'
            sql4 = 'SELECT `dates` FROM `exhibition` where `eName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            cursor.execute(sql4, name)
            records = cursor.fetchall()
            date = []
            for i in records:
                date.append(''.join(i))
            date1 = "開始日期 : " + date[0]
            st.write(date1)
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            eName = []
            for i in records:
                eName.append(''.join(i))
            eName1 = "陳列室 : " + eName[0]
            st.write(eName1)
            cursor.execute(sql3, name)
            records = cursor.fetchall()
            collection = []
            for i in records:
                collection.append(''.join(i))
            collection1 = "相關文物 : "
            for j in  range(len(collection)):
                collection1 += (collection[j] + ', ')
            st.write(collection1)
    if eName == listrecords[7]:
        cursor = connection.cursor()
        sql = 'SELECT `theme` FROM `exhibition` where `eName` = %s;'
        name = (listrecords[7],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 =  content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            sql1 = 'SELECT `gallery` FROM `gallery` where `eName` = %s;'
            sql2 = 'SELECT `eprice` FROM `exhibition` where `eName` = %s;'
            sql3 = 'SELECT cName FROM exhibit join collection WHERE exhibit.cId = demo.collection.cId and demo.exhibit.eName = %s;'
            sql4 = 'SELECT `dates` FROM `exhibition` where `eName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            cursor.execute(sql4, name)
            records = cursor.fetchall()
            date = []
            for i in records:
                date.append(''.join(i))
            date1 = "開始日期 : " + date[0]
            st.write(date1)
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            eName = []
            for i in records:
                eName.append(''.join(i))
            eName1 = "陳列室 : " + eName[0]
            st.write(eName1)
            cursor.execute(sql3, name)
            records = cursor.fetchall()
            collection = []
            for i in records:
                collection.append(''.join(i))
            collection1 = "相關文物 : "
            for j in  range(len(collection)):
                collection1 += (collection[j] + ', ')
            st.write(collection1)
    if eName == listrecords[8]:
        cursor = connection.cursor()
        sql = 'SELECT `theme` FROM `exhibition` where `eName` = %s;'
        name = (listrecords[8],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 = content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            sql1 = 'SELECT `gallery` FROM `gallery` where `eName` = %s;'
            sql2 = 'SELECT `eprice` FROM `exhibition` where `eName` = %s;'
            sql3 = 'SELECT cName FROM exhibit join collection WHERE exhibit.cId = demo.collection.cId and demo.exhibit.eName = %s;'
            sql4 = 'SELECT `dates` FROM `exhibition` where `eName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            cursor.execute(sql4, name)
            records = cursor.fetchall()
            date = []
            for i in records:
                date.append(''.join(i))
            date1 = "開始日期 : " + date[0]
            st.write(date1)
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            eName = []
            for i in records:
                eName.append(''.join(i))
            eName1 = "陳列室 : " + eName[0]
            st.write(eName1)
            cursor.execute(sql3, name)
            records = cursor.fetchall()
            collection = []
            for i in records:
                collection.append(''.join(i))
            collection1 = "相關文物 : "
            for j in  range(len(collection)):
                collection1 += (collection[j] + ', ')
            st.write(collection1)
    if eName == listrecords[9]:
        cursor = connection.cursor()
        sql = 'SELECT `theme` FROM `exhibition` where `eName` = %s;'
        name = (listrecords[9],)
        cursor.execute(sql, name)
        records = cursor.fetchall()
        content = []
        for i in records:
            content.append(''.join(i))
        content1 = content[0]
        st.write(' ')
        st.write(' ')
        st.markdown(content1)
        detail = st.button('細部說明')
        if detail:
            cursor = connection.cursor()
            sql1 = 'SELECT `gallery` FROM `gallery` where `eName` = %s;'
            sql2 = 'SELECT `eprice` FROM `exhibition` where `eName` = %s;'
            sql3 = 'SELECT cName FROM exhibit join collection WHERE exhibit.cId = demo.collection.cId and demo.exhibit.eName = %s;'
            sql4 = 'SELECT `dates` FROM `exhibition` where `eName` = %s;'
            cursor.execute(sql2, name)
            records = cursor.fetchall()
            price = []
            for i in records:
                price.append(''.join(i))
            price1 = "價格 : " + price[0]
            st.write(price1)
            cursor.execute(sql4, name)
            records = cursor.fetchall()
            date = []
            for i in records:
                date.append(''.join(i))
            date1 = "開始日期 : " + date[0]
            st.write(date1)
            cursor.execute(sql1, name)
            records = cursor.fetchall()
            eName = []
            for i in records:
                eName.append(''.join(i))
            eName1 = "陳列室 : " + eName[0]
            st.write(eName1)
            cursor.execute(sql3, name)
            records = cursor.fetchall()
            collection = []
            for i in records:
                collection.append(''.join(i))
            collection1 = "相關文物 : "
            for j in  range(len(collection)):
                collection1 += (collection[j] + ', ')
            st.write(collection1)

if item == '查詢文物' :
    st.header('文物查詢')
    search1 = st.text_input('查詢')
    srhBtn = st.button('搜尋')
    if srhBtn:
        search2 = (search1,)
        cursor.execute('SELECT `cName` FROM `collection`;')
        record  = cursor.fetchall()
        if search2 in record:
            cName = "#### "+"".join(search2)
            st.markdown(cName)
            collectionInfo = 'SELECT `cInfo` FROM `collection` WHERE `cName` = %s;'
            collectionSize = 'SELECT `cSize` FROM `collection` WHERE `cName` = %s;'
            collectionMaterial = 'SELECT `material` FROM `collection` WHERE `cName` = %s;'
            collectionCategory = 'SELECT `category` FROM `collection` WHERE `cName` = %s;'
            collectionFeature = 'SELECT `feature` FROM `collection` WHERE `cName` = %s;'
            collectionPeriod = 'SELECT `period` FROM `collection` WHERE `cName` = %s;'
            st.markdown("#### 文物資訊:")
            cursor.execute(collectionInfo, search2)
            records = cursor.fetchall()
            if records == [(None,), (None,)] or records == [(None,)]:
                st.markdown("##### 無")
            else:
                info = []
                for i in records:
                    info.append("".join(i))
                info1 ="##### " + info[0]
                st.markdown(info1)
            st.markdown("#### 時代:")
            cursor.execute(collectionPeriod, search2)
            records = cursor.fetchall()
            if records == [(None,), (None,)] or records == [(None,)]:
                st.markdown("##### 無")
            else:
                period = []
                for i in records:
                    period.append("".join(i))
                period1 ="##### " + period[0]
                st.markdown(period1)
            st.markdown("#### 大小:")
            cursor.execute(collectionSize, search2)
            records = cursor.fetchall()
            if records == [(None,), (None,)] or records == [(None,)]:
                st.markdown("##### 無")
            else:
                size = []
                for i in records:
                    size.append("".join(i))
                size1 ="##### " + size[0]
                st.markdown(size1)
            st.markdown("#### 材質:")
            cursor.execute(collectionMaterial, search2)
            records = cursor.fetchall()
            if records == [(None,), (None,)] or records == [(None,)]:
                st.markdown("##### 無")
            else:
                material = []
                for i in records:
                    material.append("".join(i))
                material1 ="##### " + material[0]
                st.markdown(material1)
            st.markdown("#### 種類:")
            cursor.execute(collectionCategory, search2)
            records = cursor.fetchall()
            if records == [(None,), (None,)] or records == [(None,)]:
                st.markdown("##### 無")
            else:
                category = []
                for i in records:
                    category.append("".join(i))
                category1 ="##### " + category[0]
                st.markdown(category1)
            st.markdown("#### 功能:")
            cursor.execute(collectionFeature, search2)
            records = cursor.fetchall()
            if records == [(None,), (None,)] or records == [(None,)]:
                st.markdown("##### 無")
            else:
                feature = []
                for i in records:
                    feature.append("".join(i))
                feature1 ="##### " + feature[0]
                st.markdown(feature1)
            
        else:
            st.markdown('#### 沒有此文物')

if item == '登入會員' :
    if member_login:
        st.write("您已登入成功")
        # cursor1.execute('SELECT `[會員名稱]` FROM `姓名` WHERE `password` = password;')
        # memName = cursor1.fetchall()
        # st.write(memName+"會員您好")
    else:
        with st.form("my_form"):
            st.header('登入會員')
            email = st.text_input('email')
            password = st.text_input('密碼', type = 'password')
            signIn = st.form_submit_button('Login')
        if signIn :
            for r in records:
                if search(r, email) & search(r, password):
                    st.write('登入成功')
                    login()
                    cursor = connection.cursor()
                    sql = 'SELECT `姓名` FROM `member` WHERE `password` = %s;'
                    pwd = (password,)
                    cursor.execute(sql, pwd)
                    record = cursor.fetchall()
                    memName = "".join(record[0])
                    st.write(memName+"  先生(小姐)您好")
                    break
            else:
                st.write('登入失敗')

        
if item == '修改會員資料' : 
    st.header('登入會員')
    email = st.text_input('email')
    password = st.text_input('密碼', type = 'password')
    modphone = st.text_input('輸入新電話號碼')
    modaddress = st.text_input('輸入新地址')
    modemail = st.text_input('輸入新email')
    modpwd = st.text_input('輸入新密碼', type = 'password')
    modpwd1 = st.text_input('再輸入一次密碼', type = 'password')
    confirmBtn = st.button('確認')
    if confirmBtn:
        for r in records:
            if search(r, email) & search(r, password):
                st.write('登入成功')
                login()
                cursor = connection.cursor()
                sql = 'SELECT `姓名` FROM `member` WHERE `password` = %s;'
                pwd = (password,)
                cursor.execute(sql, pwd)
                record = cursor.fetchall()
                memName = "".join(record[0])
                st.write(memName+"  先生(小姐)您好")
                if modphone != "" and len(modphone) == 10:
                    sql = 'UPDATE `member` SET `電話` = %s where `姓名` = %s;'
                    new_data = (modphone, memName)
                    cursor = connection.cursor()
                    cursor.execute(sql, new_data)
                    connection.commit()
                    st.write('電話號碼修改成功')
                elif modphone != "":
                    st.write('輸入電話號碼內容錯誤')
                if modaddress != "" and len(modaddress) > 10:
                    sql = 'UPDATE `member` SET `地址` = %s where `姓名` = %s;'
                    new_data = (modaddress, memName)
                    cursor = connection.cursor()
                    cursor.execute(sql, new_data)
                    connection.commit()
                    st.write('住址修改成功')
                elif modaddress !="":
                    st.write('輸入地址太短')
                if modemail != "" :
                    sql = 'UPDATE `member` SET `email` = %s where `姓名` = %s;'
                    new_data = (modemail, memName)
                    cursor = connection.cursor()
                    cursor.execute(sql, new_data)
                    connection.commit()
                    st.write('email修改成功')
                if modpwd != "" and modpwd1 !="" and 15 > len(modpwd1)>7 and modpwd == modpwd1:
                    sql = 'UPDATE `member` SET `password` = %s where `姓名` = %s;'
                    new_data = (modpwd, memName)
                    cursor = connection.cursor()
                    cursor.execute(sql, new_data)
                    connection.commit()
                    st.write('密碼修改成功')
                elif modpwd != "" and modpwd1 !="":
                    st.write('輸入密碼內容錯誤')
                break
        else:
            st.write('登入失敗')
                 

          

if item == '註冊會員':
    with st.form("my_form"):
        st.header('註冊會員')
        email = st.text_input('email')
        pwd = st.text_input('密碼', type = 'password')
        confirmPwd = st.text_input('確認密碼', type = 'password')
        identify =st.text_input('身分證編號')
        name = st.text_input('姓名')
        sex  = st.selectbox('性別', ['男性', '女性'])
        birthday = st.text_input("生日(格式:西元年/月/日, yyyy/mm/dd)") 
        phone = st.text_input('電話')
        address = st.text_input('地址')
        finishBtn = st.form_submit_button('完成')
    if finishBtn:
            if pwd != confirmPwd :
                st.write('密碼輸入錯誤')
            elif len(pwd)<8:
                st.write('密碼長度太短')
            elif len(pwd)>15:
                st.write('密碼長度太長')
            elif pwd  in  records:
                st.write('密碼與其他使用者重複，請重新輸入')
            elif phone[0]!= '0' or phone[1] != '9' or len(phone)!=10:
                st.write("電話號碼輸入錯誤")
            elif 'A'>identify[0]>'Z'  or len(identify)!=10 or '1'>identify[1]>'2' or '0'>identify[2:11]>'9':
                st.write("身分證字號輸入錯誤")
            else:
                st.write('註冊成功')
                cursor.execute('SELECT `會員編號` FROM `member`;')
                recordMemNum = cursor.fetchall()
                No = []
                # print(recordMemNum)
                for i in recordMemNum:
                    No .append(''.join(i))
                # print(mNo)
                max = 0
                for i in No:
                    if max < int(i[3:5]):
                        max = int(i[3:5])
                max+=1
                print(max)
                mNo = "m00"+str(max)
                sql = "INSERT INTO member (會員編號, 身分證編號, 姓名, 生日, 電話, 地址, email, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
                new_data = (mNo, identify, name, birthday, phone, address, email, pwd)
                cursor = connection.cursor()
                cursor.execute(sql, new_data)
                connection.commit()
              
if item == '報名展覽':
    st.header('報名展覽')
    email = st.text_input('email')
    password = st.text_input('密碼', type = 'password')
    cursor = connection.cursor()
    cursor.execute('SELECT `eName` FROM `exhibition`;')
    record = cursor.fetchall()
    listrecords = []
    for i in record:
        listrecords.append(''.join(i))
    eName = st.selectbox('選擇展覽項目', listrecords)
    payment = st.selectbox('選擇付款方式', ['現金', '信用卡', '金融卡'])
    signsum = st.slider('報名人數', 1, 5, 1)
    confirmBtn = st.button('確認')
    if confirmBtn :
        for r in records:
            if search(r, email) & search(r, password):
                st.write('登入成功')
                login()
                cursor = connection.cursor()
                sql = 'SELECT `姓名` FROM `member` WHERE `password` = %s;'
                pwd = (password,)
                cursor.execute(sql, pwd)
                record = cursor.fetchall()
                memName = "".join(record[0])
                st.write(memName+"  先生(小姐)您好")
                day = datetime.now()
                datetime_format = day.strftime("%Y-%m-%d %H:%M:%S")
                print(datetime_format)
                print(type(datetime_format))
                sql2 = 'SELECT `會員編號` FROM `member` WHERE `password` = %s;'
                cursor.execute(sql2, pwd)
                record = cursor.fetchall()
                mNo = "".join(record[0])
                day = datetime.now()
                day1 = day.strftime("%Y-%m-%d %H:%M:%S")
                sql1 = "INSERT INTO signupexhibition (展覽名稱, 會員編號, 報名時間, 報名人數) VALUES (%s, %s, %s, %s);"
                data = (eName, mNo, day1, signsum)
                cursor.execute(sql1, data)
                connection.commit()
                sqlpayment = "INSERT INTO epayment(eName, payment)VALUES(%s, %s);"
                paydata = (eName, payment)
                cursor.execute(sqlpayment, paydata)
                connection.commit()
                sqlprice = "SELECT `eprice` FROM `exhibition` WHERE `eName` = %s"
                pricedata = (eName,)
                cursor.execute(sqlprice, pricedata)
                records = cursor.fetchall()
                price = []
                for i in records:
                    price.append("".join(i))
                price1 = price[0]
                print(price1)
                print(type(price1))
                sum = int(price1) * int(signsum)
                feedback = "一共要支付" + str(sum)
                st.write(feedback)
                break
        else:
            st.write("登入失敗")

if item == '報名活動':
    st.header('報名活動')
    email = st.text_input('email')
    password = st.text_input('密碼', type = 'password')
    cursor = connection.cursor()
    cursor.execute('SELECT `aName` FROM `activity`;')
    record = cursor.fetchall()
    listrecords = []
    for i in record:
        listrecords.append(''.join(i))
    aName = st.selectbox('選擇活動項目', listrecords)
    payment = st.selectbox('選擇付款方式', ['現金', '信用卡', '金融卡'])
    signsum = st.slider('報名人數', 1, 5, 1)
    confirmBtn = st.button('確認')
    if confirmBtn :
        for r in records:
            if search(r, email) & search(r, password):
                st.write('登入成功')
                login()
                cursor = connection.cursor()
                sql = 'SELECT `姓名` FROM `member` WHERE `password` = %s;'
                pwd = (password,)
                cursor.execute(sql, pwd)
                record = cursor.fetchall()
                memName = "".join(record[0])
                st.write(memName+"  先生(小姐)您好")
                day = datetime.now()
                datetime_format = day.strftime("%Y-%m-%d %H:%M:%S")
                print(datetime_format)
                print(type(datetime_format))
                sql2 = 'SELECT `會員編號` FROM `member` WHERE `password` = %s;'
                cursor.execute(sql2, pwd)
                record = cursor.fetchall()
                mNo = "".join(record[0])
                sql3 = 'SELECT `aNo` FROM `activity` WHERE `aName` = %s;'
                namedata = (aName,)
                cursor.execute(sql3, namedata)
                record = cursor.fetchall()
                aNo = "".join(record[0])
                day = datetime.now()
                day1 = day.strftime("%Y-%m-%d %H:%M:%S")
                sql1 = "INSERT INTO signupactivity (aNo, mId, asignTime, asignsum) VALUES (%s, %s, %s, %s);"
                data = (aNo, mNo, day1, signsum)
                cursor.execute(sql1, data)
                connection.commit()
                sqlpayment = "INSERT INTO apayment(aNo, payment)VALUES(%s, %s);"
                paydata = (aNo, payment)
                cursor.execute(sqlpayment, paydata)
                connection.commit()
                sqlprice = "SELECT `price` FROM `activity` WHERE `aNo` = %s"
                pricedata = (aNo,)
                cursor.execute(sqlprice, pricedata)
                records = cursor.fetchall()
                price = []
                for i in records:
                    price.append("".join(i))
                price1 = price[0]
                print(price1)
                print(type(price1))
                sum = int(price1) * int(signsum)
                feedback = "一共要支付" + str(sum)
                st.write(feedback)
                break
        else:
            st.write("登入失敗")          

        


cursor.close()
# connection.commit()
connection.close()
  