from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello, world"

@app.get("/say-hello")
def say_hello():
    return "Say Hello!"