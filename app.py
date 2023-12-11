from flask import Flask, render_template,jsonify,request
from backend import (
    get_suggested_funds,
)
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "https://app.kolortrak.com"}})

@app.route("/",methods=['POST'])
def index():
    fund_codes_to_search = request.get_json()

    suggested_funds_result = get_suggested_funds(
        "static/Funds.xlsx", fund_codes_to_search
    )
    return jsonify(suggested_funds_result)
    # return render_template("index.html", suggested_funds=suggested_funds_result)



if __name__ == "__main__":
    app.run(debug=True)
