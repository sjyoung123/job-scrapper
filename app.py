from flask import Flask, redirect, render_template, request
from remoteScraper import get_remote_jobs

from soScraper import get_last_page, get_so_jobs
from wwrScraper import get_wwr_jobs

app = Flask("scraper!!")


@app.route("/")
def home():
    get_wwr_jobs()
    return render_template("home.html")


@app.route("/search")
def search():
    word = request.args.get("word").lower()
    if word == "":
        return redirect("/")
    get_so_jobs(word)
    get_remote_jobs(word)
    get_wwr_jobs(word)

    return render_template("search.html", word=word)
