import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    rows = db.execute("SELECT symbol, SUM(shares) AS [shares] FROM stocks WHERE stocks_id=? GROUP BY symbol", session["user_id"])
    price = [float(lookup(row['symbol'])['price']) for row in rows]
    rows_and_prices = zip(rows, price)
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    total = 0
    for i,row in rows:
        print(i)

    total = total + cash[0]['cash']
    return render_template("index.html", rows_and_prices = rows_and_prices, cash = cash[0]['cash'], total = total)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        user_id = session["user_id"]
        name = request.form.get("symbol")
        if not name:
            return apology("Missing name")
        shares = request.form.get("shares")
        if not shares or int(shares) <= 0:
            return apology("invalid share")
        try:
            result = lookup(name)
            price = result["price"]
            symbol = result["symbol"]
        except:
            return apology("Invalid symbol")
        row = db.execute("SELECT cash FROM users WHERE id = (?)", user_id)
        cash = row[0]["cash"]
        cash = int(cash) - int(price)
        if int(cash) < 0:
            return apology("Sorry not enough cash")
        db.execute("INSERT INTO stocks (stocks_id, symbol, shares) VALUES (?, ?, ?)", user_id, symbol, shares)
        db.execute("UPDATE users SET cash = ? WHERE id=?", cash, user_id)
        return redirect("/")
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        name = request.form.get("symbol")
        try:
            result = lookup(name)
            price = result["price"]
            symbol = result["symbol"]
        except:
            return apology("Invalid symbol")
        return render_template("quoted.html", symbol = symbol, price = price)
    else:
        return render_template("/quote.html")
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        reg_username = request.form.get("reg_username")
        reg_password = request.form.get("reg_password")
        confirmation = request.form.get("confirmation")
        if not reg_username:
            return apology("must provide username", 403)
        elif not reg_password:
            return apology("must provide password", 403)
        elif not confirmation:
            return apology("must provide confirmation", 403)
        elif confirmation != reg_password:
            return apology("password and confirmation does not match", 403)
        hash_password = generate_password_hash(reg_password, method='pbkdf2', salt_length=16)
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", reg_username, hash_password)
        except ValueError:
            return apology("username is taken")
        return render_template("login.html")

    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")
