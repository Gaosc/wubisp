from flask import Flask, render_template, Response
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('wubisp.html')

@app.route('/<c>')
def split(c):
    return render_template('wubisp.html', c=c, title=c+"的图解")

@app.route('/img/<c>')
def getimg(c):
    filename = "./rootspider/img/{}_86.gif".format(c)
    print(filename)
    image = open(filename, 'rb')
    resp = Response(image, mimetype="image/gif")
    return resp

if __name__ == '__main__':
    app.run(debug=True)