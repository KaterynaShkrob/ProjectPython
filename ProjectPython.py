import requests
from bs4 import BeautifulSoup
from Job import Job
url = 'https://www.linkedin.com/jobs/search?keywords=Fahrer&location=Germany&geoId=101282230&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
jobsHtml = soup.find_all("div", {"class": "base-card"})
jobs = []
for jobStructure in jobsHtml:
    title = jobStructure.find("h3", {"class": "base-search-card__title"}).text.strip()
    city = jobStructure.find("span", {"class": "job-search-card__location"}).text.strip()
    time = jobStructure.time["datetime"]
    link = jobStructure.a["href"]
    jobObject = Job(title, city, time, link)
    jobs.append(jobObject)
    # print(jobObject.title)
    # print(jobObject.city)
    # print(jobObject.time)
print(len(jobs))
with open('results/readme.txt', 'w') as file:
    for job in jobs:
         file.write(job.title + ":" + job.link + "\n")
