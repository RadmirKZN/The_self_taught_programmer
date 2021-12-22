from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    return "Dirty sanchez!"
app.run (port='8000')