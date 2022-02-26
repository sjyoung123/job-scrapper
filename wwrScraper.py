from bs4 import BeautifulSoup
import requests
# 직업,회사,링크(https://weworkremotely.com/remote-jobs/:id)


def extract_job(soup):
    job_id = soup.select_one("li > a")["href"]
    title = soup.find("span", class_="title").text
    company = soup.find("span", class_="company").text
    link = f"https://weworkremotely.com/remote-jobs{job_id}"

    return {
        "title": title,
        "company": company,
        "link": link
    }


def extract_jobs(url):
    jobs = []
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
              }  # 503에러 해결 => 브라우저에 봇이 아닌 사람이란 걸 알려주는 헤더 코드
    result = requests.get(url, headers=header).text

    soup = BeautifulSoup(result, "html.parser")
    section_list = soup.find_all("section", class_="jobs")
    for section in section_list:
        job_list = section.find_all("li")
        del job_list[-1]
        for job_result in job_list:
            job = extract_job(job_result)
            jobs.append(job)
    return jobs


def get_wwr_jobs(word):
    url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    jobs = extract_jobs(url)
    return jobs
