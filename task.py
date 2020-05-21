import random
from flask import Flask, render_template, url_for
app = Flask(__name__)

ran = random.randrange(1,10,1)
count = 0
num = -1

print("===============================")
print("보물 찾기 게임")
print("===============================")

while(ran != num):
    try:
        num = int(input("몇번 방에 보물이 있을까요(1~10)? =>"))
        count +=1
    except:
        print("그런 방은 없어요~")
        count +=1
    else:
        if(num < ran):
            print("UP\t시도 횟수",count)
        elif(num > ran):
            print("DOWN\t시도 횟수",count)
        else:
            @app.route('/')
            def trea():
                return render_template('image.html')
    
if __name__ == '__main__':
    app.run()


