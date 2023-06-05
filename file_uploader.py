from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from allowed_files import allowed_file
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'imgs'

@app.route('/upload', methods = ['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # File uzantisinin kontrolu ve yuklenmesi
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'File is succesfuly uploaded.'
            os.system('lp imgs/', filename)     
        else:
            return 'Invalid file extension.' 
    elif request.method == 'GET':
        return render_template('file_upload.html')
    else:
        return 'invalid request methods'

if __name__ == '__main__':
   app.run(debug = True)