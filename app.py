from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple in-memory storage
account = {
    "name": "John Doe",
    "balance": 1000
}

@app.route("/")
def home():
    return "Banking API is running"

# Endpoint to get the current balance
@app.route("/balance", methods=["GET"])
def get_balance():
    return jsonify(account)

# Endpoint to get account details
@app.route("/account", methods=["GET"])
def get_account():
    return jsonify({
        "name": account["name"],
        "balance": account["balance"]
    })

# Endpoint to deposit money into the account
@app.route("/deposit", methods=["POST"])
def deposit():
    data = request.get_json()
    amount = data.get("amount")

    if amount is None or amount <= 0:
        return jsonify({"error": "Invalid amount"}), 400

    account["balance"] += amount
    return jsonify({
        "message": "Deposit successful",
        "new_balance": account["balance"]
    })


# Initial withdraw endpoint with basic validation and error handling
'''
@app.route("/withdraw", methods=["POST"])
def withdraw():
    data = request.get_json()
    amount = data.get("amount")

    if amount is None or amount <= 0:
        return jsonify({"error": "Invalid amount"}), 400

    if amount > account["balance"]:
        return jsonify({"error": "Insufficient funds"}), 400

    account["balance"] -= amount
    return jsonify({
        "message": "Withdrawal successful",
        "new_balance": account["balance"]
    })
'''

# Improved withdraw endpoint with better validation and error handling
@app.route("/withdraw", methods=["POST"])
def withdraw():
    data = request.get_json()

    #validate input if amount is present and is a number
    if not data or "amount" not in data:
        return jsonify({
            "status": "Error",
            "message": "Amount is required"
        }), 400

    try:
        amount = float(data["amount"])
    except (TypeError, ValueError):
        return jsonify({
            "status": "Error",
            "message": "Amount must be a number"
        }), 400

    # Validate that the amount is positive
    if amount <= 0:
        return jsonify({
            "status": "Error",
            "message": "Invalid amount"
        }), 400

    # Validate that the account has sufficient funds
    if amount > account["balance"]:
        return jsonify({
            "status": "Error",
            "message": "Insufficient funds"
        }), 400

    account["balance"] -= amount

    # Return a success response with the updated balance
    return jsonify({
        "status": "Success",
        "message": "Withdrawal successful",
        "data": {
            "balance": account["balance"]
        }
    })

if __name__ == "__main__":
    app.run(debug=True)