# 통상적으로 Flask framework를 사용할 때 가장 기본이되는 python파일을 app.py로 명칭한다.
# 변경 가능하나 통상적으로 사용하니 그대로 따라하자.
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

@app.route('/mypage')
def mypage():
   return '<html>Button</html>'

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5001,debug=True)