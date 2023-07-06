#dbprac3_1_movie_insert 에서 실행한 웹크롤링+DB넣기로 생성된 DB의 데이터들을
#가져오고
#수정하자

# Python과 DB를 연결하는 코드(공통)
from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://ohnyong:test@cluster0.lu7mz8j.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

#[1] 가져온다 == Find를 사용하자
# "영화 제목 '아저씨'의 순위를 가져오자"

# READ(FIND_ONE)
# 한 개 찾기 - 예시
movie = db.movies2.find_one({'title':'아저씨'})
print(movie)
#그 중에서 순위(rank) 가져오기.
print(movie['rank'])

# READ(FIND)
# 우선 조건 기준을 삼으려는 _1개의 데이터_를 찾는다.
movie = db.movies2.find_one({'title':'하모니'})
print(movie)
# '하모니' 영화의 연령제한이 기준점이 되고 'age'라는 변수에 담는다.
age = movie['age']
print(age)
# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# 'age'가 위 movie'하모니'의 age값인 조건 추가하여
# list()로 movies라는 객체 생성
movies = list(db.movies2.find({'age':age},{'_id':False}))
# 객체기 때문에 
for m in movies:
    print(m)
