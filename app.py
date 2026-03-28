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


@app.route("/balance", methods=["GET"])
def get_balance():
    return jsonify(account)


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


if __name__ == "__main__":
    app.run(debug=True)