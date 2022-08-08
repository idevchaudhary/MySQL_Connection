import mysql.connector as connector  # We have to import this module in order to connect with our Database
class DBhelper:
    def __init__(self):
        self.con=connector.connect(host='localhost' 
                                ,port='3306'
                                ,user='root',#In my case the user is 'root' , if your username is different fill this one with your user name 
                                password='----'#password of the user "do fill it carefully because this is used in authentication while connecting to MySQL server"
                                ,database='-----', # fill with the name of data base in which you want to run Operations(To check Databases run'SHOW DATABASES' in your database)
                                auth_plugin='mysql_native_password')#You can check your plugin authentication setting by "select host,user,plugin,authentication_string,account_locked from mysql.user where user='username'" and make chnages accordingly//////Connector method only suppourt 'mysql_native_password'
    
    def run(self,query):
        cur=self.con.cursor()
        try:
            cur.execute(query)
            self.con.commit()
            print("Query Executed")
        except:
            print("Invalid Query Try again")

x=DBhelper()
t=1
while t>0:
    query=input('Enter Query to Run in Database:')
    x.run(query)
    t=int(input('''Enter 1 to run Query
Enter 0 to terminat program : '''))