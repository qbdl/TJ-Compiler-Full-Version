from flask import Flask, request, jsonify
import os
import subprocess
import sys
# sys.path.append("C:/Users/likejie/AppData/Local/Programs/Python/Python39/Lib/site-packages")
from flask_cors import CORS

# Global Variables
app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)  # 解决跨域问题


@app.route('/compile', methods=['POST'])
def compile_code():
    #make clean
    clean_result = subprocess.run(['make', '-C', 'TJ-Compiler', 'clean'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    code = request.json.get('code')
    if not code:
        return jsonify({"error": "No code provided"}), 400

    with open('./TJ-Compiler/code_file', 'w') as file:
        file.write(code)

    # 使用你的编译器编译源代码
    #make
    result = subprocess.run(['make', '-C', 'TJ-Compiler'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #make input_test
    run_result = subprocess.run(['make', '-C', 'TJ-Compiler','input_test'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    run_result_output = run_result.stdout.decode().split('\n')
    filtered_output = [line for line in run_result_output if not line.strip().startswith('make:')]
    final_output='\n'.join(filtered_output)
    print(final_output)
    
    run_result_err_output=run_result.stderr.decode().split('\n')
    filtered_err_output=[line for line in run_result_err_output if not line.strip().startswith('make:')]
    final_err_output='\n'.join(filtered_err_output)
    print(final_err_output)
    
    # result = subprocess.run(['gcc', '-o', 'output', './code_file.c'],
    #                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if run_result.returncode != 0:
        return jsonify({
            "output": final_output,
            "error": "An error occurred while compiling the code:\n{}".format(final_err_output)
        }), 400
    else:
        return jsonify({
            "output": final_output,
            "error": final_err_output,
        }), 200


# 六一快乐！
@app.route('/', methods=['GET', 'POST'])
def hello():
    return "Nice to see you again!"


if __name__ == '__main__':
    app.run(debug=True)
