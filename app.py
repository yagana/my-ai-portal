from flask import Flask
app = Flask(__name__)  # 이 'app' 변수 이름이 중요합니다!

@app.route("/")
def hello():
    return "Hello! Azure Deployment Success!?????????"

if __name__ == "__main__":
    app.run()
