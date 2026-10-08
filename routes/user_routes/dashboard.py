from flask import Blueprint,render_template,session,request,redirect,url_for
import os,random
from database import db,cursor

user_bp = Blueprint("user",__name__) 


@user_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@user_bp.route("/start",methods=["POST"])
def start():

    duration = request.form["duration"]

    if duration == "1":
        folder = "paragraphs/1min"

    elif duration == "2":
        folder = "paragraphs/2min"

    elif duration == "5":
        folder = "paragraphs/5min"

    files = os.listdir(folder)
    random_file = random.choice(files)

    with open(os.path.join(folder, random_file), "r", encoding="utf-8") as file:
        paragraph = file.read()

    return render_template(
        "text.html",
        paragraph= paragraph,
        duration= duration
    )