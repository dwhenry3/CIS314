# pip install flask
#from flask import Flask, render_template, request, make_response, redirect
from flask import *
from werkzeug.utils import secure_filename
import os
import random

UPLOAD_FOLDER = "C:\\Users\\Dane\\OneDrive - Legal Aid of West Virginia, Inc\\Personal\\Shepherd\\Spring 2025\\CIS314\\firstFlask\\uploads"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return 'Hello CIS 314!'

@app.route('/admin')
def admin():
    return 'Welcome to the admin interface'

@app.route('/lorem')
def lorem():
    return render_template("index.html")

@app.route('/cookie') 
def cookie(): 
    return render_template('cookie.html') 

@app.route('/setcookie', methods = ['POST', 'GET']) 
def setcookie(): 
    if request.method == 'POST': 
        user = request.form['nm'] 
        resp = make_response(render_template('show_cookie.html')) 
        resp.set_cookie('userID', user) 
        return resp

@app.route('/getcookie') 
def getcookie(): 
    name = request.cookies.get('userID') 
    return '<h1>welcome '+name+'</h1>'

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

@app.route('/rng')
def rng():
    num = random.randint(1, 1000000)
    return str(num)

@app.route('/sorting')
def sorting():
    output = []
    x = 0
    while x < 20:
        output.append(random.randint(1, 20))
        x+=1
    sorted_output = output.copy()
    sorted_output.sort()
    return '''
    <!doctype html>
    <html>
    <head>
    <title>Sorted Stuff</title>
    </head>
    <body>
    <div>Unsorted:'''+str(output)+'''</div>
    <div>Sorted:'''+str(sorted_output)+'''</div>
    </body>
    </html>
    '''

@app.route('/sorthtml')
def sorthtml():
    output = []
    x = 0
    while x < 20:
        output.append(random.randint(1, 20))
        x+=1
    sorted_output = output.copy()
    sorted_output.sort()
    return render_template('sorthtml.html', first_out = output, second_out = sorted_output) 

if __name__ == '__main__':
    app.run(debug=True)