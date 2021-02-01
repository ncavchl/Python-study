# Python-study
1) 2019.12 - 파이썬 학습 - 생활코딩 edwith.org - 김문주 교수 
2) 2021.02 - 프로그래머스 - 파이썬 코테  https://programmers.co.kr/learn/courses/2


  (1) 파이썬 주석 # 
   ~~~
   #주석이다
   print('Hello World')
   ~~~
    
   (2) if 문
   ~~~
   if a<b:
    print('들여쓰기')
    
   if True: 
    #꼭 T는 대문자
    
   if False:
    #꼭 F는 대문자
   ~~~
   
   (3) 블럭 <br>
   함께 실행되는 하나의 코드 덩어리로, 들여쓰기로 구분한다.<Br>
   블럭 안에 다른 블럭이 들어갈 수 있다.
  
   (4) if, else, elif
   ~~~
   if a == b:
    print('')
   elif b == c:
    print('')
   else:
     print('')
   ~~~
   
   (5) 함수
   ~~~
   def functiontest():
    print('함수는 def 으로 정의')
   ~~~

   (6) format
   ~~~
   a = 3
   b = 5
   print("{} + {}" .format(a,b))
   ~~~
   
  (7) 문자열 ', " 출력을 원할시  """ ~~ """ 
  ~~~
  print(' " ')
  print(" ' ")
  string = """ '랑 " 둘다 """
  print(string)
  #줄바꿈은 \n 
  ~~~
  
  (8) 정수 실수
  - a = 5//3 : // 몫 연산자
  - int(5.4) : 정수 
  - float(5) = 5.0 : 실수 
  
  
  (9) 사용자 입력 받기 
  - 사용자의 키보드 입력을 return
  ~~~
  print('가위 바위 보 중 하나를 내주세요> ', end = ' ')
  mine = input()
  print('mine:', mine)
  ~~~

  간단한 print기능을 내장
  ~~~
  mine = input('가위 바위 보 중 하나를 내주세요> ')
  print('mine:', mine)
  ~~~
