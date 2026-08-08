from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

BOT_TOKEN = "8674475412:AAEOQaKu4DkhjZpOag4E9ZtoH6669wxu5ho"
CHAT_ID = "5382570966"


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}

    name = data.get("name", "Noma'lum")
    email = data.get("email", "Noma'lum")

    message_text = (
        f"📝 <b>YANGI RO'YXATDAN O'TISH</b>\n\n"
        f"👤 <b>Name:</b> {name}\n"
        f"✉️ <b>Email:</b> {email}"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message_text, "parse_mode": "HTML"}

    try:
        response = requests.post(url, json=payload, timeout=10)
        res_data = response.json()

        if res_data.get("ok"):
            return (
                jsonify(
                    {
                        "status": "success",
                        "message": "Ro'yxatdan muvaffaqiyatli o'tdingiz!",
                    }
                ),
                200,
            )
        else:
            return (
                jsonify(
                    {"status": "error", "message": res_data.get("description")}
                ),
                400,
            )
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)