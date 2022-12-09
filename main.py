from flask import Flask, render_template, request
# render_template : flask가 templates를 찾게 함
# 유저가 응답을 받기 전에 변수를 data로 변경
# request : 브라우저에 가서 콘텐츠 요청하는 것을 의미
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

# 플라스크 애플리케이션 생성
app = Flask("JobScrapper")

db = {}

# request - springboot 어노테이션 역할
@app.route("/")
def home():
  # templates 폴더명 변경 불가 / main.py와 같은 위치에 존재해야함
  # home.html 파일명 변경 가능 / render_template 안에는 동일하게 기재해야함
  return render_template("home.html",name="nico")

@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  # keyword가 db 안에 있으면 그 값을 리턴
  if keyword in db:
    jobs = db[keyword]
  else:
    # 없으면 검색해서 db에 저장하고 리턴
    indeed = extract_indeed_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = indeed + wwr
    db[keyword] = jobs
  return render_template("search.html", keyword = keyword, jobs = jobs)


# 이 코드는 Replit에서 만든 VM에서 실행되므로 Replit에게 웹사이트 만들거니 접속을 열어달라고 알려주기
app.run("0.0.0.0")
