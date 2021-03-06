# Entry point of the app
from flask import render_template
from flask_and_db import app

@app.route("/")
def index():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True)