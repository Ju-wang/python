import requests
from bs4 import BeautifulSoup

LIMIT = 10

URL = "https://kr.indeed.com/jobs?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&l=%EC%84%9C%EC%9A%B8"


def extract_indeed_pages():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_job(result):
    title = result.find("h2", {"class": "jobTitle"})
    job_title = title.find("span").string
    if job_title == "new":
        job_title = title.find_all("span")[1].string
    company = result.find("span", {"class": "companyName"}).string
    location = result.find("div", {"class": "companyLocation"}).string
    job_id = result["data-jk"]
    return {"title": job_title, "company": company, "location": location, "link": f"https://kr.indeed.com/jobs?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&l=%EC%84%9C%EC%9A%B8&vjk={job_id}"}


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping indeed page {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("a", {"class": "fs-unmask"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_indeed_page = extract_indeed_pages()
    jobs = extract_indeed_jobs(last_indeed_page)
    return jobs
