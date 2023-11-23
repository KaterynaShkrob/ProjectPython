from Job import Job


def createJob(jobStructure):
    title = jobStructure.find("h3", {"class": "base-search-card__title"}).text.strip()
    city = jobStructure.find("span", {"class": "job-search-card__location"}).text.strip()
    time = jobStructure.time["datetime"]
    link = jobStructure.a["href"]
    job_object = Job(title, city, time, link)
    return job_object
