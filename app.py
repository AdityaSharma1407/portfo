from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/<string:page_number>')
def html_page(page_number):
	return render_template(page_number)

def write_to_file(data):
	with open('database.txt',mode='a') as database :
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv',mode='a') as database2 :
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2,delimiter =',')
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	try:
    		data = request.form.to_dict()
    		write_to_csv(data)
    		return redirect('/thanku.html')
    	except Exception as e:
    		return "did not save to database"


    else:
    	return "something went wrong"