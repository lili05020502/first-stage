from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__, 
            static_folder="Public"
        )
app.debug = True
app.secret_key = "secret_keyy"

# @app.route("/",methods=["POST"])
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    username=request.form["username"]
    password=request.form["password"]
    if  (username == "" or password ==""):
        session["state"] =  False
        # return redirect("/error")
        return redirect(url_for("error", message = "請輸入帳號密碼"))
    
    elif (username == "test" and password =="test"):
        session["state"] =  True
        return redirect("/member")
    else :
        session["state"] =  False
        # return redirect("/error")
        return redirect(url_for("error", message = "帳號或密碼錯誤"))
    
@app.route("/member")
def member():
    if (session["state"]):
        return render_template("/success.html")
    else :
        return redirect("/")

@app.route("/error")
def error():
    session["state"] =  False
    message=request.args.get("message")
    print (message)
    if (message =="請輸入帳號密碼"):
        return render_template("/fail.html",message ="請輸入帳號密碼")
    else:
        return render_template("/fail.html",message ="帳號或密碼錯誤")
@app.route("/signout")
def signout():
    session["state"] =  False
    return redirect("/")

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


    
app.run(port=3000)
