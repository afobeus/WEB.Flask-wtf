from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def hello_world(title):
    return render_template("base.html", title=title)


if __name__ == '__main__':
    app.run()
