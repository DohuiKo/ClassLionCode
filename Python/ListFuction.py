#리스트 (내장함수)

li = [3,1,4,5,2]

print(li)

#리스트 원소 오름차순 정렬해주는 변수 : 변수.sort()
li.sort()

print(li)

#인덱스 슬라이싱
print(li[0:2])

#리스트의 길이를 구해주는 함수 : len(변수)

print(len(li))

#리스트 내의 특정 원소 인덱스를 반환해주는 함수 .index()

print(li.index(3))

#리스트 내의 특정 원소의 갯수 세기 : .count(요소)

li2 = ["움칫", "움칫", "둠칫", 2,2,2]

print(li2.count("움칫"))