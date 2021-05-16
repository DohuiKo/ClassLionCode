# 문자열 (내장함수)
# 덧셈

str = "멋쟁이사자처럼"
str2 = "은 좋은 동아리입니다."

print(str+str2)

# [x:y] --> x번째 인덱스부터 y인덱스 "전까지"
print(str[0:4]) #멋쟁이사 (0~4)

#문자열의 길이를 구하는 내장함수 : len() -> length의 줄임말
print(len(str)) #문자열의 길이인 7을 반환함

#문자열 내에서 특정 문자의 등장 횟수 : 문자열 변수, count('특정문자')

print(str.count('사'))

str3 = "사사사사사"

print(str3.count('사'))

#문자열을 (특정 기준으로) 나누기 : 문자열 변수.split()

print(str2.split()) #split안에 아무것도 없다면 공백을 기준으로 나눈다.

str4 = "지금,은, split, 함수를, 테스트, 해보려고, 해"

print(str4.split(","))

# 특정 문자 인덱스 찾기 : find('문자'), index('문자')

print(str.find('사')) #3번째 인덱스에 '사'가 있음.
