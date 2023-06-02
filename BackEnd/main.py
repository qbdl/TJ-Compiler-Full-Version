from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import sys
import time
import subprocess
from flask_cors import CORS

# Global Variables
app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)  # 解决跨域问题
app.config['UPLOAD_FILE_FOLDER'] = './uploads'  # 设置上传文件的文件夹路径
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'cpp', 'c'}  # 设置允许的文件类型

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def upload_save_file(file, path: str):
    file_ext = file.filename.rsplit('.', 1)[1].lower()
    timestamp = int(time.time())
    new_filename = f"{timestamp}_{file.filename}"
    file.save(os.path.join(path, new_filename))
    return new_filename

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        new_filename = upload_save_file(file, app.config['UPLOAD_FILE_FOLDER'])
        # 使用你的编译器编译源代码
        result = subprocess.run(['gcc', '-o', 'output', os.path.join(app.config['UPLOAD_FILE_FOLDER'], new_filename)],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        return jsonify({
            "success": f"File uploaded and saved as {new_filename}",
            "output": result.stdout.decode(),
            "error": result.stderr.decode(),
        }), 200
    else:
        return jsonify({"error": "Unsupported file type"}), 400

@app.route('/compile', methods=['POST'])
def compile_code():
    code = request.json.get('code')
    if not code:
        return jsonify({"error": "No code provided"}), 400

    with open('./code_file.c', 'w') as file:
        file.write(code)
        
    # 使用你的编译器编译源代码
    result = subprocess.run(['gcc', '-o', 'output', './code_file.c'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return jsonify({
        "output": result.stdout.decode(),
        "error": result.stderr.decode(),
    }), 200

@app.route('/', methods=['GET', 'POST'])
def hello():
    return "Nice to see you again!"

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FILE_FOLDER']):
        os.makedirs(app.config['UPLOAD_FILE_FOLDER'])  # 如果上传文件夹不存在，则创建
    app.run(debug=True)
