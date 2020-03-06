from flask import Flask, render_template, url_for, request
import re
from function import translator


app = Flask(__name__)

@app.route('/')
def index():
	return render_template("translator.html")


@app.route('/translator', methods=['POST'])
def process():
	if request.method == 'POST':
		raw_text = request.form['rawtext']
		results = translator.translate(raw_text)

	return render_template("translator.html", results=results,raw_text=raw_text)


if __name__ == '__main__':
	app.run(debug=True)	