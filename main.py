from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

keyword = input("What do you want to search for?")

# 파일열기 / 한글 인코딩 utf-8-sig
file = open(f"{keyword}.csv","w",encoding="utf-8-sig")
# 아래 코드는 csv파일 규칙에 맞춰 작성됨
# csv 파일 규칙 : 열을 쉼표로 구분, 새 행은 새 줄로 구분(개행문자 삽입)
file.write("Position,Company,Location,URL\n")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

jobs = indeed + wwr

for job in jobs:
  # 파일 내용 작성
  # 따옴표 내 따옴표 작성할 땐 쌍따옴표와 쌍따옴표가 아닌 것으로 구분
  file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")
  # 발생문제 : 잘못 분리되는 내용이 있음
  # 해결방법 : 파일에 작성하기 전 데이터에서 불필요한 콤마 지워주기
file.close()
