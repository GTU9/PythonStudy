from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>hello</h1>"

@app.route('/user/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}!, you are {number + 3} years old!"

if __name__ == "__main__":
    app.run(debug=True)