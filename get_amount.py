import mysql.connector
import time
import itchat
from itchat.content import *
def main_():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="autof460",
    database="pachong"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM jilu")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x[0])
    return x[0]
@itchat.msg_register(TEXT)
def text_reply(msg):
    if msg.text=='fee':
        a=main_()     
        print(str(a))
        localtime = time.asctime( time.localtime(time.time()) )
        send(str(a))
        
        return str(a)+'--'+str(localtime)
    else:
        pass

main_()
a=main_()
#print(time.time())
#print(str(a))
itchat.auto_login(enableCmdQR=2,hotReload=True)

itchat.run()

