from flask import url_for, session, Flask, render_template, request, redirect

application = Flask(__name__)
application.secret_key = "lkjds#2-1j~dsp!ldaskfj"

#임의로 id와 pw를 만들어줌 
ID = "hello"
PW = "world"

@application.route("/")
def home():
    if "userID" in session:
        return render_template("home.html", username = session.get("userID"),login=True)
    else:
        return render_template("home.html", login=False)

@application.route("/login", methods=["get"])
def login():
    global ID, PW
    _id_ = request.args.get("loginId")
    _password_ = request.args.get("loginPw")

    if ID == _id_ and _password_ == PW:
        session["userID"] = _id_
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))

@application.rout("/logout")
def logout():
    session.pop("userID")
    return redirect(url_for("home"))


application.run(host="0.0.0.0")