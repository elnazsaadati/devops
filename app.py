from flask import Flask

app = Flask(__name__)
@app.route("/<name>")
def index(name):
    return f"hello {name}"
if __name__=="__main__":
       app.run(host="0.0.0.0", port=5000)

