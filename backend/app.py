from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    videos = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', videos=videos)

@app.route('/upload', methods=['POST'])
def upload():
    video = request.files['video']
    if video:
        path = os.path.join(UPLOAD_FOLDER, video.filename)
        video.save(path)
    return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
