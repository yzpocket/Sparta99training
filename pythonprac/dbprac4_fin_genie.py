#웹 크롤링 하기 실습
#URL = https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20230101
#순위 / 곡 제목 / 가수
#를 가져오자.

# 크롤링 = 웹페이지에서 어떤 데이터를 가져오는것

import requests
from bs4 import BeautifulSoup

URL = "https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20230601"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# 위 링크 페이지의 전체 HTML이 아웃풋 된다
# print(soup)

# BeautifulSoup 라이브러리는 엄청 많은 HTML 코드 중에 우리가 원하는 특정 부분 을 빠르고 쉽게 필터링 해주는 라이브러리이다.
# Title 데이터가 포함된 코드를 가져와보자

# 데이터는 td에 있고 상위 계층인 tr은 "곡"을 말한다. tr"들" 전체를 trs라고 변수에 담는다.
trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

# 반복문으로 trs를 돌면서 [rank, title, singer 변수를 {tr}에 담고, 출력한 후 <다음 trs>로 넘어간다.] 를 반복(어디까지? trs 리스트의 끝까지==0부터 전체)

# 1싸이클 해석:
# tr 변수에 trs 첫번째 인덱스 = soup으로 받은 trs의 첫번째[0] <tr>데이터가 들어감
for tr in trs:
# 그 tr.select_one으로 순위 텍스트가 있는 곳인 td.number로 가서
# 텍스트를 0~2까지 자르고, 양옆 공백을 제거(strip)한 텍스트를
# rank변수에 담는다.
    rank = tr.select_one('td.number').text[0:2].strip()
# title 동일, singer 동일
    title = tr.select_one('td.info > a.title.ellipsis').text.strip()
    singer = tr.select_one('td.info > a.artist.ellipsis').text.strip()
# rank변수에 담긴것, + /구분선, title+ /, singer를 출력.
    print(rank+" / ", title+" / ", singer)
# 하고 반복문 맨 위로 다시오면 trs에 담긴 다음 인덱스[1] <tr>데이터(두번째곡)가 들어감

