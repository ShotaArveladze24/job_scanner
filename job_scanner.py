import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent': 'Mozilla/5.0'}

def scan_jobs(params):
    # Example scanning on Indeed (you can expand this function for other websites)
    url = f"https://www.indeed.com/jobs?q={'+'.join(params['skills'])}&l={params['city']}&jt={params['job_type']}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = []
    for job in soup.select('.result'):
        title = job.select_one('h2').text.strip()
        company = job.select_one('.companyName').text.strip() if job.select_one('.companyName') else 'N/A'
        location = job.select_one('.companyLocation').text.strip() if job.select_one('.companyLocation') else 'N/A'
        link = 'https://indeed.com' + job.select_one('a')['href']
        jobs.append({'title': title, 'company': company, 'location': location, 'link': link})
    
    return jobs

def save_jobs(jobs, filename='jobs.json'):
    with open(filename, 'w') as f:
        json.dump(jobs, f)

def load_jobs(filename='jobs.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []