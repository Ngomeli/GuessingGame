from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "🎯 Welcome to the Guessing Game! Use /guess?number=your_number"

@app.route('/guess')
def guess():
    try:
        user_guess = int(request.args.get('number', ''))
        number_to_guess = random.randint(1, 10)

        if user_guess == number_to_guess:
            result = "🎉 Correct! You guessed the number!"
        else:
            result = f"❌ Wrong! The number was {number_to_guess}."

        return jsonify({"your_guess": user_guess, "result": result})
    except ValueError:
        return jsonify({"error": "Please provide a valid number between 1 and 10."}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
