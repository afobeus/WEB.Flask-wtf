from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs
from loginform import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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
def register_success():
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/distribution')
def distribution():
    astronauts = [
        {
            "name": "Ридли",
            "surname": "Скотт"
        },
        {
            "name": "Энди",
            "surname": "Уир"
        },
        {
            "name": "Венката",
            "surname": "Капур"
        },
        {
            "name": "Тедди",
            "surname": "Сандерс"
        }
    ]
    return render_template('distribution.html', astronauts=astronauts)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    if age < 21:
        age_param = "child"
        if sex == "male":
            color_param = "lightblue"
        else:
            color_param = "lightcoral"
    else:
        age_param = "adult"
        if sex == "male":
            color_param = "blue"
        else:
            color_param = "red"
    return render_template('table.html', color=color_param, age=age_param)


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run()
