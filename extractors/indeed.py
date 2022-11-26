from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# pagination - 페이지 개수 확인하기
# 페이지번호 우클릭 > inspect(검사) : 개발자도구에 표시됨(navigation 구성 확인) > 검색페이지가 5페이지 이상인지 확인
def get_page_count(keyword):
  options = Options()
  # replit에만 있음
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  browser = webdriver.Chrome(options=options)
  browser.get(f"https://kr.indeed.com/jobs?q={keyword}")

  soup = BeautifulSoup(browser.page_source, "html.parser")
  # find 내부에서 딕셔너리 호출
  pagination = soup.find("nav", {"aria-label": "pagination"})
  pages = pagination.select("div a")
  count = len(pages)+1
  
  for page in pages:
    if page['aria-label']=="Previous Page":
      count -= 1
    if page['aria-label']=="Next Page":
      count -= 1
  
  if count >= 5:
    return 5
  else:
    return count

# 페이지에서 데이터 추출
def extract_indeed_jobs(keyword):
  pages = get_page_count(keyword)
  results = []
  print("Found", pages, "pages")
  # 각 페이지에 요청을 보내 데이터 추출
  for page in range(pages):
    options = Options()
    # replit에만 있음
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options=options)
    # page가 바뀌면 시작페이지 바뀌도록 &start={page*10} 삽입
    browser.get(f"https://kr.indeed.com/jobs?q={keyword}&start={page*10}")
    print("Requesting", f"https://kr.indeed.com/jobs?q={keyword}&start={page*10}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    # 자식요소만 가져오기
    jobs = job_list.find_all("li", recursive=False)
    # 구인정보 가져오기
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
        # a 내부 속성은 딕셔너리로 저장 : 딕셔너리 호출
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
  return results