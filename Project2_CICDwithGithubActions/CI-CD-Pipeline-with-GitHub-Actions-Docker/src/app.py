from flask import Flask, jsonify, request
import os
import sys
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        'message': 'Hello from Jenkins Pipeline!',
        'version': os.environ.get('VERSION', '1.0.0'),
        'environment': os.environ.get('ENV', 'development')
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

@app.route('/info')
def info():
    return jsonify({
        'Application': {
            'name': 'Flask Route App',
            'version': os.environ.get('VERSION', '1.0.0'),
            'environment': os.environ.get('ENV', 'development'),
            'python_version': sys.version.split()[0]
        }
    })

@app.route('/api/data')
def sample_data():
    sample_data = [
        {'id': 1, 'name': 'Chocolate', 'status': 'active'},
        {'id': 2, 'name': 'Froyo', 'status': 'active'},
        {'id': 3, 'name': 'Gingerbread', 'status': 'active'},
    ]

    return jsonify({
        'data': sample_data,
        'count': len(sample_data),
        'timestamp': datetime.datetime.utcnow().isoformat()
    })

@app.route('/api/echo', methods=['GET', 'POST'])
def echo():
    """Send request data, and receive information about the API request"""
    json_data = None
    if request.method == 'POST':
        try:
            json_data = request.get_json()
        except:
            json_data = None

    return jsonify({
        'method': request.method,
        'json_data': json_data,
        'form_data': dict(request.form),
        'args': dict(request.args)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)