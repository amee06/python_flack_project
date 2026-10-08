from flask import Blueprint,session,render_template,request,redirect,url_for
from database import db,cursor

game_bp = Blueprint("result",__name__)

@game_bp.route("/result",methods = ["POST"])
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
