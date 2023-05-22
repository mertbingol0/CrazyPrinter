from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload')
def upload_file():
    return render_template('file_upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_filea():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return "succesfuly for this func"
        
'''
f.filename ile upload edilen dosya name'i alinir.
Bunu kullanarak aldigimiz dosya adini 'lp {f.filename} gibi bir isleme sokmamiz gerekiyor.
'''

if __name__ == '__main__':
   app.run(debug = True)