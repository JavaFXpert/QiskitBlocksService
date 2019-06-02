from flask import Flask, jsonify, request
from api import run_qasm
import json

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hi Qiskiter!"

@app.route('/test')
def test():
    return "Testing!"

@app.route('/api/run/qasm', methods=['POST'])
def qasm():
    qasm = request.form.get('qasm')
    print("--------------")
    print (qasm)
    print(request.get_data())
    print (request.form)
    backend = 'qasm_simulator'
    output = run_qasm(qasm, backend)
    ret = {"result": output}
    return jsonify(ret)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)