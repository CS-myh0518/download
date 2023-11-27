from ranking_info import ranking_info
from flask import Flask, render_template

a=ranking_info()
dic111=list()
rank=0
for i in a[0]:
    result = []
    rank+=1
    result.append(str(rank)+'위')
    result.append(i[0])
    dic111.append(result)
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
@app.route("/")
def hello():
    data = dic111   # 딕셔너리  # Break point 찍은 후 디버깅
    return render_template('DaumMovie.html', values=data)    # JSON 형식으로 데이터를 전달

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")