from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Students! Shopping Bill Calculator API is working!"

@app.route("/calculate", methods=["POST"])
def calculate():
 
    data = request.get_json(silent=True)
    
    if not data or "price" not in data or "quantity" not in data:
        return jsonify(error="Missing required fields: 'price' and 'quantity'"), 400
        
    try:
        price = float(data["price"])
        quantity = int(data["quantity"])
        
        # Push 1: Calculate the total bill
        total_bill = price * quantity
        
        return jsonify(
            price=price,
            quantity=quantity,
            total_bill=round(total_bill, 2)
        ), 200
        
    except (ValueError, TypeError):
        return jsonify(error="Invalid data types. 'price' must be a number and 'quantity' must be an integer."), 400

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
