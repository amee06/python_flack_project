from flask import Flask,render_template,request,redirect,url_for,session
from database import db,cursor


import mysql.connector
import os
import random

app = Flask(__name__)

app.secret_key = "my_sec"

@app.route("/")
def home():
    return "Hello Flask!"

@app.route("/home")
def r2():
    return "Hello world!"

@app.route("/registration", methods=["GET","POST"])
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
    
    
@app.route("/login", methods=["GET","POST"])
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
        return render_template("dashboard.html")
    else:
        return "Invalid information"

#Dashboard Page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/start",methods=["POST"])
def start():

    duration = request.form["duration"]
    print(duration)

    if duration == "1":
        folder = "paragraphs/1min"

    elif duration == "2":
        folder = "paragraphs/2min"

    elif duration == "3":
        folder = "paragraphs/5min"

    files = os.listdir(folder)
    random_file = random.choice(files)

    with open(os.path.join(folder, random_file), "r", encoding="utf-8") as file:
        paragraph = file.read()

    return render_template(
        "text.html",
        paragraph = paragraph,
        duration = duration
    )


@app.route("/result",methods = ["POST"])
def result():
    paragraph = request.form["paragraph"]

    user_text = request.form.get('typed_text')
    print(user_text)

    duration = int(request.form["duration"])

    
    original_words = paragraph.split()
    typed_words = user_text.split()

    correct = 0
    wrong = 0

    length = min(len(original_words), len(typed_words))

    for i in range(length):

        if original_words[i] == typed_words[i]:
                correct += 1
        else:
                wrong += 1

    wrong += abs(len(original_words) - len(typed_words))

    total_words = len(original_words)


    user_id = session["user_id"]
    accuracy = (correct/total_words)*100
    wpm = correct

    sql = """
        insert into result (user_id, total_words, correct_words, wrong_words, wpm, accuracy) 
        values(%s,%s,%s,%s,%s,%s)
        """

    values = (
            user_id,
            total_words,
            correct,
            wrong,
            wpm,
            accuracy
        )

    cursor.execute(sql,values)
    db.commit()

    

    return render_template(
        "result.html",
         correct = correct,
         wrong = wrong,
         accuracy = accuracy,
         wpm = wpm
         )




if __name__ == "__main__":
    app.run(debug=True)
