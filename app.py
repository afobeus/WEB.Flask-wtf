from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run()
