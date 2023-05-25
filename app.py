from flask import Flask, render_template, redirect, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# functions for scraping
def get_scrape(url_s):
	url = url_s
	# Step 1 : Get the HTML
	r = requests.get(url)
	htmlContent = r.content
	soup = BeautifulSoup(htmlContent, 'html.parser')
	return soup.prettify()

def get_title(url_s):
	url = url_s
	r = requests.get(url)
	htmlContent = r.content
	soup = BeautifulSoup(htmlContent, 'html.parser')
	return soup.title.string

def get_paras(url_s):
	url = url_s
	r = requests.get(url)
	htmlContent = r.content
	soup = BeautifulSoup(htmlContent, 'html.parser')
	return str(soup.find_all('p'))

def get_anchors(url_s):
	url = url_s
	r = requests.get(url)
	htmlContent = r.content
	soup = BeautifulSoup(htmlContent, 'html.parser')
	return str(soup.find_all('a'))

def get_Text(url_s):
	url = url_s
	r = requests.get(url)
	htmlContent = r.content
	soup = BeautifulSoup(htmlContent, 'html.parser')
	return soup.get_text()


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/basic", methods=['GET', 'POST'])
def scrape():
	if request.method == 'POST':
		url = request.form['url']
		type_p = request.form['type']
		if len(url)==0:
			result = "Enter url Please!"
			
		elif type_p == "1":	
			try:
				result = get_scrape(url)	
			except:
				result = "Error Occured !!"
			
		elif type_p == "2":
			try:
				result = get_title(url)
			except:
				result = "Error Occured !!"
		
		elif type_p == "3":
			try:
			 	result = get_paras(url)
			except:
				result = "Error Occured !!"
		
		elif type_p == "4":
			try:
				result = get_anchors(url)
			except:
				result = "Error Occured !!"

		elif type_p == "5":
			try:
				result = get_Text(url)
			except:
				result = "Error Occured !!"

		else:
			result = "Something Error!"

		return result

	return render_template("scrape.html")

@app.route("/advance", methods=['GET', 'POST'])
def advance_scrape():
	if request.method == 'POST':
		url = request.form['url']
		type_p = request.form['type']
		if len(url)==0:
			result = "Enter url Please!"
			
		elif type_p == "1":	
			try:
				result = get_scrape(url)	
			except:
				result = "Error Occured !!"

		elif type_p == "2":
			Id = request.form['id']
			Class = request.form['class']
			if(len(Id)>0):
				try:
					r = requests.get(url)
					htmlContent = r.content
					soup = BeautifulSoup(htmlContent, 'html.parser')
					result = str(soup.find(id=Id))
				except:
					result = "Error Occured !!"

			elif(len(Class)>0):
				try:
					r = requests.get(url)
					htmlContent = r.content
					soup = BeautifulSoup(htmlContent, 'html.parser')
					result = str(soup.select("."+Class))
				except:
					result = "Error Occured !!"

			else:
				result= "select ID or CLASS"

		elif type_p == "3":
			Id = request.form['id']
			Class = request.form['class']
			if(len(Id)>0):
				try:
					r = requests.get(url)
					htmlContent = r.content
					soup = BeautifulSoup(htmlContent, 'html.parser')
					result = str(soup.find_all("p", id=Id))
				except:
					result = "Error Occured !!"

			elif(len(Class)>0):
				try:
					r = requests.get(url)
					htmlContent = r.content
					soup = BeautifulSoup(htmlContent, 'html.parser')
					result = str(soup.find_all("p", class_=Class))
				except:
					result = "Error Occured !!"

			else:
				result= "select ID or CLASS"

		elif type_p == "4":
			Id = request.form['id']
			Class = request.form['class']
			if(len(Id)>0):
				try:
					r = requests.get(url)
					htmlContent = r.content
					soup = BeautifulSoup(htmlContent, 'html.parser')
					result = str(soup.find_all("div", id=Id))
				except:
					result = "Error Occured !!"

			elif(len(Class)>0):
				try:
					r = requests.get(url)
					htmlContent = r.content
					soup = BeautifulSoup(htmlContent, 'html.parser')
					result = str(soup.find_all("div", class_=Class))
				except:
					result = "Error Occured !!"

			else:
				result= "select ID or CLASS"

		elif type_p == "5":
			Id = request.form['id']
			Class = request.form['class']
			if(len(Id)>0):
				try:
					r = requests.get(url)
					htmlContent = r.content
					soup = BeautifulSoup(htmlContent, 'html.parser')
					result = str(soup.find_all("span", id=Id))
				except:
					result = "Error Occured !!"

			elif(len(Class)>0):
				try:
					r = requests.get(url)
					htmlContent = r.content
					soup = BeautifulSoup(htmlContent, 'html.parser')
					result = str(soup.find_all("span", class_=Class))
				except:
					result = "Error Occured !!"

			else:
				result= "select ID or CLASS"

		return result
	return render_template("advance.html")

if __name__=="__main__":
	app.run(debug=True, port=8000)