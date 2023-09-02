# import files
from flask import Flask, render_template, request
import chatbot as chtbt

app = Flask(__name__)




@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chtbt.query(userText))


if __name__ == "__main__":
    app.run()