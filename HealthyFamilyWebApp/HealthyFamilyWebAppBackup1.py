#from flask import Flask, render_template, redirect, request, json
from flask import *
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash,check_password_hash

mysql = MySQL()
healthyfamily = Flask(__name__)
healthyfamily.secret_key= '&&&777@seven.!@ASDASD!(H&*@H*&FGH@12312$F*&R$&F21312!@&*)^+_ASBFSJBXZSNabdasidasdb122989a'

# MySQL configurations
healthyfamily.config['MYSQL_DATABASE_USER'] = 'royce'
healthyfamily.config['MYSQL_DATABASE_PASSWORD'] = '261523'
healthyfamily.config['MYSQL_DATABASE_DB'] = 'healthy_family'
healthyfamily.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(healthyfamily)

@healthyfamily.route("/")
def index():
    return render_template('index.html')

@healthyfamily.route("/ShowSignin")
def signin():
    return render_template('signin.html')

@healthyfamily.route("/validateLogin", methods=['GET','POST'])
def validate():
    if request.method == 'POST':
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']

        if _username == "royce236@gmail.com" and _password == "261523":
            return redirect("/main")
        else:
            return "<h1>Wrong username or password </h2>"

@healthyfamily.route("/ShowSignup")
def signup():
    return render_template('signup.html')

# @healthyfamily.route("/createAccount", methods=['POST','GET'])
# def createAccount():
#     print("function launched!")
#
#     if request.method == 'POST':
#         print("Request Method is: {}".format(request.method))
#         try:
#             _name = request.form['inputName']
#             _username = request.form['inputUserName']
#             _mobileno = request.form['inputMobileno']
#             _telno = request.form['inputTelno']
#             _email = request.form['inputEmail']
#             _address = request.form['inputAddress']
#             _password = request.form['inputPassword']
#             print("All forms retrieved")
#             # validate the recieved values (Output should be true since all fields have values)
#             if _name and _username and _mobileno and _telno and _email and _address and _password:
#
#                 # Call MySQL
#                 #     conn = mysql.connect()
#                 #     cursor = mysql.get_db().cursor()
#                 conn = mysql.connect()
#                 cursor = conn.cursor()
#                 _hashed_password = generate_password_hash(_password)
#                 cursor.callproc('usp_createUser',
#                                 (_name, _username, _mobileno, _telno, _email, _address, _hashed_password))
#                 data = cursor.fetchall()
#
#                 if len(data) is 0:
#                     conn.commit()
#                     return redirect('/')
#                     # return json.dumps({'message': 'User created sucessfully !'})
#                 else:
#                     print("Something Wrong!")
#                     return json.dumps({'error': str(data[0])})
#             else:
#                 return json.dumps({'message': '<span>Enter the Required Fields</span>'})
#         except Exception as e:
#             print("Some error catched")
#             return json.dumps({'error': str(e)})
#         finally:
#             cursor.close()
#             conn.close()

@healthyfamily.route("/createAccount", methods=['POST','GET'])
def createAccount():
    if request.method == 'POST':
        _name = request.form['inputName']
        _username = request.form['InputUserName']
        _mobileno = request.form['inputMobileno']
        _telno = request.form['inputTelno']
        _email = request.form['inputEmail']
        _address=request.form['inputAddress']
        _password=request.form['inputPassword']
        return "Data Recieved: {} {} {} {} {} {} {}".format(_name,_username,_mobileno,_telno,_email,_address,_password)

@healthyfamily.route("/main")
def main():
    return render_template('main.html')

if __name__ == '__main__':
    healthyfamily.run(debug=True)

healthyfamily.run(debug=True)
