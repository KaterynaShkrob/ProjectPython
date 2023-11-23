import requests
import sys
from bs4 import BeautifulSoup
from CreatJob import createJob
from requests.exceptions import ConnectionError

search = sys.argv[1]
print("Search jobs")
print('Searching: ' + search)

url = 'https://www.linkedin.com/jobs/search?keywords=' + search + '&location=Germany&geoId=101282230&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobsHtml = soup.find_all("div", {"class": "base-card"})
    jobs = []

    for jobStructure in jobsHtml:
        jobObject = createJob(jobStructure)
        jobs.append(jobObject)
    with open('results/' + search + '.csv', 'w') as file:
        file.write("Title;City;Time;Link\n")
        print("Created a file: " + search + ".csv")
        for job in jobs:
            file.write(job.title + ";" + job.city + ";" + job.time + ";" + job.link + "\n")
except ConnectionError as e:
    print("Wrong url")
