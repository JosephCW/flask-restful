from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
    return 'Root Directory'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8445)
