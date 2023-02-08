import mysql.connector as mc
import pandas as pd

def scrap_inserter():
    mydb=mc.connect(host='localhost',user='root',password='root',database='devhack')
    cursor=mydb.cursor()
    cursor.execute('truncate hackathons_data1;')
    file = pd.read_excel('hacksdata.xlsx')
    h1=file
    for i,j in h1.iterrows():
        cursor.execute('INSERT INTO  hackathons_data1 VALUES ("{0}","{1}","{2}","{3}","{4}","{5}");'.format(j[0], j[1], j[2], j[3], j[4],j[5]))
        mydb.commit()
    mydb.close()