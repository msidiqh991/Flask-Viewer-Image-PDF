from flask import Flask, render_template, request, session
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join('static')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'This is your secret key to utilize session in Flask'

@app.route('/')
def index():
    return render_template('index.html', output=None)

@app.route('/proses', methods=['GET', 'POST'])
def proses():
    if request.method == 'POST':
        uploaded_img = request.files['uploaded-file']
        img_filename = secure_filename(uploaded_img.filename)
        uploaded_img.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
        session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)
 
        return render_template('index.html')

@app.route('/output')
def displayFile():
    img_file_path = session.get('uploaded_img_file_path', None)
    return render_template('show_image.html', user_image = img_file_path)
 
if __name__=='__main__':
     app.run(debug=True,
            host="127.0.0.1",
            port=int(os.environ.get("PORT", 8080)))

