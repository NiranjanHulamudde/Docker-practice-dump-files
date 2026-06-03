from flask import Flask
app = Flask(app)

@app.route('/')
def hello():
    return "Hello from python world!"

if app == '__main__':
    app.run(host='0.0.0.0', port=5000)
