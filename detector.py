#!/usr/bin/python3

import subprocess as sb
print ("Content-type:text/html\r\n\r\n")

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields

data_entered = []

name = form.getvalue('name')
email = form.getvalue('email')
age = int(form.getvalue('age'))      #numeric age
 
gender = int(form.getvalue('gender'))

data_entered.append(gender)

fever = form.getvalue('fever')     #string : normal , fever , high

if form.getvalue('dry_cough') :
	dry_cough = 1
else :
	dry_cough = 0

data_entered.append(dry_cough)

if form.getvalue('sore_throat') :
	sore_throat = 1
else :
	sore_throat = 0

data_entered.append()

if form.getvalue('weakness') :
	weakness = 1
else :
	weakness = 0

data_entered.append(weakness)

if form.getvalue('breathing_problems') :
	breathing_problems = 1
else :
	breathing_problems = 0

data_entered.append(breathing_problems)

if form.getvalue('drowsiness') :
	drowsiness = 1
else :
	drowsiness = 0

data_entered.append(drowsiness)



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

progressed = int(form.getvalue('progressed'))   # 1 and 0

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

travel_history = int(form.getvalue('travel_history'))



print(name,' ',email,' ',age,'\n',
	fever, '\n' ,
	weakness , ' ' , dry_cough , ' ' , sore_throat , ' ' , drowsiness , ' ' , breathing_problems , ' ' , chest_pain , ' ' , loss_sense_smell , ' ' , appetide_change , '\n ' ,
 progressed , '\n' ,
	kidney_disease , ' ' ,heart_disease , ' ' , lung_disease , ' ' , diabetes , ' ' , high_blood_pressure , ' ' , stroke , '\n' , 
	travel_history)
