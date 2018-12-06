import mysql.connector
import time
import itchat
from itchat.content import *
def main_():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="xxx",
    database="xxx"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM xxx")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x[0])
    return x[0]
#Below part is register the msg.
"""Which means that. 
When I get a msg 'fee'.
I will reply the 'fee' I searched in my Sql.
"""
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
itchat.auto_login(enableCmdQR=2,hotReload=True)
itchat.run()

