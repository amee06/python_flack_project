from flask import Blueprint,session,request,redirect,render_template,url_for
from database import db,cursor

user_bp = Blueprint("edit_pf",__name__)

@user_bp.route("/edit_profile", methods = ["GET","POST"])
def update_pf():

    user_id = session["user_id"]

    if request.method == "POST":
        print("From Data : ",request.form)
        name = request.form["name"]
    
        cursor.execute(
            "update users set name = %s where id = %s",
            (name,user_id)
        )

        db.commit()

        cursor.execute(
                "select * from users where id=%s",
                (user_id,)
            )
        
        user = cursor.fetchone()
        return render_template("profile/edit_profile.html",user=user)
   

    cursor.execute(
        "select * from users where id=%s",
        (user_id,)
    )

    user = cursor.fetchone()
    return render_template("profile/edit_profile.html",user=user)
