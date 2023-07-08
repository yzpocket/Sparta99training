# 통상적으로 Flask framework를 사용할 때 가장 기본이되는 python파일을 app.py로 명칭한다.
# 변경 가능하나 통상적으로 사용하니 그대로 따라하자.
# render_template 를 추가로 임포트 했다.
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

@app.route('/mypage')
def mypage():
# render_template를 임포트한 뒤 다음처럼 root/templates/ 폴더 내 html을 가져올 수 있다.
   return render_template('index.html')

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5001,debug=True)