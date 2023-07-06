# 웹 크롤링을 위한 requests, bs4 Import
import requests
from bs4 import BeautifulSoup

# Python과 DB를 연결하는 코드(공통)
from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://ohnyong:test@cluster0.lu7mz8j.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

# 웹 크롤링 구현
URL = "https://movie.daum.net/ranking/boxoffice/yearly?date=2010"
    # user agent는 HTTP 요청을 보내는 디바이스와 브라우저 등 사용자 소프트웨어의 식별 정보를 담고 있는 request header의 한 종류이다.
    # 임의로 수정될 수 없는 값이고, 보통 HTTP 요청 에러가 발생했을 때 요청을 보낸 사용자 환경을 알아보기 위해 사용한다.
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# URL로부터 requests.get으로 HTML 소스를 data에 담는다
data = requests.get(URL, headers=headers)
# BeautifulSoup으로 data(html 소스)를 soup에 담는다(bs의 기능을 기능을 이용하기 위해)
soup = BeautifulSoup(data.text, 'html.parser')

# soup에 담긴 data중에 list_movieranking > li 에 속한 요소들을 lis에 담는다
lis = soup.select(".list_movieranking > li")
# for in 반복문은 객체에 주로 사용합니다.
# 즉, 객체 자료형에 자료들을 하나씩 꺼내고 싶을때 사용
# 	//key를 받는 변수명은 임의변경 가능
#   //in 객체명
#   for (key in book) {
#     console.log(key, book[key]);
#   }
# 객체에 사용 할수 있습니다.
# 객체의 key값과 value 값을 뽑아내는데 유용합니다.
# 객체의 키값의 갯수만큼 반복하여 첫번쨰키값부터 마지막 키값까지 반복합니다.

# 1] lis 객체에서 li라고 명칭한 변수에 다음을 반복 실행한다 객체의 마지막 키값까지.
for li in lis:
# 2] rank, age, title 변수에 li중 .rank_num, .ico_see, .link_txt 값을 담는다
    rank = li.select_one(".rank_num").text
    age = li.select_one(".ico_see").text
    title = li.select_one(".link_txt").text
    print(rank, title, age)

# 3] 위 변수를 doc에 rank, title, age key값의 각각 value로 넣는다.
    doc = {
        'rank': rank,
        'title': title,
        'age': age
    }
# 4] movies2라는 collection에 doc에 담긴 데이터를 document로 insert 한다.
    db.movies2.insert_one(doc)
