



from flask import Flask, url_for,  request, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return '메인 페이지'


@app.route('/form')
def form():
    return render_template('login.html')
        
@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET으로 전송이다'
    else:
        num = request.form['num']
        name = request.form['name']
        print(num, name)
        with open("static/save.txt","w",encoding='utf-8') as f:
            f.write("%s,%s" % (num, name))
        return 'POST이다.학번은 {} 이름은 {}이다'.format(num, name)

@app.route('/getinfo')
def getinfo():
    with open("static/save.txt", "r",encoding='utf-8') as file:
        student = file.read().split(',')
    return '번호:{}, 이름:{}'.format(student[0], student[1])
    


if __name__ == '__main__':
    app.run(debug=True)

