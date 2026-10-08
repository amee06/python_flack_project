from flask import Blueprint,render_template,session,request,redirect,url_for
from database import db,cursor

user_bp = Blueprint("res",__name__) 

@user_bp.route("/registration", methods=["GET","POST"])
def reg():
    
    print("registration route hit")

    if request.method == "GET":
        return render_template("registration.html")
        
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    sql = """
    insert into users(name,email,password)
    values (%s,%s,%s)
    """

 

    values = (name,email,password)
    print(name)
    print(email)
    print(password)

    print("Before execute")
    cursor.execute(sql,values)
    print("After commit")

    db.commit()


    # return "Done"
    return render_template("login.html") 