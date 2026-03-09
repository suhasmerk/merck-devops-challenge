from flask import Flask, jsonify, request

app = Flask(__name__)

# Simple hardcoded API Key for the challenge
API_KEY = "merck-secret-123"

def require_auth(f):
    def wrapper(*args, **kwargs):
        if request.headers.get("X-API-KEY") != API_KEY:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200 [cite: 10]

@app.route('/data', methods=['GET'])
@require_auth
def get_data():
    dummy_data = {"id": 1, "message": "Hello from the DevOps Challenge!"}
    return jsonify(dummy_data), 200 [cite: 10]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)