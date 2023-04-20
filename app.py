from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs


app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template("base.html", title=title)


@app.route('/training/<profession>')
def training(profession):
    return render_template("training.html", profession=profession)


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    professions_list = ["инженер-исследователь", "пилот", "строитель", "экзобиолог",
                        "врач", "инженер по терраформированию", "климатолог",
                        "специалист по радиационной защите", "астрогеолог", "гляциолог",
                        "инженер жизнеобеспечения", "метеоролог", "оператор марсохода",
                        "киберинженер", "штурман", "пилот дронов"]

    return render_template("professions.html", list_type=list_type, professions_list=professions_list)


@app.route('/answer')
def login():
    values = {"title": "Анкета",
              "surname": "Wanty",
              "name": "Mark",
              "education": "выше среднего",
              "profession": "штурман марсохода",
              "sex": "male",
              "motivation": "Всегда мечтал застрять на Марсе!",
              "ready": "True"}
    return render_template("answer.html", **values)


@app.route('/')
def works_log():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).join(User, Jobs.team_leader == User.id).all()
    return render_template("works_log.html", jobs=jobs)


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run()
