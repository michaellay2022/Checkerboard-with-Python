from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def display8x8():
    return render_template("index.html", x=8, y=8)


@app.route('/<int:num>')
def display8x4(num):
    return render_template("index.html", y=num, x=8)


@app.route('/<int:num1>/<int:num2>')
def parameters(num1, num2):
    return render_template("index.html", y=num1, x=num2)


@app.route('/<int:num1>/<int:num2>/<string:color1>/<string:color2>')
def parameters2(num1, num2, color1, color2):
    return render_template("index.html", y=num1, x=num2, color1=color1, color2=color2)


if __name__ == "__main__":
    app.run(debug=True)
