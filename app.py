from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print("Hello me ayaan")
    
if __name__ == "__main__":
    app.run(port=5001, debug=True)