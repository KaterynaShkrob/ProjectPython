import requests
from bs4 import BeautifulSoup

url = 'https://www.linkedin.com/jobs/search?keywords=Fahrer&location=Germany&geoId=101282230&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
jobs = soup.find_all("div", {"class": "base-search-card__info"})

for job in jobs:
    title = job.find("h3", {"class": "base-search-card__title"})
    city = job.find("span", {"class": "job-search-card__location"})
    time = job.time["datetime"]
    print("Arbeit: " + title.text.strip())
    print("Stadt: " + city.text.strip())
    print("Zeit: " + time)
