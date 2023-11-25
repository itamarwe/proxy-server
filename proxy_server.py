from flask import Flask, request, Response
import requests
import logging
import sys
import os
from utils import log_request

app = Flask(__name__)

# Configure your destination URL here
DESTINATION_URL = os.getenv('DESTINATION_URL') or 'http://example.com'

# Configure logging
#logging.basicConfig(filename='proxy.log', level=logging.INFO)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('/var/log/proxy.log')
    ]
)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def proxy(path):
    # Get the URL to forward the request to
    url = f"{DESTINATION_URL}/{path}"

    # Forward the headers, excluding the Host header to avoid conflicts
    headers = {key: value for key, value in request.headers if key != 'Host'}

    # Make the outgoing request with the same method, headers, and data as the incoming request
    response = requests.request(
        method=request.method,
        url=url,
        headers=headers,
        data=request.get_data(),
        params=request.args,
        allow_redirects=False
    )

    # Log the request
    log_request(logging.info, request, response)

    # Create a response object and return it
    return Response(response.content, status=response.status_code, headers=dict(response.headers))

def run_app():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    print('destination:', DESTINATION_URL)
    run_app()
