import random

from flask import Flask


random_number = random.randint(1, 9)
print(random_number)

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return '<h1 style="text-align: center">Hello World!</h1>'

# @app.route('/')
# def hello_world():
#     return '<h1 style="text-align: center">Hello World!</h1>' \
#            '<p>This is paragraph.</p>' \
#            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWFxYjltbWpkaXltNG0weDB6eDhjZ3R2N2RlNWlmbWl1ZmRtb2o3ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vKHKDIdvxvN7vTAEOM/giphy.gif" />'

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjNjZGY3OXduZG82NjBzYTV2ZzJyYXVmMm1vZ3dmaGxzNm8zeDcxeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UDU4oUJIHDJgQ/giphy.gif'/>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHZ1a2ljM29oN3UyeDRwb3cwZnNpMmJpNjBjdjZzbXVxZ2F3a25sMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ep7lPvQMedLcwjpdh9/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGExY2YyaXgyY3c1bWp5eDE2ancyaWdjcTk0cjNrejRrbHUwZGYweCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/rS2uLYRGkGWySNX69v/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnV2cHQ1ZjMxbm9pMmw2cGRheHFpeGNtcXAyZTdtY3h3enpwb3h0byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RpizrZcLTdlVFjZFFP/giphy.gif'/>"

@app.route('/bye')
def hello_bye():
    return 'Bye!'

@app.route('/<name>')
def hello_name(name):
    return f"Hello, {name}!"

@app.route('/user/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}!, you are {number + 3} years old!"

if __name__ == '__main__':
    app.run(debug=True)