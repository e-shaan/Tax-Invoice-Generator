# importing Required Modules
from reportlab.pdfgen import canvas
import csv
import json


currency_dict = {
	'AED' : 'UAE', 
	'GBP' : 'UK',
	'USD' : 'USA',
	'SAR' : 'Saudi Arabia',
	'SGD' : 'Singapore',
	'QAR' : 'Qatar',
}


#description for "Description" columns
description1 = "Coding"
description2 = "Comprehensive"
description3 = "Course"


#function to generate and save invoice in .pdf format
def generate_pdf(id, amount, currency, order_id, email, contact, created_at, settled_at):

	filename = settled_at +" " + order_id+".pdf"

	# Creating Canvas
	c = canvas.Canvas(filename,pagesize=(200,270),bottomup=0)

	# Logo Section
	# Setting the origin to (10,40)
	c.translate(10,40)
	# Inverting the scale for getting mirror Image of logo
	c.scale(1,-1)

	# Inserting Logo into the Canvas at required position
	c.drawImage("MF logo.png",0,0,width=25,height=30)
	c.drawImage("mF Footer.png",0,-227,width=180,height=25)

	# Title Section
	# Again Inverting Scale For strings insertion
	c.scale(1,-1)
	# Again Setting the origin back to (0,0) of top-left
	c.translate(-10,-40)
	# Setting the font for Name title of company
	c.setFont("Helvetica-Bold",8)
	# Inserting the name of the company
	c.drawCentredString(125,20,"Lanuk Soft Pvt Limited")
	# Changing the font size for Specifying Address
	c.setFont("Helvetica-Oblique",7)
	c.drawCentredString(125,30,"moveForward(100)")
	c.setFont("Helvetica-Bold",4)
	c.drawCentredString(125,40,id)
	# Line Seprating the page header from the body
	c.line(5,45,195,45)
	# Document Information
	# Changing the font for Document title
	c.setFont("Courier-Bold",8)
	c.drawCentredString(100,55,"TAX-INVOICE")
	# This Block Consist of Costumer Details
	c.roundRect(15,63,170,40,1,stroke=1,fill=0)
	c.setFont("Times-Bold",5)


	c.drawString(20,71,"Customer E-mail : " + email)
	c.drawString(20,79,"Customer Contact :" + contact)
	c.drawString(20,87,"Place : " + currency_dict[currency])
	c.drawString(20,95,"Invoice No. : " + order_id)
	c.drawString(115,87, "Created On : " + created_at)
	c.drawString(115,95, "Settled On : " + settled_at)

	# This Block Consists of Item Description
	c.roundRect(15,108,170,130,1,stroke=1,fill=0)
	c.line(15,120,185,120)
	c.drawString(17,118,"S.No.")
	c.drawString(36,118,"DESCRIPTION")
	c.drawString(76,118,"CURRENCY")
	c.drawString(109,118,"RATE")
	c.drawString(135,118,"MODE")
	c.drawString(165,118,"TOTAL")

	# Drawing table for Item Description
	c.line(15,210,185,210)
	c.line(30,108,30,220)
	c.line(75,108,75,220)
	c.line(105,108,105,220)
	c.line(125,108,125,220)
	c.line(160,108,160,220)

	# Table contents
	c.drawString(17,128, '1')
	c.drawString(38,128, description1)
	c.drawString(38,133, description2)
	c.drawString(38,138, description3)
	c.drawString(79,128, currency)
	c.drawString(109,128, amount)
	c.drawString(135,128, "RazorPay")
	c.drawString(165,128, amount)
	c.drawString(135,215,"Total:")
	c.drawString(165,215,amount)

	# Declaration and Signature
	c.line(15,220,185,220)
	c.line(100,220,100,238)
	c.drawString(28,225,"Terms - Due on receipt")
	c.drawString(20,235,"(This is system generated invoice)")
	c.setFont("Times-Bold",5)
	c.drawRightString(165,230,"(Includes 18 % GST)")

	# End the Page and Start with new
	c.showPage()
	# Saving the PDF
	c.save()


#function to extract contents from .csv files
def extract_from_csv():


	file = open("NONE_INR.json")
	data = json.load(file)
	#print(json.dumps(data,indent = 4))
	file.close()

	for i in data:
		id = str(i['id'])
		amount = str(i['amount'])
		currency = str(i['currency'])
		order_id = str(i['order_id'])
		email = str(i['email'])
		contact = str(i['contact'])
		created_at = str(i['ltrim(rtrim(created_at))'])
		settled_at = str(i['ltrim(rtrim(settled_at))'])

		generate_pdf(id,amount,currency,order_id,email,contact,created_at,settled_at)

extract_from_csv()
