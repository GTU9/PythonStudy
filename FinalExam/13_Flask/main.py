from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return '<h1>안녕</h1>'

@app.route("/<name>/<int:old>")
def name(name,old):
    return f"{name}은 {old}살 입니다."



if __name__ == "__main__":
    app.run(debug=True)
