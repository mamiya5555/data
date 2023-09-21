from flask import Flask


app = Flask(__name__)

@app.route('/',methods=['get'])
def index():
    return '200'


@app.route('/user',methods=['get'])
def index():
    return {'user': 'kheang','email': 'test@gmail.com'}


if __name__ == '__main__':
    app.run(debug=True)