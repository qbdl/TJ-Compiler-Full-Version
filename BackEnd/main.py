from flask import Flask, request, jsonify
import os
import subprocess
import sys
sys.path.append("C:/Users/likejie/AppData/Local/Programs/Python/Python39/Lib/site-packages")
from flask_cors import CORS

# Global Variables
app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)  # 解决跨域问题


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


# 六一快乐！
@app.route('/', methods=['GET', 'POST'])
def hello():
    return "Nice to see you again!"


if __name__ == '__main__':
    app.run(debug=True)
