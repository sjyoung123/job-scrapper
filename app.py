from flask import Flask, render_template

app = Flask("scrapper!!")


@app.route("/")
def home():
    return render_template("home.html")
