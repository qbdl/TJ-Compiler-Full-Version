from flask import Flask, request, jsonify
import os
import subprocess


if __name__ == '__main__':
    # clean_result = subprocess.run(['make', '-C', 'TJ-Compiler', 'clean'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = subprocess.run(['make', '-C', 'TJ-Compiler'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #make input_test
    run_result = subprocess.run(['make', '-C', 'TJ-Compiler','input_test'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    run_result_output = run_result.stdout.decode().split('\n')
    filtered_output = [line for line in run_result_output if not line.strip().startswith('make:')]
    real_output='\n'.join(filtered_output)
    print(real_output)
    
    run_result_err_output=run_result.stderr.decode().split('\n')
    filtered_err_output=[line for line in run_result_err_output if not line.strip().startswith('make:')]
    final_err_output='\n'.join(filtered_err_output)
    print(final_err_output)
   