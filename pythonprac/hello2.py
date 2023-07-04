# requests 라이브러리 설치 필요
# requests 라이브러리 임포트
import requests 

# requests.get 사용
r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')

#rjson 변수에 데이터 담기
rjson = r.json()

# print(rjson['RealtimeCityAir']['row'])
# rows에 Dictionary 형태로 담기
rows = rjson['RealtimeCityAir']['row']

# 반복문으로 gu_name, gu_mise로 원하는 데이터 넣기
for a in rows:
    # print(a)
    gu_name = a['MSRSTE_NM']
    gu_mise = a['IDEX_MVL']
    # 원하는 정보만 출력하기
    print(gu_name, gu_mise)