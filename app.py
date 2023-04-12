from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template("base.html", title=title)


@app.route('/training/<profession>')
def training(profession):
    return render_template("training.html", profession=profession)


if __name__ == '__main__':
    app.run()
