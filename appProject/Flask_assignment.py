from flask import Flask
import random

face = {
    "김정은": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTl2NnkzaDB4dGJ2aHI5N3Zsa2dsYWEydjhpOG81Mm9ubm11dzZyciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wyz7DsIBcvniw/giphy.gif",
    "트럼프": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExem5tb3Nkc2l6NDB2NzlrenA1OGw4cm1nc2g4bzU5cGRlZzN3N244NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7Wiozceem6Vt2eMFxO/giphy.gif",
    "바이든": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWQ0eXc4cG43NzA3cTdoMW05ZnhueDBpMzhuczR2NXFncDBramFyNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/sNGnnd0ddePJe/giphy.gif"
}

app = Flask(__name__)
random_name = random.choice(list(face.keys()))
random_image = face[random_name]

@app.route('/')
def main():
    return "<h1>사람이름 맞추기 게임</h1>" \
           "<img src ='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbW5iampkcXc1aTJkY25mcWtqZDZlMzEzdzYyMzR2emFnZjMzMDJndSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0MYC0LajbaPoEADu/giphy.gif'/>" \
           "<br>" \
           "<h3>누구일까요?</h3>" \
           f"<img src='{random_image}'/>"


@app.route('/<name>')
def result(name):
    if (name == random_name):
        return "<h1>정답입니다!</h1>" \
               "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWZpNWZiMzVxb3Q4MTNnMWhzejVhd25nODVtMzRsem5ldjZ5NGM5OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hz6L3FwCc3hI2zUAFI/giphy.gif'/>"
    else:
        return "<h1>정답이 아닙니다..</h1>" \
               "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjFjenBjNWh6cTVpeHJsZ2JjMG43Z3F6NHF6NjJ4eHNzbHhrN2JsMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/11SJ52YouBaDFS/giphy.gif'/>"


if __name__ == '__main__':
    app.run(debug=True)
