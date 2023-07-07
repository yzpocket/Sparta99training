# 크롤링 = 웹페이지에서 어떤 데이터를 가져오는것

import requests
from bs4 import BeautifulSoup

URL = "https://movie.daum.net/ranking/reservation"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# 위 링크 페이지의 전체 HTML이 아웃풋 된다
# print(soup)

# BeautifulSoup 라이브러리는 엄청 많은 HTML 코드 중에 우리가 원하는 특정 부분 을 빠르고 쉽게 필터링 해주는 라이브러리이다.
# Title 데이터가 포함된 코드를 가져와보자
title = soup.select_one('#mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_cont > strong > a')
print(title)
# 그 중에서 텍스트만
print(title.text)
# 혹시나 그 중에서 속성만 가져오고 싶은 경우
# ( ['xxx'] -> dictionary 직접관계없다 bs개발자가 만든 문법이다.)
# print(title['href'])


# 내가원하는 데이터들이 리스트로 나열되어 있었다.
# 1개가 아니라 li를 포함한 전체 리스트들을 가져와보자
# 내가 원하는 값이 있었던 li:nth-child(1)가 아니라 li까지 스코프를 지정하자
titles = soup.select('#mainContent > div > div.box_ranking > ol > li')
print(titles)

# 리스트 중에 반복문으로 
# li 코드 내용 중에 클래스가 a class="link_txt"로 되어있는 태그부분만 가져오자
for li in titles:
    rank = li.select_one('.rank_num').text
    title = li.select_one('.link_txt').text.strip()
    rate = li.select_one('.txt_grade').text.replace(',','')
    
    #텍스트가 내가 원하는 형태가 아닐 경우 가공을 할 수 있다.
    #.strip() 을 붙이면 양쪽 공백 제거 없에줌
    #.replace(',', '') ,와 공백을 없에줌

    # print(title)
    #그 중에 텍스트만 가져오자 -> 위 변수에서 .text로 추출하는 것으로 변경함
    print(rank, title, rate)
