import os
from bottle import Bottle, request, response # pylint: disable=import-error
from .utils.helpers import HTTP_CODES

app = Bottle()

@app.route('/create_admin', method='POST')
def create_admin():
  '''Create new admin user
  req: {"username": "admin", "password": "admin"}'''

  # TODO: not implemented.

  # validate token
  token = request.headers.get('Authorization', None)
  if not token or token != os.getenv('ADMIN_TOKEN'):
    return 'Nothing to see here'

  # base response body
  body = {'code': 200, 'error': False, 'data': False}

  try:
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if username and password:
      print(username, password)
      body['code'] = HTTP_CODES['NOT_IMPLEMENTED']
      body['error'] = 'NOT_IMPLEMENTED'
      body['data'] = {'username': username}
      response.status = HTTP_CODES['NOT_IMPLEMENTED']
      return body

    # if no username or password in request, return error
    body['code'] = 400
    body['error'] = 'No username or password provided'
    body['data'] = False
    response.status_code = HTTP_CODES['BAD_REQUEST']
    return body

  # request is not JSON or doesn't have "username" or "password" fields
  except AttributeError:
    body['code'] = 400
    body['error'] = 'Invalid request'
    body['data'] = False
    response.status = HTTP_CODES['BAD_REQUEST']
    return body
