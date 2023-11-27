# 나도코딩 파이썬 무료 강의(기본편)
# 0.Intro
# 1-1. 소개
# 1-2. 환경설정

# 2-1. 숫자 자료형
print(5)
print(-10)
print(3.14)

# 2-2. 문자열 자료형
print("풍선")
print('나비')
print("ㅋ"*9)

# 2-3. boolean 자료형
    # 참 / 거짓
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print('true')
print(not False)
print(not (5>10))

# 2-4. 변수
    # 애완동물을 소개해 주세요~
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
hobby = "공놀이"
#print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 ",age,"살이며, " , hobby , "을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))

# 2-5. 주석
# 을 쓰는 방법이 있고
'''을 쓰는 방법이 있다'''

'''아래 여러 문장 선택 후

# print("우리집 " + animal + "의 이름은 " + name + "에요")
# hobby = "공놀이"
# #print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name, "는 ",age,"살이며, " , hobby , "을 아주 좋아해요")
# print(name + "는 어른일까요?" + str(is_adult))

ctrl + / 를 누르면 주석 처리가 가능하다'''

# Quiz) 변수를 이용하여 다음 문장을 출력하시오
'''
변수명 : station
변수값 : "사당", "신도림","인천공항" 순서대로 입력

출력 문장 : XX 행 열차가 들어오고 있습니다
'''
station1 = "사당"
station2 = "신도림"
station3 = "인천공항"

print(station1, "행 열차가 들어오고 있습니다")
print(station2 + "행 열차가 들어오고 있습니다")
print(station3 + "행 열차가 들어오고 있습니다")