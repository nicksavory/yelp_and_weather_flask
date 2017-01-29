from flask import Flask, render_template, request
from yelp_api import get_businesses
from weather import get_weather
import os
app = Flask(__name__)

@app.route("/")
def index():
	address = request.values.get('address')
	term = request.values.get('term')
	business = None
	forecast = None

	if address and term:
		business = get_businesses(address, term)
	else:
		business = "Search using the form!"

	if address:
		forecast = get_weather(address)
	else:
		forecast = "Search using the form!"

	return render_template('index.html', business=business, forecast=forecast, address=address)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)