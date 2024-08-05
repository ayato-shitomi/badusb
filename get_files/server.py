from flask import Flask, request
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_file():
    filename = request.form.get('filename')
    if filename is None:
        return 'Filename is required', 400
    
    file = request.files.get('file')
    if file is None:
        return 'File is required', 400

    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d-%H-%M-%S')
    
    save_dir = './data/'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    file_path = os.path.join(save_dir, f'{formatted_date}_{filename}')
    file.save(file_path)
    
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, port=4242)
