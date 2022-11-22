from requests import get
import traceback

# 사이트 리스트 만들기
websites = ("google.com", "https://naver.com", "github.com",
            "instagram.com", "https://kakao.com")

# 결과 담을 변수 선언
results = {}

try:
  # http프로토콜 기재여부 확인하여 넣어주기
  for website in websites:
    if not website.startswith("https://"):
      website = f"https://{website}"
      # 넣어주기@@
    code = get(website).status_code

  # requests 라이브러리 추가 및 활용하여 http 상태 코드로 접속가능여부 확인하기
    if code < 200:
      results[website] = 'waiting'
    elif code < 300:
      results[website] = 'success'
    elif code < 400:
      results[website] = 'redirection'
    elif code < 500:
      results[website] = 'client error'
    else:
      results[website] = 'server error'
  print(results)
except:
  print("오류발생")
  print(traceback.format_exc())