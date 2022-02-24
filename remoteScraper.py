from bs4 import BeautifulSoup
import requests

# 직업,회사,링크(https://remoteok.com/remote-jobs/:id)


def extract_job(result):
    job_id = result["data-id"]
    company = result["data-company"]
    title = result.find("td", class_="company").find("a").find("h2").text
    link = f"https://remoteok.com/remote-jobs/{job_id}"
    return {
        "title": title,
        "company": company,
        "link": link
    }


def extract_jobs(url):
    jobs = []
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    job_list = soup.find_all("tr", class_="job")
    for job_result in job_list:
        job = extract_job(job_result)
        jobs.append(job)
    return jobs


def get_remote_jobs():
    url = "https://remoteok.io/remote-dev+python-jobs"
    jobs = extract_jobs(url)
    return jobs
