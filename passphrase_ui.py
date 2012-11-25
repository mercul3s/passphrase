from flask import Flask, render_template, request, redirect, flash
import passphrase_functions

app = Flask(__name__)

# display the home page on
@app.route("/", methods=["GET"])
def index():
	return render_template('passphrase.html')

@app.route("/passphrase", methods=["POST"])
def gen_pass():
	pass_len = request.form['pass-length']
	slang = request.form['slang']
	print pass_len
	print slang
	# if pass_len == '':
	# and slang == None:
	# 	pass_len = 3
	# 	slang = '415words.txt'
	word_list = passphrase_functions.open_file(slang)
	passphrase = passphrase_functions.gen_pw(int(pass_len), word_list)
	flash(passphrase)
	return redirect('/')

app.secret_key = 'TheStick?Hubba#Penelopes$'

if __name__ == "__main__":
	app.debug = True
	app.run(host='localhost', port=5000)