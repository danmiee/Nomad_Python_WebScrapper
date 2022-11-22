# 계산기 만들기
# +, -, *, /, **, % 오류 발생하지 않게하기
def plus(a=0, b=0):
  print(a + b)
  
def minus(a=0, b=0):
  print(a - b)


def multiple(a=0, b=1):
  print(a * b)


def square(a=0, b=0):
  print(a**b)


def divide(a=1, b=1):
  if b == 0:
    print("0으로 나눌 수 없습니다")
  else:
    print(a / b)


def remainder(a=1, b=1):
  if b == 0:
    print("0으로 나눌 수 없습니다")
  else:
    print(a % b)


plus()
plus(1)
plus(1, 2)
minus()
minus(1)
minus(1, 2)
multiple()
multiple(2)
multiple(3, 2)
square()
square(3)
square(2, 3)
divide()
divide(2)
divide(5, 2)
divide(3, 0)
remainder()
remainder(1)
remainder(5, 2)
remainder(3, 0)
