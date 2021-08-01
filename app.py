from flask import Flask
from flask import json
import logging
from datetime import datetime
app = Flask(__name__)

logging.basicConfig(filename='app.log',level=logging.DEBUG)

@app.route('/status')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    app.logger.debug('%s status endpoint was reached', datetime.now())

    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    app.logger.debug('%s metrics endpoint was reached', datetime.now())
    return response

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
