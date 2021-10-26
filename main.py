# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the HomePage!"

@app.route("/<my_name>")
def greetings(my_name):
    return "Welcome " + my_name + " to our website!"

@app.route('/square/<int:number>')
def show_square(number):
    return "Square of " + str(number) + " is: " + str(number * number)

@app.route("/educative")
def learn():
    return "Welcome to the Learning Page!"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000)

