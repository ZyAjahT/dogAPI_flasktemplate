from flask import Flask, render_template
import requests
import logging
app = Flask(__name__)

@app.route("/")
def home():
    try:
        URL = "https://dogapi.dog/api/v2/breeds"
        response = requests.get(url = URL)
        if(response.status_code != 200):
            raise ValueError(f"Error connecting to Home Page. Please check back later.")
        respArray = []
        for x in range(2):
            respArray.append(response.json())
        return render_template("index.html", dataArray = respArray)
    except ValueError as e: 
        logging.error(f"ValueError with home: {e}")
        return render_template("errorPage.html", errorMessage = e)


if __name__ == "__main__":
    app.run(debug=True) 