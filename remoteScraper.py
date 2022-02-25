from bs4 import BeautifulSoup
import requests

# 직업,회사,링크(https://remoteok.com/remote-jobs/:id)


def extract_job(result):
    job_id = result["data-id"]
    company = result["data-company"]
    title = result.find("td", class_="company").find(
        "a").find("h2").get_text(strip=True)
    link = f"https://remoteok.com/remote-jobs/{job_id}"
    return {
        "title": title,
        "company": company,
        "link": link
    }


def extract_jobs(url):
    jobs = []
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
              }  # 503에러 해결 => 브라우저에 봇이 아닌 사람이란 걸 알려주는 헤더 코드
    result = requests.get(url, headers=header)
    soup = BeautifulSoup(result.text, "html.parser")
    job_list = soup.find_all("tr", class_="job")
    for job_result in job_list:
        job = extract_job(job_result)
        jobs.append(job)
    return jobs


def get_remote_jobs(word):
    url = f"https://remoteok.io/remote-dev+{word}-jobs"
    jobs = extract_jobs(url)
    return jobs
