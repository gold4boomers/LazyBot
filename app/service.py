from bottle import Bottle

app = Bottle()

@app.get('/')
def hello():
    return "Hello!"

app.run(host="localhost", port=8080)