from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("Missing OPENAI_API_KEY")
openai.api_key = api_key

@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "OK"}), 200

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(force=True)
    prompt = data.get("prompt", "").strip()
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            timeout=15
        )
        content = resp.choices[0].message.content
        return jsonify({"response": content}), 200

    except openai.error.OpenAIError as oe:
        # more granular failures
        return jsonify({"error": oe.user_message or str(oe)}), 502
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
