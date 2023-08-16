from flask import Flask, render_template, request, redirect, url_for, session, jsonify,Response
import mysql.connector
import json
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="website"
  ,charset="utf8"
)


app = Flask(__name__, 
            static_folder="Public"
        )

app.secret_key = "secret_keyy"

# @app.route("/",methods=["POST"])
@app.route("/")
def index():
    return render_template("index.html")
###
@app.route("/signup",methods=["POST"])
def signup():
    
    name = request.form["name"]
    username = request.form["username"]  
    password = request.form["passwd"] 

    mycursor = mydb.cursor()

    # 檢查資料庫中有無重複的帳號
    query = "SELECT * FROM member WHERE username = %s"
    mycursor.execute(query, (username,))
    existing_member = mycursor.fetchone()

    if existing_member:
        mycursor.close()
        # return("帳號已經被註冊")
        return redirect(url_for("error",message="帳號已經被註冊"))
        

    # 插入新會員
    query = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
    mycursor.execute(query, (name, username, password))
    mydb.commit()

    mycursor.close()
    session["state"]=True
    return redirect("/")
    
@app.route("/signin", methods=["POST"])
def signin():
    
    username=request.form["signin_username"]
    password=request.form["signin_password"]
    mycursor = mydb.cursor()
     # 查詢資料庫有無對應的帳號和密碼
    query = "SELECT * FROM member WHERE username = %s AND password = %s"
    mycursor.execute(query, (username, password))
    user = mycursor.fetchone()
    
    if user:
        session["state"] =  True
        session['user_id'] = user[0]
        session['name'] = user[1]
        session['username'] = user[2]
        
        username=user
        print("user:"+str(user))
        print ("name:"+user[1])
        print ("username:"+user[2])
        
        #  return user
        return redirect(url_for("member"))
    # if  (username == "" or password ==""):
    #     session["state"] =  False
    #     # return redirect("/error")
    #     return redirect(url_for("error", message = "請輸入帳號密碼"))
    
    # elif (username == "test" and password =="test"):
    #     session["state"] =  True
    #     return redirect("/member")
    

    else :
        session["state"] =  False
        # return redirect("/error")
        return redirect(url_for("error", message = "帳號或密碼錯誤"))
    
@app.route("/member")
def member():
    # session=session["state"]
    if "state" in session and session["state"]:
        print("username:",session['username'])
        print("user_id:",session['user_id'])
        print("name:",session['name'])
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute("SELECT member.name,message.content,member_id,message.id FROM member INNER JOIN message ON member.id=message.member_id ORDER BY message.time DESC;")
        messages = mycursor.fetchall()
        mycursor.close()
        # print(messages)
        
        return render_template("/success.html", username=session["username"], name=session["name"], messages=messages)
        
    # if (session["state"]):
    #     session=session["state"]
    #     print (session)
    #     return "ok"
    #     # session["state"]
    #     return render_template("/success.html",username=username)
    else :
        return redirect("/")

@app.route("/error")
def error():
    session["state"] =  False
    message=request.args.get("message")
    print (message)
    if (message =="請輸入帳號密碼"):
        return render_template("/fail.html",message ="請輸入帳號密碼")
    elif(message=="帳號已經被註冊"):
        return render_template("/fail.html",message ="帳號已經被註冊")
    else:
        return render_template("/fail.html",message ="帳號或密碼錯誤")
@app.route("/signout")
def signout():

    # session["state"] =  False
    #清空session
    session.clear()
    # print(session)
    return redirect("/")

@app.route("/createMessage",methods=["POST"])
def createMessage():
    content=request.form["message"]
    user_id = session["user_id"]

    mycursor = mydb.cursor()
    query = "INSERT INTO message (member_id, content) VALUES (%s, %s)"
    mycursor.execute(query, (user_id, content))
    mydb.commit()
    mycursor.close()
    # print(user_id,content)
    # return "ok"
    return redirect(url_for("member"))

@app.route("/deleteMessage",methods=["POST"])
def deleteMessage():
    message_id=request.form["message_id"]
    user_id = session["user_id"]

    mycursor = mydb.cursor()
    query = "DELETE FROM message WHERE id = %s AND member_id = %s"
    mycursor.execute(query, (message_id, user_id))
    mydb.commit()
    mycursor.close()

    return redirect(url_for("member"))

# 用帳號查詢姓名
@app.route("/api/member",methods=["GET"])
def getnumber():
    username = request.args.get('username')  #獲取查詢參數
    mycursor = mydb.cursor(dictionary=True)
    query = "SELECT id, name, username FROM member WHERE username = %s"
    mycursor.execute(query, (username,))
    member = mycursor.fetchone()
    # print (username)
    # print (member)
    if member:
        response_data = {
            "data": member
        }
        # print (response_data)
        json_response = json.dumps(response_data, ensure_ascii=False)
        return Response(json_response, content_type='application/json; charset=utf-8'), 200
        # return jsonify(response_data), 200, {'Content-Type': 'application/json; charset=utf-8'}
    else:
        response_data = {"data": None}
        json_response = json.dumps(response_data, ensure_ascii=False)
        return Response(json_response, content_type='application/json; charset=utf-8'), 200
        # return jsonify(response_data), 200, {'Content-Type': 'application/json; charset=utf-8'}


# 更新姓名
@app.route("/api/member", methods=["PATCH"])
def update_name():
    
    # print("username:",session['username'])
    # print("user_id:",session['user_id'])
    # print("name:",session['name'])
    if "user_id" in session:
        new_name = request.json.get("name")
        # print(new_name)
        if new_name:
            # print(new_name)
            mycursor = mydb.cursor()
            query = "UPDATE member SET name = %s WHERE id = %s"
            mycursor.execute(query, (new_name, session["user_id"]))
            mydb.commit()
            json_response = json.dumps({"ok": True}, ensure_ascii=False)
            # print (json_response)
            session['name']=new_name
            print("session_username:"+session['username'])
            print("session_name:"+session['name'])
            return Response(json_response, content_type='application/json; charset=utf-8'), 200
            # return jsonify({"ok": True}), 200
    json_response = json.dumps({"error": True}, ensure_ascii=False)
    return Response(json_response, content_type='application/json; charset=utf-8'), 400    
    # return jsonify({"error": True}), 400
#---------------------------------------------------------------

# @app.route("/sq/")
# def handle():
#     number=request.args.get("number")
#     print(number)
#     # return(str(number))
#     return redirect(url_for("square",number=number))
# @app.route("/square/<number>")
# def square(number):
#     number=int(number)**2
#     # return str(number)
#     return render_template("square.html",number=number)



@app.route('/square/<int:number>')
def square_number(number):
    squared = number ** 2
    return render_template('square.html', number=squared)


    
app.run(port=3000,debug = True)
