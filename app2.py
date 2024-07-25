from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/reverse-message')
def reverse_message():
    try:
        # Call the first service
        response = requests.get('http://app1:5001/')
        data = response.json()
        
        # Reverse the message
        reversed_message = data["message"][::-1]
        data["message"] = reversed_message

        return jsonify(data)
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Error accessing the service"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
