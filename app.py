from flask import Flask, request, jsonify, render_template
from search import search

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search_route():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Query missing"}), 400
    results = search(query)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)

