import csv


def save_to_file(jobs, word):
    # 인코딩 에러 해결: encodeing="utf-8"
    file = open(f"{word}.csv", mode="w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return  # csv 파일 만드는 함수
