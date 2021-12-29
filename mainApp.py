
from flask import Flask,request,render_template,redirect,url_for,session,jsonify
import sqlite3 as sql
import os
import datetime
app=Flask(__name__)

app.secret_key="sdfsdjkfhsdakfhds23432"
# get the base directory of the program
basedir = os.path.abspath(os.path.dirname(__file__))
dbdir = os.path.join(basedir,'dashboard.db')

# admin main page
@app.route("/admin")
def admin():
    msg="admin"
    return render_template('admin.html',msg=msg)
@app.route("/")
def login():
    print(print(os.path.abspath(os.path.dirname(__file__))))
    return render_template('login.html')

# home is use to register new user
@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/dashboard",methods=['POST'])
def dashboard():
    email=request.form.get('email')
    password=request.form.get('pwd')
    # get email and password from database
    with sql.connect(dbdir) as con:
        cur = con.cursor()
        cur.execute("select * from users where email=? and password=?",(email,password))
        result = cur.fetchall()
        print(result)
        if result:
            session['user_info']=email
            msg="login in successfully"
        else:
            msg="login failed"
            return render_template('login.html',msg=msg)

        signout='<a class="signout" href="/signout">Sign Out</a>'

    return render_template('dashboard.html',email=email,signout=signout)

@app.route("/registerSubmit",methods=['POST','GET'])
def registerSubmit():
    isauth=False
    authgroup='operator'
    registdate=datetime.date.today()
    if request.method == 'POST':
        print(request.form)
        try:
            firstname = request.form.get('firstname')
            lastname = request.form.get('lastname')
            email = request.form.get('email')
            password = request.form.get('pwd')
            with sql.connect(dbdir) as con:
                cur = con.cursor()
                cur.execute("insert into users(email,firstname,lastname,isauth,authgroup,registdate,password) values(?,?,?,?,?,?,?)",
                    (email, firstname, lastname, isauth, authgroup, registdate,password))
                con.commit()
                cur.execute('select * from users')
                result = cur.fetchall()
                print(result)
            msg="Register successfully"
        except:
            con.rollback()
            msg="Error in insert in Database"
        finally:
            return render_template('login.html',msg=msg)
            con.close()
    return "helloRegister"
@app.route('/signout')
def signout():
    del session['user_info']
    return redirect('/')
""" complaint case maintance table"""

@app.route('/complaint',methods=['post','get'])
def complaint():
    # render 20 rows data to template
    with sql.connect(dbdir) as con:
        cur = con.cursor()
        cur.execute("select * from complaint")
        result = cur.fetchall()
    return render_template('complaint.html',result=result)

@app.route('/complaintData',methods=['POST','GET'])
def complaintData():
     # 1 . save verified data to table compliant
    if request.method == 'POST':
        try:
            caseNo = request.form.get('caseNo')
            dateReceived = request.form.get('dateReceived')
            status = request.form.get('status')
            description = request.form.get('description')
            rootCause = request.form.get('rootCause')
            actions = request.form.get('actions')
            with sql.connect(dbdir) as con:
                cur = con.cursor()
                cur.execute("insert into complaint(caseNo, dateReceived, status, description, rootCause, actions) values(?,?,?,?,?,?)",
                            (caseNo, dateReceived, status, description, rootCause, actions))
                con.commit()
            msg = "complaint case add to database successfully"
        except:
            con.rollback()
            msg = "Error in insert in Database"
        finally:
            # 2. render 20 rows data to complaint.html
            cur.execute("select * from complaint")
            result = cur.fetchall()
            con.close()
            return render_template('complaint.html', result=result)
    if request.method == 'GET':
        # 2. render 20 rows data to complaint.html
        with sql.connect(dbdir) as con:
            cur = con.cursor()
            cur.execute("select * from complaint")
            result = cur.fetchall()
            con.close()
        return render_template('complaint.html',result=result)
@app.route("/deleteComplaint",methods=['POST'])
def deleteComplaint():
    if request.method == 'POST':
        caseNo = request.form.get("caseNo")
        print(caseNo)
        with sql.connect(dbdir) as con:
            cur = con.cursor()
            cur.execute("delete from complaint where caseNo= %s" %(caseNo))
            con.commit()
    return jsonify(status="success")
@app.route("/updateComplaint",methods=['POST'])
def updateComplaint():
    if request.method=='POST':
        caseNo=request.form.get("caseNo")
        updateStatus = request.form.get("status")
        print(caseNo,updateStatus)
        with sql.connect(dbdir) as con:
            cur = con.cursor()
            cur.execute("update complaint set status=? where caseNo=?",(updateStatus,caseNo))
            print("update complaint set status=? where caseNo=?",(updateStatus,caseNo))
            con.commit();
    return jsonify(status="success")
""" shipping kpi type"""
@app.route('/kpitype',methods=['post','get'])
def kpitype():
    # render 20 rows data to template
    with sql.connect(dbdir) as con:
        cur = con.cursor()
        cur.execute("select * from shipkpitype")
        result = cur.fetchall()
    return render_template('kpitype.html',result=result)

@app.route('/kpitypeData',methods=['post','get'])
def kpitypeData():
    if request.method == 'POST':
        try:
           kpiid = request.form.get('kpiid')
           kpiname = request.form.get('kpiname')
           year = request.form.get('kpiyear')
           target = request.form.get('kpitarget')
           description = request.form.get('description')
           with sql.connect(dbdir) as con:
                cur = con.cursor()
                cur.execute("insert into shipkpitype(kpiid,kpiname,year,target,description) values(?,?,?,?,?)",(kpiid,kpiname,year,target,description))
                con.commit()
           msg = "shipkpitype add to database successfully"
        except:
            con.rollback()
            msg = "Error in insert in Database"
        finally:
            # 2. render 20 rows data to complaint.html
            cur.execute("select * from shipkpitype")
            result = cur.fetchall()
            print(result)
            con.close()
            return render_template('kpitype.html', result=result)
    if request.method == 'GET':
        # 2. render 20 rows data to complaint.html
        with sql.connect(dbdir) as con:
            cur = con.cursor()
            cur.execute("select * from shipkpitype")
            result = cur.fetchall()
            print(result)
            con.close()
        return render_template('kpitype.html', result=result)