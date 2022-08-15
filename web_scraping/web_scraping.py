from tkinter import N
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
date = []
# job_requierments =[]
page_num = 0

while True:
    result = requests.get(
        f"https://wuzzuf.net/search/jobs/?a=hpb&q=flutter&start={page_num}")

    src = result.content
    # print(src)
    soup = BeautifulSoup(src, "lxml")

    page_limit = int(soup.find("strong").text)
    if page_num > page_limit//15:
        break

    job_titles = soup.find_all("h2", {"class": "css-m604qf"})
    # print(job_title)
    company_names = soup.find_all("a", {"class": "css-17s97q8"})
    # print(company_name)
    locations = soup.find_all("span", {"class": "css-5wys0k"})
    # print(locations)
    job_skills = soup.find_all("div", {"class": "css-y4udm8"})
    # print(job_skills)

    new_posted = soup.find_all("div", {"class": "css-4c4ojb"})
    old_posted = soup.find_all("div", {"class": "css-do6t5g"})
    post_date = [*new_posted, *old_posted]

    for i in range(len(job_titles)):
        titles.append(job_titles[i].text)
        links.append(job_titles[i].find("a").attrs['href'])
        companys.append(company_names[i].text)
        job_locations.append(locations[i].text)
        skills.append(job_skills[i].text)
        date.append(post_date[i].text)
    page_num += 1

# for link in links:
#     result = requests.get("https://wuzzuf.net"+link)
#     scr = result.content
#     soup = BeautifulSoup(scr, "lxml")
#     requierment = soup.find("div",{"class":"css-1t5f0fr"}).ul
#     response_text =""
#     for li in requierment.find_all("li"):
#         response_text+=li.text +"| "
#         response_text = response_text[:-2]
#     job_requierments.append(response_text)


flie_list = [titles, companys, date, job_locations, skills, links]
exported = zip_longest(*flie_list)

with open("/Users/hanysameh/Development/py projects/web_scraping/flutter_jobs.csv", "w") as myfile:
    writer = csv.writer(myfile)
    writer.writerow(["job title", "company name", "post date", "location",
                    "skills", "links"])
    writer.writerows(exported)
