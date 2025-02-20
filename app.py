from flask import Flask, render_template
import requests
import logging
app = Flask(__name__)

@app.route("/")
def home():
    try:
        URL = "https://dogapi.dog/api-docs/v2/swagger.json"
        response = requests.get(url = URL)
        if(response.status_code != 200):
            raise ValueError(f"Error connecting to Dog API. Check back later.")
        return render_template("index.html", data = response.json())
    except ValueError as e:
        logging.error(f"ValueError with home: {e}")
        return render_template("errorPage.html", errorMessage = e)
    
if __name__=="__main__":
    app.run(debug=True)