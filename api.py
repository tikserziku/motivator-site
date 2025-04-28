import os
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route("/bot/status", methods=["GET"])
def bot_status():
    return jsonify({
        "status": "бот активен",
        "datetime": datetime.utcnow().isoformat() + "Z",
        "version": "0.1.0"
    })

@app.route("/bot/game", methods=["GET"])
def bot_game():
    # Здесь далее будет игра или генерация фразы
    return jsonify({
        "game": "plug",
        "phrase": "Сегодня твой день для маленькой победы! 💥"
    })

@app.route("/bot/webhook", methods=["POST"])
def bot_webhook():
    # Пока просто принимаем и печатаем входящее сообщение из Telegram
    data = request.json
    print("Получено сообщение из Telegram:", data)
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

