from flask import Flask, request, jsonify
from main import Account # Import the Account class from main.py

app = Flask(__name__)

account = Account("John Doe", 1000) # Create an instance of the Account class with initial balance

@app.route("/")
def home():
    return "Banking API is running"

# Endpoint to get the current balance
@app.route("/balance", methods=["GET"])
def get_balance():
    return jsonify({
        "balance": account.check_balance()
    })

# Endpoint to get account details
@app.route("/account", methods=["GET"])
def get_account():
    return jsonify({
        "name": account.name,
        "balance": account.balance
    })


# Endpoint to deposit money into the account
@app.route("/deposit", methods=["POST"])
def deposit():
    data = request.get_json()

    if not data or "amount" not in data:
        return jsonify({"error": "Amount is required"}), 400

    try:
        amount = float(data["amount"])
    except (TypeError, ValueError):
        return jsonify({"error": "Amount must be a number"}), 400

    result = account.deposit(amount)

    if isinstance(result, str):  # error message from class
        return jsonify({"error": result}), 400

    return jsonify({
        "message": "Deposit successful",
        "new_balance": result
    })

# Improved withdraw endpoint with better validation and error handling
@app.route("/withdraw", methods=["POST"])
def withdraw():
    data = request.get_json()

    if not data or "amount" not in data:
        return jsonify({"error": "Amount is required"}), 400

    try:
        amount = float(data["amount"])
    except (TypeError, ValueError):
        return jsonify({"error": "Amount must be a number"}), 400

    result = account.withdraw(amount)

    if isinstance(result, str):
        return jsonify({"error": result}), 400

    return jsonify({
        "status": "success",
        "message": "Withdrawal successful",
        "data": {
            "balance": result
        }
    })

if __name__ == "__main__":
    app.run(debug=True)