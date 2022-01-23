import requests
from bs4 import BeautifulSoup


def get_last_page(url):  # 2
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    # [0:-1]은 처음에서 시작에서 가장 마지막까지의 리스트를 가져오는 것이고, [-1]은 가장 마지막 리스트만 가져오는 것이다
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


# find_all을 사용할 때 recursive=False로 사용을 하면, 찾고자하는 모든 태그를 찾는 것이 아닌 가장 상위 레벨의 태그만 찾는다
def extract_job(html):  # 4
    title = html.find("h2").find("a")["title"]
    company_row = html.find("h3").find_all("span")
    company = company_row[0].get_text(strip=True)
    location = company_row[1].get_text(strip=True)
    job_id = html["data-jobid"]
    return {"title": title, "company": company, "location": location, "apply_link": f"https://stackoverflow.com/jobs?id={job_id}&pg=3&q=python"}


def extract_jobs(last_page, url):  # 3
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Stack Over Flow page {page}")
        result = requests.get(f"{url}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs(word):  # 1
    url = f"https://stackoverflow.com/jobs?q={word}"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs
