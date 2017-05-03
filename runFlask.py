from flask import Flask, render_template, redirect, flash, request
import os
import leagReq

app = Flask(__name__)
if 1 == 1:
	app.secret_key = "joba"
else:
	app.secret_key = os.environ.get('secret',-1)

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
			flash(username('VinnyDaGod'))
	return render_template("index.html")

def username(username):
	online = leagReq.lookUp(username)
	return online

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port = port, debug=True) #no debug=true