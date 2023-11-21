import requests
from bs4 import BeautifulSoup
from Job import Job
from requests.exceptions import ConnectionError


print("Search jobs")
search = input()
print('Searching:' + search)
url = 'https://www.linkedin.com/jobs/search?keywords=' + search + '&location=Germany&geoId=101282230&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'

try:
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
    with open('results/' + search + '.csv', 'w') as file:
        file.write("Title;City;Time;Link\n")
        for job in jobs:
            file.write(job.title + ";" + job.city + ";" + job.time + ";" + job.link + "\n")
except ConnectionError as e:
    print("Wrong url")


