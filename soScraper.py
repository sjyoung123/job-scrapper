from bs4 import BeautifulSoup
import requests

# 직업,회사,링크(https://stackoverflow.com/jobs/:id)


def get_last_page(url):
    i = 1
    for i in range(1, 20):
        result = requests.get(url+f"&pg={i}")
        soup = BeautifulSoup(result.text, "html.parser")
        pages = soup.find(
            "div", class_="s-pagination").find_all("a")[-1].find("span").text
        i += 1
        if(pages != "next"):
            i -= 1
            break
        elif i == 20:
            break

    return i


def extract_job(result):
    job_id = result["data-jobid"]
    title = result.find("a", {"title": True}).text
    company = result.find("h3", class_="mb4").find_all("span")[
        0].get_text(strip=True)
    link = f"https://stackoverflow.com/jobs/{job_id}"
    return {
        "title": title,
        "company": company,
        "link": link
    }


def extract_jobs(url, last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(url+f"&pg={page}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", class_="-job")
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_so_jobs(word):
    url = f"https://stackoverflow.com/jobs?r=true&q={word}"
    last_page = get_last_page(url)
    jobs = extract_jobs(url, last_page)
    return jobs
