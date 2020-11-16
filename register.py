import pymysql
mysql_server="localhost"

class register():

    def registerfunc(self,*organ,**result):
        self.name=result['name']
        self.mailId= result['email1']
        self.password=result['pwd1']
        self.blood=result['BloodGroup']
        self.age=result['age']
        self.genre=organ
        self.Heart=0
        self.Liver=0
        self.Kidney=0
        self.Eyes=0
        self.Lungs=0
        self.blood_donation=result['blood']
        self.city=result['city']
        self.phone=result['phone']

        #print("organ: ",organ)
        for item in organ:
            if item=="Heart":
                self.Heart=1
            if item=="Liver":
                self.Liver=1
            if item=="Kidney":
                self.Kidney=1
            if item=="Eyes":
                self.Eyes=1
            if item=="Lungs":
                self.Lungs=1

        db = pymysql.connect(mysql_server, "root", "lokesh1999", "organdonation")
        # prepare a cursor object using cursor() method
        db.autocommit(False)
        cursor = db.cursor()
        # execute SQL query using execute() method.
        #print(result)
        sql = "insert into users values(Null,%s,%s,%s,aes_encrypt(%s,'passkey'),%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val =(self.mailId,self.name,self.age,self.password,self.blood,int(self.Heart),int(self.Liver),int(self.Kidney),int(self.Eyes),int(self.Lungs),
              bool(self.blood_donation),self.city,self.phone)
        try:
            #print("in try")
            # Execute the SQL command
            cursor.execute(sql,val)
            #print("command executed")
            # Fetch all the rows in a list of lists.
        except Exception as e:
            print(e)
            print("Error: unable to insert data")
            db.close()
            return False
        db.commit()
        db.close()
        return True


    def updatefunc(self,*organ,**result):
        self.email=result['email']
        self.Heart=0
        self.Liver=0
        self.Kidney=0
        self.Eyes=0
        self.Lungs=0
        self.phone=result['phone']
        self.blood_donation=result['blood']
        if self.blood_donation=="Yes":
            self.blood_donation1=1
        else:
            self.blood_donation1=0

        for item in organ:
            if item=="Heart":
                self.Heart=1
            if item=="Liver":
                self.Liver=1
            if item=="Kidney":
                self.Kidney=1
            if item=="Eyes":
                self.Eyes=1
            if item=="Lungs":
                self.Lungs=1

        db = pymysql.connect(mysql_server, "root", "lokesh1999", "organdonation")
        db.autocommit(False)
        cursor = db.cursor()
        sql = "update users set Heart=%s,Liver=%s,Kidney=%s,Eyes=%s,Lungs=%s,blood_donation = %s,phone=%s where email=%s"
        #for item in self.genre:

        val=(int(self.Heart),int(self.Liver),int(self.Kidney),int(self.Eyes),int(self.Lungs),bool(self.blood_donation1),self.phone,self.email)
        try:
            cursor.execute(sql, val)
        except Exception as e:
            print("Error: unable to insert data")
            print(e)
            db.close()
            save = False
            return save
        print("Updated")
        db.commit()
        db.close()
        return True
