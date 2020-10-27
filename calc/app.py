from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# http://127.0.0.1:5000/add?a=1&b=2

@app.route("/add")
def get_sum():
    a = request.args["a"]
    b = request.args["b"]

    return f"<h1>Sum: {add(int(a),int(b))}</h1>"

@app.route("/sub")
def get_difference():
    a = request.args["a"]
    b = request.args["b"]

    return f"<h1>Difference: {sub(int(a),int(b))}</h1>"

@app.route("/mult")
def get_product():
    a = request.args["a"]
    b = request.args["b"]

    return f"<h1>Product: {mult(int(a),int(b))}</h1>"

@app.route("/div")
def get_quotient():
    a = request.args["a"]
    b = request.args["b"]

    return f"<h1>Quotient: {div(int(a),int(b))}</h1>"

#Part 2

OPERATIONS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

# http://127.0.0.1:5000/math/add?a=1&b=2
    
@app.route('/math/<operation>')
def math_operation(operation):
    a = request.args["a"]
    b = request.args["b"]
    result = OPERATIONS[operation](int(a), int(b))
    
    return f"""
        <h1>
        Values a: {a} b: {b} <br>Produced the result of: {result} <br>Using the {operation.capitalize()} operation</h1>
        """
