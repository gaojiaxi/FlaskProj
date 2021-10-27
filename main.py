# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template

app = Flask(__name__)


"""Information regarding the Pets in the System."""
pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."},
        ]

"""1. Add a View Function for the Home page."""
@app.route("/")
def home():
    return render_template("home.html", pets = pets)
"""2. Add a View Function for the About page."""
@app.route("/about")
def about():

    return render_template("about.html")

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

