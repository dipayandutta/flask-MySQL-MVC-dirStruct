from view.reg_form import RegisterForm
from flask import request
from flask import render_template,url_for , session ,logging,redirect,flash
from view.reg_form import RegisterForm
from application import app
from application import db
from passlib.hash import sha256_crypt 

@app.route('/register',methods=['GET','POST'])
#The register URL Function defination 
def register():
	form = RegisterForm(request.form) # calling the RegisterForm class

	#Checking if the Form method is POST and also it is validated
	if request.method == 'POST' and form.validate():
		# code for form value data base submission
		#First Getting the Form Values

		name 		= form.name.data 
		email 		= form.email.data
		username 	= form.username.data 
		password 	= sha256_crypt.encrypt(str(form.password.data)) #Wrap the password in encrption wrapper


		# Create the Cursor 
		cur = db.connection.cursor()

		#Excute Commands using the connected Cursor
		cur.execute("INSERT INTO users(name,email,username,password) VALUES (%s , %s , %s , %s)",(name,email,username,password)) 

		#Commit To Database
		db.connection.commit()

		#Close the Connection 
		cur.close()

		#Set the Flash Message after registered

		flash('You are Registered ','success') # For setting the Flash messages with catagories , we have to add a templapte and also add the template in the layout.html file
		
		#Redirecting in the Index Page after successful Registration
		return redirect(url_for('index'))


	return render_template('register.html',form = form)