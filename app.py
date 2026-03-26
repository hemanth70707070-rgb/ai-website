from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI()

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI that creates video prompts."},
            {"role": "user", "content": user_input}
        ]
    )

    return jsonify({
        "reply": response.choices[0].message.content
    })

app.run(host="0.0.0.0", port=10000)
