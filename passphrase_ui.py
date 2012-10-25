from flask import Flask, render_template, request
import passphrase_functions

app = Flask(__name__)

# display the home page on
@app.route("/")
def index():
	return render_template('passphrase.html')

@app.route("/enter_length", methods=["POST"])
def gen_pass():
	word_list = passphrase_functions.open_file('415words.txt')
	pass_len = int(request.form['length'])
	#language = request.form['']
	passphrase = passphrase_functions.gen_pw(pass_len, word_list)
	return passphrase

if __name__ == "__main__":
    app.run(debug=True)