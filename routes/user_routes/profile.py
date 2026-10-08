from flask import Blueprint,session,render_template,redirect,request,url_for
from database import cursor,db

user_bp = Blueprint("profile",__name__)

@user_bp.route('/profile')
def profile():

    user_id = session["user_id"]
    cursor.execute("select * from users where id=%s",
                   (user_id,))

    user = cursor.fetchone()
    # return render_template("profile/profile.html",user=user)

#get previous result of this user

    cursor.execute("select * from result where user_id=%s",
                   (user_id,))
    user_result = cursor.fetchall()

    return render_template("profile/profile.html",
                           user=user, user_result=user_result)
    