from flask import Flask, jsonify, request

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

@app.route('/person/')
def person():
    # jsonify wraps json.dumps() and makes it a response object
    #  that is application/json type
    return jsonify({
        'name': 'Joey',
        'age': '23'
    })

# by omitting the trailing '/', you get 404 if / is provided
#  but accessing '/person' would redirect to /person/
@app.route('/numbers')
def numbers():
    return jsonify([
        1, 2, 3, 5, 9, 25
    ])

@app.route('/teapot/')
def teapot():
    # Tuple stating the return code.
    return 'Would you like some tea?', 418

@app.before_request
def before():
    print('This will happen before every request.')

@app.after_request
def after():
    print('This will happen after every request.')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8445)
