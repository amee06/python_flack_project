from flask import Blueprint,render_template,session,request,redirect,url_for
from database import db,cursor

user_bp = Blueprint("login",__name__) 

@user_bp.route("/login", methods=["GET","POST"])
def check_login():

    print("login route hit")

    if request.method == "GET":
        return render_template("login.html")

    email = request.form["email"]
    password = request.form["password"]

    #database check
    sql = "select * from users where email = %s and password = %s"
    values = (email,password)
    cursor.execute(sql,values)
    user = cursor.fetchone()

    if user:
        session["user_id"] = user[0]   # Save logged-in user's ID
        return redirect(url_for("user.dashboard"))
    else:
        return "Invalid information"
