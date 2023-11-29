#4-1 문자열

sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = ''' 
나는 소년이고,
파이썬은 쉬워요
'''
print(sentence3)

#4-2 슬라이싱

jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2 전까지
print("월 : " + jumin[2:4]) 
print("일 : " + jumin[4:6]) 
print("생년월일 : " + jumin[:6])  # 처음부터 6 전까지
print("뒤 일곱자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 일곱자리(뒤에서부터) : " + jumin[-7:]) # 뒤에서 7번째부터 끝까지

# 4-3 문자열 처리함수

python = "Python is amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)

print(python.find("n"))
print(python.find("Java")) # 없으면 -1로 나옴
# print(python.index("Java")) : 없으면 오류가 남

print(python.count("n"))

#4-4 문자열 포맷

print("a"+"b")
print("a","b")

# 방법 1

print("나는 %d살입니다" %20) # %d에서 d는 정수값만 가능하다
print("나는 %s을 좋아해요" % "파이썬") # %s에서 s는 문자열도 숫자도 가능하다
print("Apple 은 %c로 시작해요" % "A") # %c에서 c는 한 글자만 받겠다는 뜻

# %s
print("나는 %s살입니다." %20)
print("나는 %s색과 %s색을 좋아해요" % ("파란","빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간","노란"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age = 20 ))

# 방법 4
age = 20
color = "빨간"

print(f"나는 {age}살이며, {color}색을 좋아해요.")


#4-5 탈출문자

'''
print("백문이 불여일견 
      백견이 불여일타")''' #오류가 난다

# \n 활용
print("백문이 불여일견\n백견이 불여일타")

# 저는 "나도코딩"입니다
'''print("저는 "나도코딩"입니다.")''' # 오류가 난다
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print('저는 \'나도코딩\'입니다.')

# \\ : 문장 내에서 \
print("C:\\Users\\hyejo\\Desktop\\python workspace>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")
print("Red apple\rPine")
print("apple\rPine")

# \b : 백스페이스 (한글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

'''
Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 수 + 글자 내 'e' 개수+ "!"로 구성
                  (naver)          (5)           (1)           (!)
예) 생성된 비밀번호 : nav51!
'''

url = "http://youtube.com"
url2 = url.replace("http://","") # 규칙1
print(url2)

url3 = url2[:url2.index(".")] # url2[0:5]
print(url3)

password = url3[0:3]  + str(len(url3)) + str(url3.count("e"))+"!"
print(password)
print("{0}의 비밀번호는 {1}입니다.".format(url,password))