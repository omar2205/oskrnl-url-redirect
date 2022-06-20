import json
from bottle import Bottle, request, response, redirect # pylint: disable=import-error

app = Bottle()

@app.route('/api/hello', method=['POST', 'GET'])
def hello():
  return json.dumps(request.json)