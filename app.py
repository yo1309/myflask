



from flask import Flask, url_for,  request, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return '메인 페이지'

@app.route('/hello/')
def hello():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hellovar(name):
    return 'Hello, {}!'.format(name)
    
@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        return '도라에몽'
    elif num == 2:
        return '진구'
    elif num == 3:
        return '퉁퉁이'
    else:
        return '없음'
    # return 'Hello, {}!'.format(num)

@app.route('/naver')
def naver():
    return render_template("naver.html")

@app.route('/kakao')
def daum():
    return redirect("https://www.daum.net/")
if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('naver'))
    app.run(debug=True)

@app.route('/url_test')
def url_test():
    return redirect("https://www.daum.net")







@app.route('/form')
def form():
    return render_template('test.html')
        
@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET으로 전송이다'
    else:
        num = request.form['num']
        name = request.form['name']
        print(num, name)
        with open("static/save.txt")
        return 'POST이다.학번은 {} 이름은 {}이다'.format(num, name)




@app.route('/login')
def login():
    return render_template('login.html')
        
@app.route('/way', methods=['GET', 'POST'])
def way():
    if request.method == 'POST':
        p_id = request.form['id']
        p_pw = request.form['pw']
        print(p_id, p_pw)
        if(p_id == 'abc' and p_pw == '1234'):
            return '로그인 성공[post]'
        else:
            return '로그인 실패'


