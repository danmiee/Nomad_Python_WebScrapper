from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# replit에만 있음
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=options)
browser.get("https://kr.indeed.com/jobs?q=python&limit=50")

results = []
soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList")
# 자식요소만 가져오기
jobs = job_list.find_all("li", recursive=False)
for job in jobs:
  # class=mosaic-zone인 태그 제외
  zone = job.find("div", class_="mosaic-zone")
  if zone == None:
    
    # li에서 job 추출 : h2 class="jobTitle"
    # h2 > a의 링크, label 저장
    anchor = job.select_one("h2 a")  # select : list / select_one : element
    # h2 = job.find("h2", class_="jobTitle")
    # a = h2.find("a")
    
    # BeautifulSoup은 html태그들을 데이터 구조로 변환시킴(list, dict)
    # a 내부 속성은 딕셔너리로 저장되어 쉽게 불러올 수 있음
    title = anchor['aria-label']
    link = anchor['href']

    # companyLocation, companyInfo div 가져오기
    company = job.find("span", class_="companyName")
    location = job.find("div", class_="companyLocation")
    
    # region, city, position, company name : wws에서 찾아뒀음
    job_data = {
      # 링크 가져올 때 상대경로 여부에 주의
      'link': f"https://kr.indeed.com{link}",
      'company': company.string,
      'location': location.string,
      'position': title
    }
    results.append(job_data)

for result in results:
  print(result, "\n")