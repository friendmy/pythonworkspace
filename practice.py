# # 애완동물을 소개해 주세요~
# animal = "강아지"
# name = "해피"
# age = 4
# hobby = "낮잠"
# is_adult = age >= 3

# print("우리집 " + animal + "의 이름은 " + name + "에요")
# hobby = "공놀이"
# # print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
# print(name + "는 어른일까요? " + str(is_adult))

# print(5 % 3)  # 나머지
# print(5 // 3)  # 몫
# print(not (1 != 3))
# print((3 > 0) and (3 < 5))
# print((3 > 0) & (3 < 5))
# print((3 > 0) or (3 > 5))
# print((3 > 0) | (3 > 5))
# print(5 > 4 > 3)

# print(abs(-5))
# print(pow(4, 2))
# print(max(5, 12, 15))
# print(min(5, 2))
# print(round(3.15))
# print(round(4.99))

# from math import *

# print(floor(4.99))
# print(ceil(3.14))
# print(sqrt(4))

# from random import *

# print(random())  # 0.0 ~ 1.0 미만의 임의의 값
# print(random() * 10)  # 0.0 ~ 10.0 미만의 값 생성
# print(int(random()) * 10)  # 0 ~ 10 미만의 값 생성
# print(int(random() * 10) + 1)  # 0 ~ 10 이하의 값 생성
# from random import *

# print(int(random() * 45) + 1)

# print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성

# print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성

# print(randint(4, 28))

# from random import *

# print("오프라인 스터디 모임 날짜는 매월 " + str(randint(4, 28)) + "일로 선정되었습니다.")

# sentence = """
# 와우
# WOW
# 와~
# """
# print(sentence)

# jumin = "990101-1212121"

# print("성별:" + jumin[7])  # 0 으로 시작 7번째
# print("연 : " + jumin[0:2])  # 0부터 2 직전까지
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 " + jumin[:6])  # 처음부터 6 직전까지
# print("뒤 7자리 : " + jumin[7:])  # 7부터 끝까지
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:])  # 맨 뒤에서 7번째부터 끝까지

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)

# index = python.index("n", index + 1)
# print(index)

# print(python.find("n"))
# print(python.find("Java"))  # -1
# print(python.index("Java"))  # error

# print(python.count("n"))

###################### 문자열 포맷 ########################

# 방법 1
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple 은 %c로 시작해요." % "A")
# %s
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# # 방법 3
# print("나는 {age}살이며 {color}색을 좋아해요.".format(age=20, color="빨간"))

# # 방법 4
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며 {color}색을 좋아해요.")

###################### 탈출문자 ########################

# \n 줄바꿈
# \" \' \\
# \r 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# \b : 백스페이스 ( 한 글자 삭제 )
# print("Redd\bApple")

# \t : 탭
# print("Red\tApple")

# 패스워드
# url = "http://naver.com"

# password = url.replace("http://", "")
# password = password[: password.index(".")]
# password = password[:3] + str(len(password)) + str(password.count("e")) + "!"

###################### 리스트 ########################

# # 지하철 칸별로 10명 20명 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)

# subway.insert(1, "정형돈")
# print(subway)

# # 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# # 같은 이림의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬도 가능
# num_list = [5, 2, 4, 3, 1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용
# num_list = [5, 2, 4, 3, 1]
# mix_list = ["조세호", 20, True]
# print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

###################### dictionary########################
# cabinet = {3: "유재석", 100: "김태호"}
# # print(cabinet[3])

# # # print(cabinet[3]) # 오류
# # print(cabinet.get(5))  # None 리턴
# # print(cabinet.get(5, "사용 가능"))  # "사용 가능" 리턴

# # print(3 in cabinet)
# # print(5 in cabinet)

# cabinet = {"A-3": "유재석", "B-100": "김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "김종국"
# print(cabinet)

# # 간 손님
# del cabinet["A-3"]
# print(cabinet)

# # key 들만 출력
# print(cabinet.keys())
# print(cabinet.values())

# # key value 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 폐점

# cabinet.clear()
# print(cabinet)

###################### 튜플########################
# 변경되지 않는 목록

# menu = ("돈까스", "치즈까스")
# print(menu[0])

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

###################### SET(집합) ########################
# 중복 안됨, 순서 없음
# my_set = {1, 2, 3, 3, 3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 (java 와 python 을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# # 합집합 (java 할 수 있거나 python을 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# # 차집합 (java 할 수 있지만 python을 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java 를 잊었어요
# java.remove("김태호")
# java.union(python)
# print(java)

###################### 자료구조의 변경 ########################
# 커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))


############################ 퀴즈 ##############################
# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다 --

# -- (활용 예제)
# from random import *

# users = range(1, 21)  # 1부터 20까지 숫자를 생성
# # print(type(users))
# users = list(users)
# # print(type(users))

# winners = sample(users, 4)  # 4명 중에서 1명은 치킨, 3명은 커피
# print(winners)

# print("-- 당첨자 발표 --")
# print(f"치킨 당첨자 : {winners[0]}")
# print(f"커피 당첨자 : {winners[1:]}")
# print(f"-- 축하합니다 --")


############################ if ##############################
# weather = "비"
# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요없어요.")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요.")

############################ for ##############################

# for waiting_no in [0, 1, 2, 3, 4]:
# for waiting_no in range(5):
# for waiting_no in range(1, 6):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

############################ while ##############################
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요...".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# 무한루프
# customer = "아이언맨"
# index = 5
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}회.".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")


############################ continue break ##############################
# continue 다음반복으로
# break 반복문 끝
# absent = [2, 5]
# no_book = [7]  # 책을 깜박했음
# for student in range(1, 11):
#     if student in absent:
#         continue
#     if student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

############################ 한줄 for ##############################
# 출석번호가 1 2 3 4ㅡ 앞에 100을 붙이기로 함 -> 101, 102
# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i + 100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대분자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

############################ 퀴즈 ##############################
# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은ㅇ 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [ ] 3번째 손님 (소요시간: 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 15분)

# 총 탑승 승객: 2 분

# from random import *

# customerCount = 0
# for customer in range(1, 51):  # 50명의 승객
#     time = randint(5, 50)
#     if 5 <= time <= 15:
#         print(f"[O] {customer}번째 손님 (소요시간 : {time}분)")
#         customerCount += 1
#     else:
#         print(f"[ ] {customer}번째 손님 (소요시간 : {time}분)")

# print(f"총 탑승 승객 : {customerCount} 분")

############################ function ##############################
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")


# def deposit(balance, money):  # 입금
#     print(f"입금이 완료되었습니다. 잔액은 {balance + money}")
#     return balance + money


# def withdraw(balance, money):  # 출금
#     if balance >= money:
#         print(f"출금이 완료되었습니다. 잔액은 {balance - money}")
#         return balance - money
#     else:
#         print("잔액이 부족합니다.")
#         return balance


# def withdraw_night(balance, money):  # 저녁에 출금
#     commission = 100  # 수수료 100원
#     return commission, balance - money - commission


# balance = 0  # 잔액
# balance = deposit(balance, 100000)
# balance = withdraw(balance, 70000)
# commission, balance = withdraw_night(balance, 20000)
# print(f"수수료는 {commission}원이며, 잔액은 {balance}원 입니다.")

######################################### 기본값 #########################################
# def profile(name, age, main_lang):
#     print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))


# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업.
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))


# profile("유재석", 20, "파이썬")
# profile("김태호")

######################################### 함수호출(키워드값) #########################################
# def profile(name, age, main_lang):
#     print(name, age, main_lang)


# profile(name="유재석", main_lang="파이썬", age=20)
# profile(name="김태호", age=25, main_lang="자바")

######################################### 가변인자 #########################################
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)


# profile("유재석", 20, "Python", "java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")


# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()


# profile("유재석", 20, "Python", "java", "C", "C++", "C#", "Javascript")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")

######################################### 지역변수,전역변수 #########################################

# gun = 10


# def checkpoint(soldiers):  # 경계근무
#     global gun  # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))


# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun


# # checkpoint(2)  # 2명이 경계 근무 나감
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

########################################### 퀴즈5 ####################################################

# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#     * 함수명 : std_weight
#     * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.


# def std_weight(height, gender):
#     if gender == "남자":
#         return round(height / 100 * height / 100 * 22, 2)
#     elif gender == "여자":
#         return round(height / 100 * height / 100 * 21, 2)


# height = 173
# gender = "남자"
# weight = std_weight(height, gender)
# print(f"키{height}cm {gender}의 표준 체중은 {weight}kg 입니다.")

########################################### 표준 입출력 ###############################################
# print("Python", "Java", sep=",", end="?")
# print("무엇이 더 재밌을까요?")

# import sys

# print("Python", "Java", file=sys.stdout) # 표준출력
# print("Python", "Java", file=sys.stderr) # 표준에러

# 시험 성적
# scores = {"수학": 0, "영어": 50, "코딩": 100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003, ...

# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print("입려가신 값은 " + answer + "입니다.")

########################################### 다양한 출력 포맷 ###############################################

# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(1000000000000000000000))
# # 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
# print("{0:+,}".format(1000000000000000000000))
# print("{0:+,}".format(-1000000000000000000000))
# # 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# # 돈이 많으면 행복하니까 빈 자리는 ^ 로 채워주기
# print("{0:^<+30,}".format(10000000000000000))
# # 소수점 출력
# print("{0:f}".format(5 / 3))
# # 소수점 특정 자리수 까짐만표시( 소수점 3째 자리에세 반올림)
# print("{0:.2f}".format(5 / 3))

########################################### 파일 입출력 ###############################################

# score_file = open("score.txt", "w", encoding="utf8") # 쓰기 덮어쓰기
# print("수학: 0", file=score_file)
# print("영어: 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")  # 이어쓰기 append
# score_file.write("과학: 80")
# score_file.write("\n코딩: 100")  # write는 줄바꿈이 없다.
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()  # list 형태로 저장

# for line in lines:
#     print(line, end="")
# score_file.close()

########################################### pickle ###############################################
# import pickle

# 쓰기
# profile_file = open("profile.pickle", "wb")
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)  # profile 에 있는 정보를 file에 저장
# profile_file.close()

# 읽기
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)  # file에 있는 정보를 profile에 불러오기
# print(profile)

########################################### with ###############################################
# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())


########################################### Quiz #7 ###############################################

# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.

# for report in range(1, 51):
#     with open(f"{str(report)}주차.txt", "w", encoding="utf8") as study_file:
#         study_file.write(f"- X {str(report)}주차 주간보고 -")
#         study_file.write("\n부서 :")
#         study_file.write("\n이름 :")
#         study_file.write("\n업무 요약 :")

########################################### class ###############################################

# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = "마린"  # 유닛의 이름
# hp = 40  # 유닛의 체력
# damage = 5  # 유닛의 공격력

# print(f"{name} 유닛이 생성되었습니다.")
# print(f"체력 {hp}, 공격력 {damage}\n")

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print(f"{tank_name} 유닛이 생성되었습니다.")
# print(f"체력 {tank_hp}, 공격력 {tank_damage}\n")


# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print(f"{tank2_name} 유닛이 생성되었습니다.")
# print(f"체력 {tank2_hp}, 공격력 {tank2_damage}\n")


# def attack(name, location, damage):
#     print(f"{name} : {location} 방향으로 적군을 공격 합니다. [공격력 {damage}]")


# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)


# class Unit:
#     def __init__(self, name, hp, damage):  # 생성자 함수
#         self.name = name  # 멤버변수 ( 클래스 내에서 정의된 변수)
#         self.hp = hp  # 멤버변수
#         self.damage = damage  # 멤버변수
#         print(f"{self.name}유닛이 생성되었습니다.")
#         print(f"체력 {self.hp}, 공격력 {self.damage}\n")


# # marine1 = Unit("마린", 40, 5)
# # marine2 = Unit("마린", 40, 5)
# # tank = Unit("탱크", 150, 35)

# # 레이스 : 공중 유닛, 비행기, 클로킹 ( 상대방에게 보이지 않음 )
# wraith1 = Unit("레이스", 80, 5)
# print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}")

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True  # 확장한 변수는 확장한 객체에서만 적용 (다른 객체에는 적용안됨)

# if wraith2.clocking == True:
#     print(f"{wraith2.name}는 현재 클로킹 상태입니다.")

# from random import *

# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):  # 생성자 함수
#         self.name = name  # 멤버변수 ( 클래스 내에서 정의된 변수)
#         self.hp = hp  # 멤버변수
#         self.speed = speed
#         print(f"{self.name}유닛이 생성되었습니다.")
#         # print(f"체력 {self.hp}, 공격력 {self.damage}\n")

#     def move(self, location):
#         # print("[지상 유닛 이동")
#         print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다")
#         self.hp -= damage
#         print(f"{self.name} : 현재 체력은 {self.hp} 입니다")
#         if self.hp <= 0:
#             print(f"{self.name} : 파괴되었습니다.")


# # 공격 유닛
# class AttachUnit(Unit):  # Unit 클래스 상속
#     def __init__(self, name, hp, speed, damage):  # 생성자 함수
#         Unit.__init__(self, name, hp, speed)  # 상속
#         self.damage = damage  # 멤버변수
#         # print(f"{self.name}유닛이 생성되었습니다.")
#         # print(f"체력 {self.hp}, 공격력 {self.damage}\n")

#     def attach(self, location):
#         print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage} ]")


# # 마린
# class Marine(AttachUnit):
#     def __init__(self):
#         AttachUnit.__init__(self, "마린", 40, 1, 5)

#     # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print(f"{self.name} : 스팀팩을 사용합니다. ( HP 10 감소 )")
#         else:
#             print(f"{self.name} : 체력이 부족하여 스팀팩을 사용하지 않습니다.")


# # 탱크
# class Tank(AttachUnit):
#     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
#     seize_developed = False  # 시즈모드 개발여부

#     def __init__(self):
#         AttachUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return

#         # 현재 시즈모드가 아닐 때 -> 시즈모드
#         if self.seize_mode == False:
#             print(f"{self.name} : 시즈모드로 전환합니다.")
#             self.damage *= 2
#             self.seize_mode = True
#         # 현재 시즈모드 일 때 -> 시즈모드 해제
#         else:
#             print(f"{self.name} : 시즈모드로 해제합니다.")
#             self.damage /= 2
#             self.seize_mode = False


# # 날수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print(f"{name}: {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")


# # 공중 공격 유닛 클래스
# class FlyableAttachUnit(AttachUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttachUnit.__init__(self, name, hp, 0, damage)  # 지상 speed 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         # print("[공중 유닛 이동]")
#         self.fly(self.name, location)


# class Wraith(FlyableAttachUnit):
#     def __init__(self):
#         FlyableAttachUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False  # 클로킹 모드 (해제 상태)

#     def cloking(self):
#         if self.clocked == True:  # 클로킹 모드 -> 모드 해제
#             print(f"{self.name} : 클로킹 모드 해제합니다.")
#             self.clocked = False
#         else:  # 클로킹 모드 해제 -> 모드 설정
#             print(f"{self.name} : 클로킹 모드 설정합니다.")
#             self.clocked = True


# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")


# def game_over():
#     print("Player : gg")  # good game
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")


# # 실제 게임 진행
# game_start()

# # 마린 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()

# # 레이스 1기 생성
# w1 = Wraith()

# # 유닛 일괄 관리
# attach_units = []
# attach_units.append(m1)
# attach_units.append(m2)
# attach_units.append(m3)
# attach_units.append(t1)
# attach_units.append(t2)
# attach_units.append(w1)

# # 전군 이동
# for unit in attach_units:
#     unit.move("1시")

# # 탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# # 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
# for unit in attach_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()

#     if isinstance(unit, Tank):
#         unit.set_seize_mode()

#     if isinstance(unit, Wraith):
#         unit.cloking()

# # 전군 공격
# for unit in attach_units:
#     unit.attach("1시")

# # 전군 피해
# for unit in attach_units:
#     unit.damaged(randint(5, 21))  # 공격은 랜덤으로 받음 (5 ~ 20)

# # 게임종료
# game_over()

# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)
#         self.location = location


# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")


# def game_over():
#     pass


# game_start()
# game_over()

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


# # 메딕 : 의무병

# # 파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttachUnit("파이어뱃", 50, 16)
# firebat1.attach("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송 공격 X

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
# valkyrie = FlyableAttachUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttachUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# ballecruiser = FlyableAttachUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# ballecruiser.move("9시")

########################################### Quiz #8 ###############################################

# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.quit

# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000녀

# [코드]
# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     def show_detail(self):
#         print(
#             self.location,
#             self.house_type,
#             self.deal_type,
#             self.price,
#             self.completion_year,
#         )


# house_list = []
# house_list.append(House("강남", "아파트", "매매", "10억", "2010년"))
# house_list.append(House("마포", "오피스텔", "전세", "5억", "2007년"))
# house_list.append(House("송파", "빌라", "월세", "500/50", "2000년"))
# print(f"총 {len(house_list)}대의 매물이 있습니다.")
# for house in house_list:
#     house.show_detail()

######################################### 예외 처리 #############################################
# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []

#     nums.append(int(input("첫 번째 숫자를 입력하세요. : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요. : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print(f" {nums[0]} / {nums[2]} = {nums[2]}")
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 오류가 발생하였습니다.")
#     print(err)

######################################### 에러 발생시키기 #############################################
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print(f"{num1} / {num2} = {int(num1/num2)}")
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

######################################### 사용자 정의 예외처리  #############################################
######################################### finally  #############################################
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__str(self):
#         return self.msg


# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError(f"입력값: {num1}, {num2}")
#     print(f"{num1} / {num2} = {int(num1/num2)}")
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")

######################################### 퀴즈 #9  #############################################
# Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#         출력 메시지 : "잘못된 값을 입력하였습니다."

# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#         출력 메시지 : "제고가 소진되어 더 이상 주문을 받지 않습니다."

# [코드]


# class SoldOutError(Exception):
#     pass
#     # def __init__(self, msg):
#     #     self.msg = msg

#     # def __str__(msg):
#     #     return msg


# chicken = 10
# waiting = 1  # 홀 안에는 현재 만석. 대기번호 1부터 시작
# while True:
#     try:
#         print(f"[남은 치킨 : {chicken}]")
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken:  # 남은 치킨보다 주문량이 많을 때
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print(f"대기번호 {waiting}] {order} 마리 주문이 완료되었습니다.")
#             waiting += 1
#             chicken -= order
#             if chicken == 0:
#                 raise SoldOutError

#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError:
#         print("재료가 소진되어 더 이상 주문을 받지 않습니다.")
#         break

######################################### Module #############################################

# import theater_module

# theater_module.price(10)
# theater_module.price_morning(5)
# theater_module.price_solider(5)

# import theater_module as mv

# mv.price(10)
# mv.price_morning(5)
# mv.price_solider(5)

# from theater_module import *

# price(10)
# price_morning(5)
# price_solider(5)

# from theater_module import price, price_morning

# price(10)
# price_morning(5)

# from theater_module import price_solider as price

# price(5)

######################################### package #############################################
# import travel.thailand

# # import travel.thailand.ThailandPackage X(클래스를 바로 쓸수 없음)
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage  # from 구분에서는 가능

# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam


# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

######################################### all #############################################
######################################### 모듈 직접 실행 #############################################

# # from random import
# from travel import *  # *은 공개된

# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

######################################### 패키지 모듈 위치 #############################################

# import inspect
# import random
# from travel import *  # *은 공개된

# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

######################################### pip install #############################################
# from bs4 import BeautifulSoup

# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())
######################################### 내장 함수 #############################################
# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print(f"{language}는 아주 좋은 언어입니다.")
# dir : 어떤 객체를 넘겨줬을때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random  # 외장 함수

# print(dir())
# import pickle
# print(dir(random))
# lst = [1, 2, 3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

######################################### 외장 함수 #############################################
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob

# print(glob.glob("*.py"))  # 확장자가 py 인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os

# print(os.getcwd())  # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)  # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())
# import time  # 시간 관련 함수

# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# import datetime

# print("오늘 날짜는 ", datetime.date.today())
# timedelta : 두 날짜 사이의 간격
# today = datetime.date.today()  # 오늘 날짜 저장
# td = datetime.timedelta(days=100)  # 100일 저장
# print("우리가 만난지 100일은", today + td)  # 오늘부터 100일 후

# Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

# 조건 : 모듈 파일명은 byme.py 로 작성

# (모듈 사용 예제)
# import byme
# byme.sign()

# (출력 예제)
# 이 프로그램은 나도코딩에 의해 만들어졌습니다.
# 유튜브 : http://friendmy.naver.com
# 이메일 : friendmy@naver.com

import byme

byme.sign()