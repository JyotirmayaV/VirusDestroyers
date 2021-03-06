#!/usr/bin/env python3.8


print ("Content-type:text/html\r\n\r\n")

# Import modules for CGI handling 
import cgi, cgitb 
cgitb.enable()

import subprocess as sb

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields

print('''<html>
	<head>
		<title>Detection Results</title>
				<style>
		.button {
		  background-color: #4CAF50; /* Green */
		  border: none;
		  color: white;
		  padding: 15px 32px;
		  text-align: center;
		  text-decoration: none;
		  
		  font-size: 16px;
		  margin: 4px 2px;
		  cursor: pointer;
		}

		.button2 {background-color: #ffa500;} /* Orange */
		.button3 {background-color: #f44336;} /* Red */ 
		
		</style>
		
	<body>
	<center><h1>YOUR COVID DETECTION RESULT</h1>
	[ Team Members : Arpit Pathak , Hemant Gangwar , Yashi Agarwal , Akansh Agarwal , Akshay Maheshwari , Prabal , Rahul Rastogi , Ashutosh Tiwari and Jyotirmaya ]
	</center>
           <center> <pre>''')
#print('i came here')



name = form.getvalue('name')
email = form.getvalue('email')
#print('here')
age = str(form.getvalue('age'))      #numeric age
#print('age : ',age)
if age == 'None':
    age = 10
else:
    age = int(age)

gender = str(form.getvalue('gender'))
if gender == 'None':
    gender = 0
else:
    gender = int(gender)

#print('i came here basic details')
data_entered = []

fever = form.getvalue('fever')     #string : normal , fever , high

if form.getvalue('dry_cough') :
	dry_cough = 1
else :
	dry_cough = 0


if form.getvalue('sore_throat') :
	sore_throat = 1
else :
	sore_throat = 0


if form.getvalue('weakness') :
	weakness = 1
else :
	weakness = 0


if form.getvalue('breathing_problems') :
	breathing_problems = 1
else :
	breathing_problems = 0



if form.getvalue('drowsiness') :
	drowsiness = 1
else :
	drowsiness = 0


if form.getvalue('chest_pain') :
	chest_pain = 1
else :
	chest_pain = 0


if form.getvalue('loss_sense_smell') :
	loss_sense_smell = 1
else :
	loss_sense_smell = 0

if form.getvalue('appetide_change') :
	appetide_change = 1
else :
	appetide_change = 0

progressed = str(form.getvalue('progressed'))   # 1 and 0

if progressed == 'None':
    progressed = 0
else :
    progressed = int(progressed)

#print('i came here symptoms')

if form.getvalue('kidney_disease') :
	kidney_disease = 1
else :
	kidney_disease = 0

if form.getvalue('heart_disease') :
	heart_disease = 1
else :
	heart_disease = 0

if form.getvalue('lung_disease') :
	lung_disease = 1
else :
	lung_disease = 0

if form.getvalue('diabetes') :
	diabetes = 1
else :
	diabetes = 0

if form.getvalue('high_blood_pressure') :
	high_blood_pressure = 1
else :
	high_blood_pressure = 0

if form.getvalue('stroke') :
	stroke = 1
else :
	stroke = 0

travel_history = str(form.getvalue('travel_history'))

if travel_history == 'None':
    travel_history = 0
else :
    travel_history = int(travel_history)

#print('i came here read data begin')

data = '\nname : ' + name + ' email : ' + email + ' data received : [' 

data_entered.append(gender)
data = data + '  ' + str(gender)
data_entered.append(dry_cough)
data = data + ' , ' + ' , ' +str(dry_cough)
data_entered.append(sore_throat)
data = data + ' , ' + ' , ' + str(sore_throat)
data_entered.append(weakness)
data = data + ' , ' + str(weakness)
data_entered.append(breathing_problems)
data = data + ' , ' + str(breathing_problems)
data_entered.append(drowsiness)
data = data + ' , ' + str(drowsiness)
data_entered.append(chest_pain)
data = data + ' , ' + str(chest_pain)
data_entered.append(travel_history)
data = data + ' , ' + str(travel_history)
data_entered.append(diabetes)
data = data + ' , ' + str(diabetes)
data_entered.append(heart_disease)
data = data + ' , ' + str(heart_disease)
data_entered.append(lung_disease)
data = data + ' , ' + str(lung_disease)
data_entered.append(stroke)
data = data + ' , ' + str(stroke)
data_entered.append(progressed)
data = data + ' , ' + str(progressed)
data_entered.append(high_blood_pressure)
data = data + ' , ' + str(high_blood_pressure)
data_entered.append(kidney_disease)
data = data + ' , ' + str(kidney_disease)
data_entered.append(appetide_change)
data = data + ' , ' + str(appetide_change)
data_entered.append(loss_sense_smell)
data = data + ' , ' + str(loss_sense_smell)

#print('i came here read data end')

for i in range(10,100,10):
	if age >= i and age < i+10:
		data_entered.append(1)
	else :
		data_entered.append(0)
data = data + ' , ' + str(age)

#print('i came here age appended')

if fever == 'fever':
	data_entered.append(1)
else:
	data_entered.append(0)

if fever == 'high':
	data_entered.append(1)
else:
	data_entered.append(0)

data = data + ' , ' + fever

print('<hr><hr>')
print('<h3>The Data you filled</h3>')

print ( 'name :' ,name,
		'\nemail :',email,
		'\ngender :',gender,
		'\ndry_cough :',dry_cough,
		'\nsore_throat :',sore_throat,
		'\nweakness :',weakness,
		'\nbreathing_problems :',breathing_problems,
		'\ndrowsiness :',drowsiness,
		'\nchest_pain :',chest_pain,
		'\ntravel_history :',travel_history,
		'\ndiabetes :',diabetes,
		'\nheart_disease :',heart_disease,
		'\nlung_disease :',lung_disease,
		'\nstroke :',stroke,
		'\nprogressed :',progressed,
		'\nhigh_blood_pressure :',high_blood_pressure,
		'\nkidney_disease :',kidney_disease,
		'\nappetite_change :',appetide_change,
		'\nloss_sense_smell :',loss_sense_smell,
		'\nage :',age,
		'\nfever :',fever,
		'\n[age columns : 10,20,30,40,50,60,70,80,90]',
		'\n[fever columns : 98.6,102]'
	)
print('<hr>')
print('<h3>The data we generated from your input</h3>')
print(data_entered)
print('<hr>')
print('Note : The above data is being displayed only because its a protoype and we want to show what data of user we have received and how we have converted into the machine understandable form.\nThe above shall not be a part of the real working website.')
print('<hr><hr>')
from keras.models import load_model
model = load_model('updatemodel99-01.h5')
m = model.predict([[data_entered]])

m = list(m[0]) #converted from a 2D array with one row only to a 1D list 

m = m.index(max(m)) #finding the index of the maximum value predicted

#print('Class : ',m)

print('<h3>Your Result is</h3>',end='')

if m == 0 :
	print("<h2>No Risk</h2>")
elif m == 1:
	print('<h2>Medium Risk</h2>')
else:
	print('<h2>High Risk</h2>')


sb.getoutput('sudo python3 Corona\\ Hotspot.py')

print('<hr><h3>We care for your safety and therfore would like to show you the different zones in your area.Click on below buttons to see them.</h3>')

print ('''	
			</pre>
			<button type = 'button' class = 'button '><a href = '/green_map.html'> Green Zone </a></button>
			<button type = 'button' class = 'button button2'><a href = '/orange_map.html'> Orange Zone </a></button>
			<button type = /button' class = 'button button3'><a href = '/red_map.html'> Red Zone </a></button></center><hr>
	''')

print(''' 
                </body>
	            </html>''')

file1 = open("myfile.txt","a") 

data = data + ' ] ' + ' output : ' + str(m) 

file1.write(data)

file1.close()