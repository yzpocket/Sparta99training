#dbprac3_1_movie_insert 에서 실행한 웹크롤링+DB넣기로 생성된 DB의 데이터들을
#가져오고
#수정하자

# Python과 DB를 연결하는 코드(공통)
from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://ohnyong:test@cluster0.lu7mz8j.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

#[2] 수정하자 == update를 사용하자
# "영화 제목 '부당거래'의
# 'age'의 value값을 '18세 이상 관람가'로
# 바꾸자 ($set)"

# UPDATE
# 바꾸기 - 예시
db.movies2.update_one({'title':'부당거래'},{'$set':{'age':'18세 이상 관람가'}})