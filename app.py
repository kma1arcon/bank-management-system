from flask import Flask, request, jsonify
from main import Account # Import the Account class from main.py

app = Flask(__name__)

# In-memory storage for accounts (for demonstration purposes)
accounts = {}

@app.route("/")
def home():
    return "Banking API is running"

# Endpoint to create a new account
@app.route("/create-account", methods=["POST"])
def create_account():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    account_id = str(len(accounts) + 1)

    accounts[account_id] = Account(data["name"], 0)

    return jsonify({
        "message": "Account created",
        "account_id": account_id
    })

# Endpoint to get account details by ID
@app.route("/accounts/<account_id>", methods=["GET"])
def get_account(account_id):
    account = accounts.get(account_id)

    if not account:
        return jsonify({"error": "Account not found"}), 404

    return jsonify({
        "name": account.name,
        "balance": account.balance
    })

# Endpoint to deposit money into the account by AccountID
@app.route("/accounts/<account_id>/deposit", methods=["POST"])
def deposit(account_id):
    account = accounts.get(account_id)

    if not account:
        return jsonify({"error": "Account not found"}), 404

    data = request.get_json()

    if not data or "amount" not in data:
        return jsonify({"error": "Amount is required"}), 400

    try:
        amount = float(data["amount"])
    except:
        return jsonify({"error": "Invalid amount"}), 400

    result = account.deposit(amount)

    if isinstance(result, str):
        return jsonify({"error": result}), 400

    return jsonify({
        "message": "Deposit successful",
        "balance": result
    })


# Endpoint to withdraw money from the account by AccountID
@app.route("/accounts/<account_id>/withdraw", methods=["POST"])
def withdraw(account_id):

    account = accounts.get(account_id)

    if not account:
        return jsonify({"error": "Account not found"}), 404

    data = request.get_json()

    if not data or "amount" not in data:
        return jsonify({"error": "Amount is required"}), 400

    try:
        amount = float(data["amount"])
    except:
        return jsonify({"error": "Invalid amount"}), 400

    result = account.withraw(amount)

    if isinstance(result, str):
        return jsonify({"error": result}), 400

    return jsonify({
        "message": "Withdrawal successful",
        "balance": result
    })

if __name__ == "__main__":
    app.run(debug=True)