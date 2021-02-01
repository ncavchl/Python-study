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
  - rount(4.6) : 반올림
  
  (9) 사용자 입력 받기 
  - 사용자의 키보드 입력을 return
  ~~~
  print('가위 바위 보 중 하나를 내주세요> ', end = ' ')
  mine = input()
  print('mine:', mine)
  ~~~

  - 간단한 print기능을 내장
  ~~~
  mine = input('가위 바위 보 중 하나를 내주세요> ')
  print('mine:', mine)
  ~~~
  
  
  (10) list 
  - list[-1] 인 경우 뒤에서 첫번째 
  - 리스트에 새로운 값을 추가하는 방법
    - list1=[1,2,3]이라고 할 때
    - append를 이용
      ~~~
      list1.append(4)
      ~~~
      -append를 이용하면 리스트에 새로운 값이 추가된다.
    - 뒤에 새로운 리스트를 더하기
      ~~~
      list2=list1+[4]
      ~~~
      -list1은 그대로 두고, 새로운 리스트를 만들어 낸다.
      
  - 리스트에 값이 들어있는지 확인하는 방법
     - in 연산을 이용
      ~~~
      #12라는 값이 리스트에 들어있는지 확인하는 코드
      n=12
      if n in list1:
          print('{}가 리스트에 있다.'.format(n))
      ~~~
      
  - 리스트에서 필요 없는 값을 지우는 방법
    - del을 이용해서 특정 위치의 값을 지우기
      -del list1[10] 리스트의 10번째 값을 지워라
    - remove를 이용해서 특정 값을 지우기
      -list1.remove(40)을 하면 리스트에 40이라는 값이 있는경우 삭제
      -여러개의 값이 있는 경우 가장 앞에 있는 하나만 지워짐

      
  (11) for 문 <br>
    -for in 반복문
      -코드를 필요한만큼 반복해서 실행
      ~~~
      for pattern in patterns:
          print (pattern)
      ~~~
       - 리스트 patterns의 값을 하나씩 꺼내 pattern으로 전달
       - 리스트의 길이만큼 print (pattern) 실행
