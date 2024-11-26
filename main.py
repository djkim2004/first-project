#혼공 80강(클래스 문법 기본) 파이썬에서 대문자시작->클래스
import re


class Student:
  def __init__(self,이름,국어,영어,수학,과학):
   self.이름=이름
   self.국어=국어
   self.영어=영어
   self.수학=수학
   self.과학=과학
  def sum(self):
    return self.국어 + self.영어 + self.수학 +self.과학
  def average(self):
    return self.sum()/4
  def print(self):
      print(self.이름,self.sum(),self.average(),sep="\t")
  
class StudentList:
  def __init__(self):
    self.students=[]
  def add(self,student):
    self.students.append(student)
  def print():
      print("이름","총점","평균",sep="\t")
      for student in self.students:
        student.print()
students=StudentList()
students.add(Student("인성",87,86,90,85))
students.add(Student("구름",67,88,20,58))
students.add(Student("별이",27,68,50,83))
students.print()

StudentList도 클래스로 만든이유
1)상속보다 구성(컴포지션)이 안전
2)리스트(컬렉션)은 클래스로 감싸서 "퍼스트 클래스 컬렉션"으로 만드는 것이 안전
하다는 설계적인 패턴이 있기 때문

#혼공 81강(특수한 이름의 함수,값 객체)
__eq__(같다)
__ne__(같지 않다)
__gt__(왼쪽 것이 더 크다)
__ge__(왼쪽 것이 크거나 같다)
__lt__(오른쪽 것이 더 크다)
__le__(오른쪽 것이 크거나 같다)
함수 구현하면 비교 연산자를 구현할 수 있다.

class Student:
  def __init__(self,이름,국어,영어,수학,과학):
   self.이름=이름
   self.국어=국어
   self.영어=영어
   self.수학=수학
   self.과학=과학
  def sum(self):
    return self.국어 + self.영어 + self.수학 +self.과학
  def average(self):
    return self.sum()/4
  def print(self):
      print(self.이름,self.sum(),self.average(),sep="\t")
  def __str__(self):
    return f"{self.이름}\t{self.sum()}\t{self.average()}"
  pass  
  def __eq__(self,다른대상): #self == 다른대상
    print("__eq__()함수호출")
    return self.sum()== 다른대상.sum()
  def __eq__(self,다른대상): #self != 다른대상
    print("__ne__()함수호출")
    return self.sum()!= 다른대상.sum()
  def __eq__(self,다른대상): #self > 다른대상
    if type(다른대상)==Student:
      print("__gt__()함수호출") #print함수 쓰는 타이팅모름
      return self.sum()> 다른대상.sum()  
    elif type(다른대상)==int:
      return self.sum()> 다른대상  
    else:
      raise "같은 자료형을 비교해주세요"
  def __eq__(self,다른대상): #self >= 다른대상
    print("__ge__()함수호출")
    return self.sum()>= 다른대상.sum()
  def __eq__(self,다른대상): #self < 다른대상
    print("__lt__()함수호출")
    return self.sum()< 다른대상.sum()
  def __eq__(self,다른대상): #self <= 다른대상
    print("__le__()함수호출")
    return self.sum()<= 다른대상.sum()
  #print함수를 쓸 때 a>300을 비교한다면 오류가 난다 왜냐면 300은 a랑 달리 sum이랑 연관없기 때문
  #이런 상황은 조건문이랑 예외처리를 써야한다.(__gt__구문 참조)-숫자랑도 비교할 수 있음()
#__gt__에 적용된 구문을 다른 곳에도 똑같이 적용해 줘야함

#(1)비교 연산자를 사용하게 해달라!
a=Students("인성",87,86,90,85)
a=Students("구름",92,82,80,86)
#a==b # 두 학생의 성적 총합이 같을 경우 true
print(a==a)
print(a==b)

class StudentList:
  def __init__(self):
    self.students=[]
  def add(self,student):
    self.students.append(student)
  def print():
      print("이름","총점","평균",sep="\t")
      for student in self.students:
        student.print()
  def __str__(self):
    output = "이름\t총점\t평균\n"
    for student in self.students:
      output += f"{str(student)}\n"
    return output.strip()
  def clone(self):
    output=StudentList()
    for student in self.students:
      output.add(student)
    return output  
  def __add__(self,다른대상): #self + 다른대상
    output=self.clone() #비파괴적으로 바뀜 81강깃허브자료 참고
    output.add(다른대상)
    return output
students=StudentList()
# (2) +연산자를 사용할 수 있게 해달라!
students += Student("인성",87,86,90,85))
students += Student("구름",67,88,20,58))
students.add(Student("별이",27,68,50,83))
#(3)print()함수를 일반적인 형태로 사용할 수 있게 해달라!
#students.print()
print(students)
print(Student("인성",87,88,98,95))

#82강(캡슐화)
class Circle:
  def __init__(self,반지름):
    if 반지름 < 0
     raise TypeError("반지름은 0이상이어야 합니다")
    self.__반지름=반지름
    self.__파이=3.14
  @property() #get_반지름 ->반지름
  def 반지름(self):
    return self.__반지름
  @반지름.setter  #set_반지름 ->반지름
  def 반지름(self,value):
    if value < 0  #예외처리많이하는 이유는 표시되기 쉬움을 위함
     raise TypeError("반지름은 0이상이어야 합니다")
    self.__반지름 = value 
    #비파괴적으로 바꾸자 -> return self.__반지름
  @property
  def 둘레(self):
    return 2*self.__파이*self.__반지름
  @property
  def 넓이(self):
    return self.__파이*(self.__반지름**2)

circle=Circle(10)
print(circle.get_반지름())
circle.set_반지름(20)
circle.__반지름 = -10 #외부에서 접근 불가
print(circle.둘레())
print(circle.넓이())

#그냥 반지름()로 위로 올라가지말고 바로 값을 할당하게 해달라 문파는 밑 처럼 코드작성
#밑처럼 작성할려고 하면 위처럼 @기호를 추가적으로 붙여야함
circle=Circle(10)
circle.반지름
circle.반지름 = 20
print(circle.둘레)
print(circle.넓이)

#83강(상속)
#원의 넓이를 구해서 + 멋있게 출력
class Shape:
  def __init__(self):
    raise "생성자를 구현해주세요."
  def 넓이(self):
    raise "넓이 함수를 구현해주세요. 넓이를 리턴하는 함수를 작성해주세요."
  def 출력보조(self):
    raise "출력 보조 함수를 구현해주세요. 출력 전 한마디를 입력해주세요."
  def 출력(self):
    print("="*10)
    print("="*10)
    self.출력보조()
    print(f"넓이:{self.넓이()}")
    print("="*10)
    print("="*10)

class Circle(Shape):
  def __init__(self,반지름):
    self.파이=3.14
    self.반지름=반지름
  def 출력보조(self):
    print(f"원의 반지름은 {self.반지름}")
  def 넓이(self):
    return self.반지름*self.반지름*self.파이

class Sqaure(Shape):
  def __init__(self,반지름):
    self.길이=길이
  def 출력보조(self):
    print(f"정사각형 한 변의 길이는 {self.길이}")
  def 넓이(self):
    return self.길이*self.길이

sqaure=Sqaure(10)
sqaure.출력()          
circle=Circle(10)
Circle.출력() #위 Circle클래서 함수에서 인스턴스인 circle이 없으니깐 shape함수로 넘어감 
             #만약 shape함수에도 상속이 걸려있다 그런데 해당함수가 없으면 계속 위로 올라가는 것
             #shape함수에서 출력보조를 호출했는데 circle클래스이기때문에 다시 돌아와 CIRCLE에서 찾음
             #Circle(shape)일때 Circle이 자식클래스(서브클래스), Shape가 부모클래스(슈퍼클래스)

#일일이 하나하나 코드 작성하는 것 위 함수처럼 만들면 개편함
class Cirle:
  def __init__(self):
    self.파이 =  3.14
    self.반지름 = 반지름
  def 넓이(self):
    return self.반지름*self.반지름*self.파이
  def 출력(self):
    print("="*10)
    print("="*10)
    print(f"원의 반지름:{self.반지름}")
    print(f"넓이:{self.넓이()}")
    print("="*10)
    print("="*10)
class Triangle:  #이런식으로 유사한 것을 만들기위해서 복붙하다보면 시간증가 및 오류발생 빈도가 는다
class Rectangle: #그러하기 때문에 위 class shape모양을 만들어야한다.
class Ellipse:
class Sqaure:
      def __init__(self):
        self.길이 = 길이
      def 넓이(self):
        return self.길이**2
      def 출력(self):
        print("="*10)
        print("="*10)
        print(f"정사각형 한 변의 길이:{self.길이}")
        print(f"넓이:{self.넓이()}")
        print("="*10)
        print("="*10)

circle = Circle(10)
circle.출력()
  
sqaure= Sqaure(10)
sqaure.출력()

#혼공84강(오버라이트.super())
#(오버라이드)자식에서 부모함수를 호출하는 방법
class 부모:
  def 함수(self):
    print("부모 함수")

class 자식(부모):
  def 함수(self):
    super().함수()
    print("자식 함수")
    #1
    부모.함수(self)
    #2(많이 사용함)
    super().함수()

child=자식()
#child.함수()
자식.함수(child) #많이 사용X (많이 사용하지 않더라도 원리 이해하기)

#super()함수 쓰는 예시
#부모클래스를 사용하는 이유는 가독성 때문임
class 버튼:
  def __init__(self):
    print("버튼을 초기화합니다.")
    print("버튼을 만듭니다.")
    print("버튼을 화면에 출력합니다.")
class 빨간버튼(버튼):
  def __init__(self):
    super().__init__()
    print("버튼을 빨간색으로 칠합니다.")
class 파란버튼(버튼):
  def __init__(self):
    super().__init__()
    print("버튼을 파란색으로 칠합니다.")
class 초록버튼(버튼):
  def __init__(self):
    super().__init__()
    print("버튼을 초록색으로 칠합니다.")

빨간버튼()
파란버튼()
초록버튼()

#혼공 85강 (상속과 컴포지션)
class Student:
  def __init__(self):
    self.수학 = 수학
#리스트 클래스를 상속받기만 하면 기능사용가능
class StudentList(list):
  pass

학생목록 = StudentList()
학생목록.append(Student(90))
학생목록.append(Student(80))
학생목록.append(Student(70))
for 학생 in 학생목록:
  print(학생,수학)

#이 코드는 현대상황에선 안 씀 Because 리스트기능을 다 가져오면 위험함
#오버라이드로 블랙리스트마련해야할게 너무 많아지기때문
#많은 요소를 갖고 있는 클래스를 상속 받아서 위험요소를 숨기는것[블랙리스트]보다는
#많은 요소를 갖고 있는 클래스를 캡슐화로 숨기고 필요한 요소만 공개하는 것[화이트리스트]이 쉽습니다.
#마지막 코드가 컴포지션 
#프레임워크가 상속을 강제하면 쓰고 아니면 컴포지션을 쓴다고 알고 있으면 됨
class Student:
  def __init__(self):
    self.수학 = 수학
class StudentList:
  def __init__(self):
    self.__리스트 = []
  def append(self,요소):
    if type(요소) != Student:
      raise "Student 클래스만 추가할 수 있습니다."
    self.__리스트.append(요소)
  def sum(self):
    output = 0
    for 학생 in self.__리스트:
      output += 학생.수학
    return output
  def average(self):
    return self.sum() / len(self)


학생목록 = StudentList()
학생목록.append(Student(90))
학생목록.append(Student(80))
print(학생목록.sum())
print(학생목록.average())

#혼공 86강(도전문제)
#스택이랑 큐 둘 다 꺼내오는 느낌이지 삭제하는건 아님
#리스트에서는 삭제
#스택

선입후출(Fisrt in Last out)(FILO)
후입선출(Last in First out)(LIFO)
구조를 갖는 자료 구조
푸시(push): 스택에 자료를 넣는 행위
팝(pop) : 스택에서 자료를 꺼내는 행위

class Stack
 def __init__(self):
   self.__list = []
 def push(self,value):
   self.__list.append(value)
 def pop(self):
   output = self.__list[-1]
   del self.__list[-1]
   return output

stack = Stack()
stack.push(10) #10
stack.push(20) #10 20
stack.push(30) #10 20 30
print(stack.pop()) #10 20 30
print(stack.pop()) #10 20
print(stack.pop()) #10
#큐
선입선출(First in First out)
인큐(enqueue): 큐에 자료를 넣는 행위
디큐(dequeue): 큐에서 자료를 꺼내는 행위

class Queue
 def __init__(self):
   self.__list = []
 def enqueue(self,value):
   self.__list.append(value)
 def dequeue(self):
   output = self.__list[0]
   del self.__list[0]
   return output

queue = Queue()
queue.enqueue(10) #[10]
queue.enqueue(20) #[10 20]
queue.enqueue(30) #[10 20 30] 
print(queue.dequeue()) # 10 [20 30]
print(queue.dequeue()) #20 [30]
print(queue.dequeue()) # 30

#질문모음(1)
1 < x < 10
->1 < x and x < 10

1 in [] == False
-> (1 in []) and ([] ==  False)
-> (False) and (False)
-> False

(1 in []) == False
-> False == False
-> True          
이해하기 힘든 코드 작성을 피하려면 
(1)비교 연산자 연결은 같은 대소비교 연산자만 사용하자
(2) in/is 연산 등은 표현식 하나에 한 번만 사용하자

#90강 모듈

class Circle:
  def __init__(self,반지름):
    if 반지름 < 0:
      raise ValueError("반지름은 0이상이어야 합니다.")
    self.__PI = 3.14
    self.__반지름 = 반지름
  def 넓이(s):
    return s.__PI * s.__반지름 ** 2
  def 둘레(s):
    return 2 * s.__PI * s.__반지름

if __name__ == "__main__":
  ss Circle:
    def __init__(self,반지름):
      if 반지름 < 0:
        raise ValueError("반지름은 0이상이어야 합니다.")
      self.__PI = 3.14
      self.__반지름 = 반지름
    def 넓이(s):
      return s.__PI * s.__반지름 ** 2
    def 둘레(s):
      return 2 * s.__PI * s.__반지름

  if __name__ == "__main__":
    #을 사용하는 것은 보통 main.py가 아니라 모듈.py파일에서 많이 사용함
    print("넓이()를 검증합니다.")
    if Circle(10).넓이() - 314 < 10 ** -7:
      print("넓이()검증을 성공했습니다: Success")
    else:
      print("넓이()검증을 실패했습니다: Fail")
    print("둘레()를 검증합니다.")
    if Circle(10).둘레() - 62.8 < 10 ** -7:
      print("넓이()검증을 성공했습니다: Success")
    else:
      print("넓이()검증을 실패했습니다: Fail")을 사용하는 것은 보통 main.py가 아니라 모듈.py파일에서 많이 사용함

      #위 코드는 모듈.py에 적는 코드고 main.py에서는 적는 코드는 아래코드
import hellomodule as h

c = h.Circle(10)
print(c.넓이())
print(c.둘레())

#91강
#패키지
모듈의 규모가 커졌을때 그 모듈을 나누는 방법
모듈은 "관심사를 기반으로 함수와 변수를 나누는 것"
-> 그 관심사들을 더 크게 묶는 방법
-> 패키지
1.폴더 내부에 있는 모듈을 읽어 들이는 방법
2.폴더 자체를 모듈로 읽어 들이는 방법
main.py 폴더와   school 폴더 안에 있는 student.py , studentlist.py가 있다.

-student.py에는 
class Student:
  def __init__(self,수학):
   self.수학 = 수학
  def sum(self):
    return self.수학
-studentlist.py에는
class StudentList:
  def __init__(self):
   self.__list = []
  def append(self,학생):
    self.__list.append(학생)
  def print(self):
    for student in self.__list:
      print(student.sum())

#1번째 방법처럼 내부에 있는 모둘을 사용할때는 from import 구문을 써야함
폴더 내에 student와 studentlist만 있으니깐 아무 기호를 써도 됨 (import 뒤 변수를 말함)
main.py에서 
from school.studnet import Student
from school.studnetlist import StudentList

sl = StudentList(
sl.append(student(100))
sl.append(student(90))
sl.append(student(80))
sl.append(student(70))
sl.print()

#2번째방법  
school폴더 안에 __init__.py파일을 만들어줘서 파일 안에
a = "모듈입니다"
def b():
  print("school 모듈입니다.")

-main.py에서
import school
print(school.a)
school.b() 를 사용

#이 두 가지를 모두 활용할려면 어떻게 해야하나
.을 붙이는 이유: 상대적인 경로를 나타내야지 오류가 발생안함
.모듈: 현재 폴더를 기준으로
..모듈: 상위 폴더를 기준으로 찾는다. 이런식으로 생각하면 된다
__init__.py파일에
__all__ = ["Student,StudentList"] #main.py에서 a,b는 인식을 못 함

from .studnet import Student
from .studnetlist import StudentList

a = "모듈입니다"
def b():
  print("school 모듈입니다.")

-main.py
from school import *
#서브모델로 활용가능
student.Student
studentList.StudentList

    

 




