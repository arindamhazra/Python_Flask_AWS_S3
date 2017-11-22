from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object("base_config")

@app.route("/")
def home():
    return render_template("index.html")

app.run()
