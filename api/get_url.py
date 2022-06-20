from bottle import Bottle, response # pylint: disable=import-error

from .utils.URL_shortener_service import get_url
from .utils.helpers import HTTP_CODES
from .utils.handle_errors import handler as err_handler

app = Bottle()
app.error_handler = err_handler

@app.route('/get_url/<uid>', method='GET')
def get_url_by_uid(uid):
  '''Get URL by it's UID'''
  if not uid:
    response.status = HTTP_CODES['BAD_REQUEST']
    return {'code': HTTP_CODES['BAD_REQUEST'], 'error': 'No UID provided'}

  url = get_url(uid)
  if url:
    response.status = HTTP_CODES['OK']
    return {'code': HTTP_CODES['OK'], 'error': False, 'data': {'url': url}}

  response.status = HTTP_CODES['NOT_FOUND']
  return {'code': HTTP_CODES['NOT_FOUND'], 'error': 'No URL found', 'data': False}
