import requests
from bs4 import BeautifulSoup
import pandas as pd

string = '10'
url = 'https://www.monster.com/jobs/search/?q=Software-Developer&stpage=1&page={}'.format(string)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

job_title = []
job_company = []
job_location = []
job_time = []

for job in soup.find_all('section', class_='card-content'):
    job_titles = job.find('h2', class_='title')
    job_companies = job.find('div', class_='company')
    job_locations = job.find('div', class_='location')
    job_times = job.find('time')
    if(None in (job_titles, job_companies, job_locations)):
        continue
    else:
        job_title.append(job_titles.text.strip())
        job_company.append(job_companies.text.strip())
        job_location.append(job_locations.text.strip())
        job_time.append(job_times.text.strip())


jobs = pd.DataFrame({
    'Title': job_title,
    'Company': job_company,
    'Location': job_location,
    'Time' : job_time
})

#To save the dataframe in csv
file_to_save = 'jobs.csv'
jobs.to_csv(file_to_save)
print(jobs)
