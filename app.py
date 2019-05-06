from flask import Flask
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Requested path: %s' % path

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

