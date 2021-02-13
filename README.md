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
      append를 이용하면 리스트에 새로운 값이 추가된다.<br>
    - 뒤에 새로운 리스트를 더하기
      ~~~
      list2=list1+[4]
      ~~~
      list1은 그대로 두고, 새로운 리스트를 만들어 낸다.<br>
      
  - 리스트에 값이 들어있는지 확인하는 방법
     - in 연산을 이용
      ~~~
      #12라는 값이 리스트에 들어있는지 확인하는 코드
      n=12
      if n in list1:
          print('{}가 리스트에 있다.'.format(n))
      ~~~
      <br>
  - 리스트에서 필요 없는 값을 지우는 방법
    - del을 이용해서 특정 위치의 값을 지우기<br>
      del list1[10] 리스트의 10번째 값을 지워라<br>
    - remove를 이용해서 특정 값을 지우기<Br>
      list1.remove(40)을 하면 리스트에 40이라는 값이 있는경우 삭제<br>
      여러개의 값이 있는 경우 가장 앞에 있는 하나만 지워짐
  
  - 리스트 뒤부터 읽기 
  ~~~
  for a in array[::-1]
  ~~~
  

  (11) for 문
  - for in 반복문
    - 코드를 필요한만큼 반복해서 실행
      ~~~
      for pattern in patterns:
          print (pattern)
      ~~~
      - 리스트 patterns의 값을 하나씩 꺼내 pattern으로 전달
      - 리스트의 길이만큼 print (pattern) 실행
      

  - for in range : <b>0부터 색인 시작</b>
    - range 함수
      - 필요한 만큼의 숫자를 만들어내는 유용한 기능
      ~~~
      for i in range(5):
          print(i)
      ~~~

    - enumerate
      - 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
      ~~~
      names = ['철수', '영희', '영수']
      for i, name in enumerate(names):
        print('{}번: {}'.format(i + 1, name))
        
      #len(vararr) 의 경우 list 길이 알 수 있음 
      ~~~
      
    (12) 모듈
    - 모듈
      - 미리 만들어진 코드를 가져와 쓰는 방법
      - import 모듈이름
      - 사용 방법: 모듈이름.모듈안의 구성요소
      ~~~
      math.pi
      random.choice()
      ~~~ 

    - 모듈의 예
      - import math
        - 수학과 관련된 기능
      - import random
        - 무작위와 관련된 기능
      - import urllib.request
        - 인터넷의 내용을 가져오는 기능
        
        
     (13) random
     - import random
     ~~~
    import random
    list = ["빨","주","노","초","파","남","보"]
    
    random_element = random.choice(list)  #해당 리스트 내 랜덤변수 선택 
    
    random_number = random.randint(a,b)   #a이상 b이하인 범위의 정수 출력 
    
    random.shuffle(list)                  #list 순서 변경 
     ~~~


  (14) 딕셔너리 <b>중요</b>
  - 여러 값을 저장해 두고 필요한 값을 꺼내 쓰는 기능
  - 이름표를 이용하여 값을 꺼내 사용
  - 사용할 때는 리스트와 비슷한 방식
  ~~~
  wintable = {
      '가위' : '보',
      '바위' : '가위',
      '보' : '바위',
  }

  print(wintable['가위'])
  ~~~

  ~~~
  #삭제 
  del(dict['one'])
  dict.pop('two')
  ~~~
  
  - 딕셔너리와 반복문 활용
    - 경우에 따라 가져올 값을 정할 수있다.
    ~~~
    for key in ages.keys(): # keys() 생략 가능
        print(key)
    for value in ages.values():
        print(value)
    ~~~
    - key와 value 둘다 가져올 수 있다.
    ~~~
    for key, value in ages.items():
        print('{}의 나이는 {} 입니다'.format(key, value))
    ~~~
    - 딕셔너리는 값의 순서를 지키지 않는다.
    
    - 리스트와 비교
    - 공통점

    
      |공통점|리스트|딕셔너리|
      |------|---|---|
      |생성|list = [ 1, 2 ,3 ]|dict = { 'one':1, 'two':2 }|
      |호출|list[ 0 ]|dict[ 'one' ]|
      |삭제|del( list[ 0 ] )|el( dict[ 'one' ] )|
      |개수 확인|len( list )|len( dict )|
      |값 확인|2 in list|'two' in dict.keys( )|
      |전부 삭제|list.clear( )|dict.clear( )|


    - 차이점
    
      |차이점|리스트|딕셔너리|
      |------|---|---|
      |순서|삭제 시 순서가 바뀌기 때문에 인덱스에 대한 값이 바뀐다|key로 값을 가져오기 때문에 삭제 여부와 상관없다|
      |결합|list1 + list2|dict1.update( dict2 )|



20210207
ch10부터

20210211
20200212
20200213
