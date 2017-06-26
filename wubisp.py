from flask import Flask, render_template, request, Response
from flask_cache import Cache
import json
from character import Character

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE':'simple'})

@app.route('/')
def welcome():
    return render_template('wubisp.html')

@app.route('/<c>')
def split(c):
    return render_template('wubisp.html', c=c, title=c+"的图解")

@app.route('/info', methods=['GET'])
def get_info():
    c = request.args.get('c', '')
    v = request.args.get('v', '')
    key = '{}_{}'.format(c, v)
    info = cache.get(key)
    if info is None:
        filename = './rootspider/item/{}.json'.format(key)
        with open(filename, 'r') as f:
            data = json.load(f, object_hook=Character)
            cache.set(key, data)
    else:
        print(info.get_code1())
    resp = Response()
    return resp

@app.route('/img', methods=['GET'])
def get_img():
    c = request.args.get('c', '')
    v = request.args.get('v', '')
    filename = './rootspider/img/{}_{}.gif'.format(c, v)
    image = open(filename, 'rb')
    resp = Response(image, mimetype='image/gif')
    return resp

if __name__ == '__main__':
    app.run()
