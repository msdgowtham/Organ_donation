from flask import Flask, request, render_template, url_for, session, redirect, g
import os
from datetime import timedelta
from login import login
from register import register
import pymysql
mysql_server="localhost"

app = Flask(__name__)

@app.route("/index")
@app.route('/')
@app.route('/<login>')
def index(login=None):
    if g.mail:
        return render_template("index.html",login=True)
    return render_template("index.html",login=login)

@app.route('/awareness')
def awareness():
    return render_template("awareness.html")

@app.route('/aboutonelife')
def aboutonelife():
    return render_template("aboutonelife.html")

@app.route('/event')
def event():
    return render_template("event.html")

@app.route('/event-details')
def event_details():
    return render_template("event-details.html")

@app.route('/about-us')
def about_us():
    return render_template("about-us.html")

@app.route('/guide')
def guide():
    if g.mail:
        return render_template("guide.html",login=True,first=True)
    else:
        return render_template("index.html",guidelogin=False)

@app.route('/searchHosp', methods=['GET', 'POST'])
def searchHosp():
    if g.mail:
        result = request.form
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "organdonation")
        cursor = db.cursor()
        sql = "select * from hospitals where Address like %s"
        value = ("%"+result["city"]+"%")
        try:
            # Execute the SQL command
            cursor.execute(sql, value)
            # Fetch all the rows in a list of lists.
            hospitals = cursor.fetchall()
            # print(user)
        except:
            print("Error: unable to fetch data")
        db.close()

        #print(hospitals)
        return render_template("guide.html",hospitals=hospitals,login=True,first=False)
    else:
        return redirect(url_for("index"))


@app.route('/searchDonor', methods=['GET', 'POST'])
def searchDonor():
    result = request.form
    db = pymysql.connect(mysql_server, "root", "lokesh1999", "organdonation")
    cursor = db.cursor()
    sql = "select * from users where City like %s and blood=%s and blood_donation=1"
    value = ("%"+result["city"]+"%",result["BloodGroup"])
    try:
        # Execute the SQL command
        cursor.execute(sql, value)
        # Fetch all the rows in a list of lists.
        donors = cursor.fetchall()
        # print(user)
    except:
        print("Error: unable to fetch data")
        return render_template("donor.html",donors=None,first=False)
    db.close()

    #print(hospitals)
    return render_template("donor.html",donors=donors,first=False)


@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/donor')
def donor():
    if g.mail:
        return render_template("donor.html",first=True,login=True)
    else:
        return redirect(url_for("index"))

@app.route('/myacc')
def myacc():
    if g.mail:
        user = session.get("mail")
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "organdonation")
        cursor = db.cursor()
        sql = "select * from users where email=%s"
        value = (session.get("mail"))
        try:
            # Execute the SQL command
            cursor.execute(sql, value)
            # Fetch all the rows in a list of lists.
            user = cursor.fetchall()
            # print(user)
        except:
            print("Error: unable to fetch data")
        db.close()

        return render_template("myacc.html",login=True, user=user)
    return render_template("myacc.html",login=False)

@app.route('/loginForm', methods=['GET', 'POST'])
def loginForm():
    result = request.form
    x = login()
    y = x.validateLogin(**result)
    if request.method == 'POST':
        session.pop('mail', None)
        if y == True:
            session['mail'] = result['email']
            print("Session mail obj: ",session['mail'])
            return render_template("index.html", login=True)
    return render_template("index.html", login=False)


@app.route('/HosploginForm', methods=['GET', 'POST'])
def HosploginForm():
    result = request.form
    x = login()
    y = x.validatehospLogin(**result)
    if request.method == 'POST':
        session.pop('mail', None)
        if y == True:
            session['mail'] = result['email1']
            #print("Session mail obj: ",session['mail'])
            return redirect(url_for("home"))
    return render_template("myacc.html", login=False)

@app.route('/home/<login>')
@app.route('/home')
def home(login=None):
    if g.mail:
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "organdonation")
        cursor = db.cursor()
        sql = "select * from users"
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            users = cursor.fetchall()
            # print(user)
        except:
            print("Error: unable to fetch data")
        db.close()
        return render_template("home.html",login=True,users=users)
    else:
        return render_template("index.html")

@app.route('/updateForm', methods=['GET', 'POST'])
def updateForm():
    if g.mail:
        #print("In Update form")
        result = request.form
        organ = result.getlist('organ')
        obj = register()
        ans = obj.updatefunc(*organ, **result)
        return redirect(url_for("myacc"))


@app.route('/registerForm', methods=['GET', 'POST'])
def registerForm():
    result = request.form
    organ = result.getlist('organ')
    ob = register()#creating object for register class
    ans = ob.registerfunc(*organ, **result)
    if ans == True:
        status = True
        return render_template("index.html", status=status)
    else:
        return render_template("index.html", status=False)






@app.before_request
def before_request():
    g.mail = None
    if 'mail' in session:
        g.mail = session['mail']



@app.route('/getsession')
def getsession():
    if 'mail' in session:
        return session['mail']
    return 'Not logged in!'


@app.route('/dropsession')
def dropsession():
    session.pop('mail', None)
    return render_template("index.html")


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.permanent_session_lifetime = timedelta(minutes=10)
    app.run(debug=True)