import pymysql
mysql_server="localhost"

class login():
    def validateLogin(self,**data):
        self.mailId = data['email']
        self.password = data['pwd']
        #print("In Login function")
        #print(self.mailId,self.password)
        # Open database connection
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "organdonation")
        # prepare a cursor object using cursor() method
        db.autocommit(False)
        cursor = db.cursor()
        # execute SQL query using execute() method.
        #print("Connected")
        #sql = "SELECT cast(aes_decrypt(%s,'passkey') as char(50)) as password FROM users where mailId=%s "
        val= (self.password,self.mailId)
        # cursor.execute("SELECT VERSION()")
        # Fetch a single row using fetchone() method.
        try:

            # Execute the SQL command
            cursor.execute("SELECT cast(aes_decrypt(pwd,'passkey') as char(40)) from users where email=%s",(self.mailId))

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            #print(results)
            password=results[0][0]
        except Exception as e:
            print(e)
            print("Error: unable to fetch data")
            db.commit()
            db.close()
            return False
        if password == self.password:
            #print("Logged in")
            db.commit()
            db.close()
            return True
        else:
            db.commit()
            db.close()
            return False

        # disconnect from server

    def validatehospLogin(self,**data):
        self.mailId = data['email1']
        self.password = data['pwd']
        print("In Login function")
        print(self.mailId,self.password)
        # Open database connection
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "organdonation")
        # prepare a cursor object using cursor() method
        db.autocommit(False)
        cursor = db.cursor()
        # execute SQL query using execute() method.
        #print("Connected")
        #sql = "SELECT cast(aes_decrypt(%s,'passkey') as char(50)) as password FROM hospitals where mailId=%s "
        val= (self.password,self.mailId)
        # cursor.execute("SELECT VERSION()")
        # Fetch a single row using fetchone() method.
        try:

            # Execute the SQL command
            cursor.execute("SELECT cast(aes_decrypt(pwd,'passkey') as char(40)) from hospitals where email=%s",(self.mailId))

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            #print(results)
            password=results[0][0]
        except Exception as e:
            print(e)
            print("Error: unable to fetch data")
            db.commit()
            db.close()
            return False
        if password == self.password:
            #print("Logged in")
            db.commit()
            db.close()
            return True
        else:
            db.commit()
            db.close()
            return False
