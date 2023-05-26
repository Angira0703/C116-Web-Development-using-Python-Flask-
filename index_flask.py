from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")

def first_webpage():

    heading = "Eloquent Soul"

    return render_template("index.html", heading_name=heading)

app.run(debug = True)
