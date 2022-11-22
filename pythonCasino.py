# 랜덤메소드 임포트
from random import randint

# 컴퓨터 랜덤숫자
pc_num = randint(1, 50)
print(pc_num)

# 반복조건 변수선언
playing = True

while (playing):
  # 유저 숫자 입력
  user_num = int(input("숫자를 입력하세요."))
  print(user_num)
  # 컴퓨터 = 유저 : 유저 win
  if pc_num == user_num:
    print("You Win")
    playing = False
  # 컴퓨터 < 유저 : upper
  elif pc_num < user_num:
    print("Lower")
  # 컴퓨터 > 유저 : lower
  else:
    print("Upper")
