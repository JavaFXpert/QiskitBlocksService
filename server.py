from flask import Flask, jsonify, request
from api import run_qasm
import json

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Hi Qiskiter!"


@app.route('/test', methods=['POST'])
def test_json():
    data = request.get_json()
    qasm = data['qasm']
    print("--------------")
    print(qasm)
    backend = 'qasm_simulator'
    output = run_qasm(qasm, backend)
    ret = {"result": output}
    return jsonify(ret)


@app.route('/api/run/qasm', methods=['POST'])
def qasm():
    data = request.get_json()
    qasm = data['qasm']
    backend = data['backend']
    print("--------------")
    print(qasm)
    print(backend)
    output = run_qasm(qasm, backend)
    ret = {"result": output}
    return jsonify(ret)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
