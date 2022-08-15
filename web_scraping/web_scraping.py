from unittest import result
from urllib import request
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

titles = []
companys = []
job_locations = []
skills = []
links = []

result = requests.get("https://wuzzuf.net/search/jobs/?q=flutter&a=hpb")

src = result.content
# print(src)
soup = BeautifulSoup(src, "lxml")

job_titles = soup.find_all("h2", {"class": "css-m604qf"})
# print(job_title)
company_names = soup.find_all("a", {"class": "css-17s97q8"})
# print(company_name)
locations = soup.find_all("span", {"class": "css-5wys0k"})
# print(locations)
job_skills = soup.find_all("div", {"class": "css-y4udm8"})
# print(job_skills)

for i in range(len(job_titles)):
    titles.append(job_titles[i].text)
    links.append(job_titles[i].find("a").attrs['href'])
    companys.append(company_names[i].text)
    job_locations.append(locations[i].text)
    skills.append(job_skills[i].text)

flie_list = [titles, companys, job_locations, skills,links]
exported = zip_longest(*flie_list)

with open("/Users/hanysameh/Development/py projects/web_scraping/flutter_jobs.csv", "w") as myfile:
    writer = csv.writer(myfile)
    writer.writerow(["job title", "company name", "location", "skills","links"])
    writer.writerows(exported)

