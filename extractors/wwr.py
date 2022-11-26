from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def extract_wwr_jobs(keyword):
  options = Options()
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  browser = webdriver.Chrome(options=options)
  browser.get(f"https://kr.indeed.com/jobs?q={keyword}&limit=50")

  results = []
  soup = BeautifulSoup(browser.page_source, "html.parser")
  jobs = soup.find_all('section', class_="jobs")

  for job_section in jobs:
    job_posts = job_section.find_all('li')
    job_posts.pop(-1)
    for post in job_posts:
      anchors = post.find_all('a')    
      anchor = anchors[1]
      link = anchor['href']
      company, kind, region = anchor.find_all('span', class_="company")
      title = anchor.find('span', class_='title')
      job_data = {
        'link' : f"https://weworkremotely.com/{link}",
        'company' : company.string, 
        'region' : region.string, 
        'position' : title.string
      }
      results.append(job_data)
  return results