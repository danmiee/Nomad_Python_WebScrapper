from flask import Flask

# 플라스크 애플리케이션 생성
app = Flask("JobScrapper")

@app.route("/")
def home():
  return 'hey there!'

# 이 코드는 Replit에서 만든 VM에서 실행되므로 Replit에게 웹사이트 만들거니 접속을 열어달라고 알려주기
app.run("0.0.0.0")
