from flask import Flask

app=Flask(__name__)

@app.rout('/')
def index():
    return "hello,world!"

app.run(port='8000')
