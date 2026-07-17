from flask import Flask, redirect
from pymongo import MongoClient
import os

app = Flask(__name__)
client = MongoClient(os.environ["MONGO_URI"])
db = client["Cluster0"]
settings_col = db["settings"]

@app.route("/f/<code>")
def forward(code):
    doc = settings_col.find_one({"_id": "config"})
    active_bot = doc["active_bot"] if doc else "roxyrobot"
    return redirect(f"https://t.me/{active_bot}?start={code}", code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
