# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template

app = Flask(__name__)

"""1. Add a View Function for the Home page."""
@app.route("/")
def home():
    return render_template("home.html")
"""2. Add a View Function for the About page."""
@app.route("/about")
def about():
    return """We are a non-profit organization working as an animal rescue center. 
        We aim to help you connect with the purrfect furbaby for you! 
        The animals you find at our website are rescue animals which have been rehabilitated. 
        Our mission is to promote the ideology of "Adopt, don't Shop"! """

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

