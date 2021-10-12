# Build a simple calculator with Flask, which uses URL query parameters to get the numbers to calculate with.
# Make a Flask app that responds to 4 different routes. Each route does a math operation with two numbers, a and b, which will be passed in as URL GET-style query parameters.

# /add
# Adds a and b and returns result as the body.
# /sub
# Same, subtracting b from a.
# /mult
# Same, multiplying a and b.
# /div
# Same, dividing a by b.
# For example, a URL like http://localhost:5000/add?a=10&b=20 should return a string response of exactly 30.

# Write the routes for this but don’t hardcode the math operation in your route function directly. Instead, we’ve provided helper functions for this in the file operations.py:


# Put your app in here.
from flask import Flask, request
from operations import add, sub, div, mult

app = Flask(__name__)

@app.route("/add")
def addition():
    """Add a and b parameters"""
    # a = int(request.args.get("a"))
    # b = int(request.args.get("b"))
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a, b)
    return str(result)

@app.route("/sub")
def subtract():
    """Subtract b from a parameter"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a, b)
    return str(result)


@app.route("/mult")
def multiply():
    """multiply a from b parameter"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a, b)
    return str(result)

@app.route("/div")
def divide():
    """divide a by b parameter"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a, b)
    return str(result)


# PART TWO
# MAKING A SINGLE ROUTE
operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)
    return str(result)
