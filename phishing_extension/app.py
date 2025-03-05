from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Properly configure CORS to allow all origins (including Chrome extensions)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.route('/')
def home():
    return "Flask server is running!"

@app.route('/detect', methods=['POST', 'OPTIONS'])
def detect_phishing():
    if request.method == "OPTIONS":
        # Handle CORS preflight request
        response = jsonify({"message": "CORS preflight OK"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
        return response, 200

    data = request.get_json()
    email_text = data.get("text", "")

    # Dummy phishing detection logic
    result = "Phishing" if "urgent" in email_text.lower() else "Not Phishing"

    response = jsonify({"message": "Email received", "result": result})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    return response

if __name__ == "__main__":
    app.run(debug=True)
