from flask import Flask, session, abort, url_for,  request, render_template, redirect
import logdb

app = Flask(__name__)

app.secret_key = b'aaa!111/'

@app.route('/')
def index():
    return '메인 페이지'


@app.route('/login')
def login():
    return render_template('login.html')
        
@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET으로 전송이다'
    else:
        id = request.form['id']
        pw = request.form['pw']
        logdb.insert_data(id,pw)
        
        if id == 'qwer' and pw =='1234':
            session['user'] = id
            return "로그인 성공"
        else:
            return "아이디나 패스워드가 틀렸습니다."

@app.route('/member')
def member():
    info = logdb.select_all()
    return render_template("showlog.html", data=info)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

