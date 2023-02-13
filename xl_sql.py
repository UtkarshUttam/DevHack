import mysql.connector as mc
import pandas as pd

def scrap_inserter():
    mydb=mc.connect(host='localhost',user='root',password='root',database='devhack')
    cursor=mydb.cursor()
    cursor.execute('truncate hackathons_data2;')
    file = pd.read_excel('Hackathons_data.xlsx')
    h1=file
    for i,j in h1.iterrows():
        cursor.execute('INSERT INTO  hackathons_data2 VALUES ("{0}","{1}","{2}","{3}","{4}","{5}");'.format(j[0], j[1], j[2], j[3], j[4],j[5]))
        mydb.commit()
    mydb.close()

def scrap_inserter2():
    mydb=mc.connect(host='localhost',user='root',password='root',database='devhack')
    cursor=mydb.cursor()
    cursor.execute('truncate internship_data;')
    file1 = pd.read_excel('Internships_data.xlsx')
    h2=file1
    for i,j in h2.iterrows():
        cursor.execute('INSERT INTO  Internship_data VALUES ("{0}","{1}","{2}","{3}","{4}","{5}");'.format(j[0], j[1], j[2], j[3], j[4],j[5]))
        mydb.commit()
    mydb.close()
    
# def img():
#     img_store=[]
#     mydb=mc.connect(host='localhost',user='root',password='root',database='devhack')
#     mycursor=mydb.cursor()
#     mycursor.execute("select count(hack_id) from hackathons_data")
#     y=mycursor.fetchone()
#     for i in range(1,y[0]):
#         mycursor.execute("select * from hackathons_data where hack_id={0}".format(str(i)))
#         x=mycursor.fetchone()
#         img_store.append(x[14])
#     return img_store
