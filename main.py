from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
    return 'Root Directory'

# Can provde URL parameters via type:name
@app.route('/<int:number>/')
def incrementer(number):
    return f'Incremented number is {number+1}'

@app.route('/<string:name>/')
def hello(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8445)
