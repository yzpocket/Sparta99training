# 통상적으로 Flask framework를 사용할 때 가장 기본이되는 python파일을 app.py로 명칭한다.
# 변경 가능하나 통상적으로 사용하니 그대로 따라하자.
# render_template 를 추가로 임포트 했다.
# request를 추가로 임포트 했다.
# jsonify를 추가로 임포트 했다.
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
# render_template를 임포트한 뒤 다음처럼 root/templates/ 폴더 내 html을 가져올 수 있다.
   return render_template('index.html')

# get 방식 요청 예시
# @app.route('/test', methods=['GET'])
# def test_get():
# #    title_give라는 데이터가 있으면 title_receive에 넣는다.
#    title_receive = request.args.get('title_give')
# #    title_receive를 출력해보자.
#    print(title_receive)
#    return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

# post 방식 요청 예시(데이터 흐름은 index.html [1]부터 시작해서 보기)
# [4] 객체 formData가 이곳에 도착하고 
@app.route('/test', methods=['POST'])
# [5] test_post()가 실행된다
def test_post():
# [6] request.form에 따라 key값이 title_give인 value("블랙팬서")이 title_receive로 담아지고
   title_receive = request.form['title_give']
# [7] title_receive가 출력된다. (블랙팬서)   
   print(title_receive)
# [8] 출력까지 메서드 수행이 완료되었으니 jsonify로 dictionary 형태의 아래 {'key1':'value1', 'key2':'value2'}를 json 형태로 반환된다. [응답]
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5001,debug=True)