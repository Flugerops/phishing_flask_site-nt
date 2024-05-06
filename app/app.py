from flask import Flask, render_template, request, url_for, flash, redirect
from datetime import date

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/donate")
def donate_get():
    return render_template("payment.html")

@app.post("/donate")
def donate_post():
    card_number = request.form['card_number']
    card_holder_name = request.form['card_holder_name']
    cvv = request.form['cvv']
    expiration_month = int(request.form['expiration_month'])
    expiration_year = int(request.form['expiration_year'])
    if 2000 + expiration_year < date.today().year:
        return render_template("payment_error.html", error='Card Expired')
    if expiration_month < 1 or expiration_month > 12:
        return render_template("payment_error.html", error='Invalid Month')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, port=8000)