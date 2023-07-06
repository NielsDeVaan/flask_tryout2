from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<p>Hoop dat ik het zo snel mogelijk haal!</p>"

if __name__ == '__main__':
    app.run(port=5000, debug=True)