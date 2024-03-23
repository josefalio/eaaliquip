from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def home():
    response = make_response("Hello, World!")
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    return response

if __name__ == '__main__':
    app.run()
