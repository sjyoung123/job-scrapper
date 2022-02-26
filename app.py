from flask import Flask, redirect, render_template, request, send_file
from exporter import save_to_file
from remoteScraper import get_remote_jobs

from soScraper import get_so_jobs
from wwrScraper import get_wwr_jobs

app = Flask("scraper!!")


@app.route("/")
def home():
    return render_template("home.html")


db = {}


@app.route("/search")
def search():
    word = request.args.get("word").lower()
    if word == "":
        return redirect("/")  # 입력을 하지 않았을때

    from_db = db.get(word)
    if from_db:
        jobs = from_db
    else:
        jobs = get_so_jobs(word) + get_remote_jobs(word) + get_wwr_jobs(word)
        db[word] = jobs
    job_len = len(jobs)

    return render_template("search.html", searchingBy=word, resultNumber=job_len, jobs=jobs)


@app.route("/export")
def export():
    word = request.args.get("word")
    if not word:
        return redirect("/")
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
        return redirect("/")
    save_to_file(jobs, word)
    return send_file(f"{word}.csv")
