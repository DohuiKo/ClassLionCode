#딕셔너리 (내장함수)

pairs = {'잔나비' : '뜨거운 여름밤은 가고 남은 건 볼품없지만', '소히':'산책', '홍크':'어쩌면'}

#하나의 키-Value 쌍을 추가하는 방법
#딕셔너리형 변수[키] = value

print(pairs)

pairs['스탠딩 에그'] = '휴식'

print(pairs)

#특정 키-Value 삭제하는 방법 : del 함수
#del 변수[키]

del pairs['잔나비']

print(pairs)

#key로 value 얻기 : 변수.get(키)
#딕셔너리에서 중요한건 찾고자 하는 데이터를 대응을 통해서 찾음

v = pairs.get('잔나비')

print(v)