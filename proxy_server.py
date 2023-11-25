from flask import Flask, request, Response
import requests
import logging
import sys
import os

app = Flask(__name__)

# Configure your destination URL here
DESTINATION_URL = os.getenv('DESTINATION_URL') or 'http://example.com'

# Configure logging
#logging.basicConfig(filename='proxy.log', level=logging.INFO)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

def log_request(req, res):
    logging.info(f"Request: {req.method} {req.url} - Payload: {req.data} - Response: {res.status_code}, {res.content}")

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    global DESTINATION_URL
    if request.method == 'GET':
        response = requests.get(f"{DESTINATION_URL}/{path}", params=request.args)
    elif request.method == 'POST':
        response = requests.post(f"{DESTINATION_URL}/{path}", json=request.json)
    # Add similar blocks for PUT, DELETE, etc.

    log_request(request, response)
    return Response(response.content, status=response.status_code, content_type=response.headers['Content-Type'])

def run_app():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    print('destination:', DESTINATION_URL)
    run_app()
