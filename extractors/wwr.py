from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?term="
  response = get(f"{base_url}{keyword}")
  
  if response.status_code != 200:
    print("Can't request website")
  
  # beautifulsoup을 이용하여 html코드 탐색하고 python 개체로 변경(find_all)
  else:
    # for문 안에서 만들어진.job_data를 유지하기 위한 필드
    results = []
    soup = BeautifulSoup(response.text, 'html.parser')
    # class가 jobs인 section 찾기
    ## why class_? class는 python에서 이미 사용중
    jobs = soup.find_all('section', class_="jobs")
  
    for job_section in jobs:
      # 해당 section의 ul에서 모든 li 찾기
      job_posts = job_section.find_all('li')
      # 불필요한 마지막 요소 제외
      job_posts.pop(-1)
      for post in job_posts:
        # li 내 모든 a 가져오기
        anchors = post.find_all('a')
        # 원하는 값의 위치를 아는 경우 인덱스로 가져오기     
        anchor = anchors[1]
        # 태그의 속성값 가져오기
        link = anchor['href']
        # 자식요소 가져와서 이름붙이기(딕셔너리 형태)
        company, kind, region = anchor.find_all('span', class_="company")
        # 타이틀 가져오기
        title = anchor.find('span', class_='title')
        # bs요소에서 텍스트 가져오기(.string)
        job_data = {
          'link' : f"https://weworkremotely.com/{link}",
          'company' : company.string, 
          'region' : region.string, 
          'position' : title.string
        }
        results.append(job_data)
    return results