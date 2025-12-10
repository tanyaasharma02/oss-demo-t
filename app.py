from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from the 1.0.1 container version!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

