from flask import Flask, render_template

app=Flask(__name__)

@app.route('/home')
def home(): 
	return render_template("home.html")

@app.route('/about')
def about(): 
	return render_template("about.html")

@app.route('/AsianFemale18Crime')
def asianFemale18(): 
	return render_template("AsianFemale18crime.html")

@app.route('/AsianMale18Crime')
def AsianMale18Crime(): 
	return render_template("AsianMale18.html")

@app.route('/WhiteFemale18Crime')
def whiteFemale18(): 
	return render_template("WhiteFemale18.html")

@app.route('/WhiteMale18Crime')
def whiteMale18(): 
	return render_template("WhiteMale18.html")

@app.route('/BlackFemale18Crime')
def blackFemale18(): 
	return render_template("BlackFemale18.html")

@app.route('/BlackMale18Crime')
def blackMale18(): 
	return render_template("BlackMale18.html")

@app.route('/HispanicFemale18Crime')
def hispanicFemale18(): 
	return render_template("HispanicFemale18.html")

@app.route('/HispanicMale18Crime')
def hispanicMale18(): 
	return render_template("HispanicMale18.html")

if __name__=="__main__": 
	app.run(debug=True)

