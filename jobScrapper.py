from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Can't request website")

# beautifulsoup을 이용하여 html코드 탐색 find_all
else:
  soup = BeautifulSoup(response.text, 'html.parser')
  # class가 jobs인 section 찾기
  ## why class_? class는 python에서 이미 사용중
  jobs = soup.find_all('section', class_="jobs")

  # 해당 section의 ul에서 모든 li 찾기
  for job_section in jobs:
    job_posts = job_section.find_all('li')
    job_posts.pop(-1)
    for post in job_posts:
      print(post)
      print()
