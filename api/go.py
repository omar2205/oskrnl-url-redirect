from bottle import Bottle, request, response, redirect # pylint: disable=import-error
from pydantic import ValidationError # pylint: disable=import-error

from .utils.URL_shortener_service import shorten_url, get_url
from .utils.helpers import HTTP_CODES

app = Bottle()

@app.route('/go/<uid>')
def redirect_url(uid):
  '''Redirect to URL by it's UID'''
  url = get_url(uid)
  if url:
    return redirect(url, code=HTTP_CODES['Found'])
  return 'No URL found'


@app.route('/create', method='POST')
def create_url():
  '''Create new URL and return it's UID
  req: {"url": "https://example.com"}'''

  # base response body
  body = {'code': HTTP_CODES['OK'], 'error': False, 'data': False}

  try:
    url = request.json.get('url', None)

    if url:
      try:
        body['code'] = HTTP_CODES['CREATED']
        body['error'] = False
        body['data'] = {'uid': shorten_url(url)}

      # If URL is invalid, it will raise ValidationError
      except ValidationError:
        body['code'] = HTTP_CODES['BAD_REQUEST']
        body['error'] = 'Invalid URL'
        body['data'] = False
        response.status_code = HTTP_CODES['BAD_REQUEST']
        return body

      # else return body with generated UID
      return body

    # if no URL in request, return error
    body['code'] = HTTP_CODES['BAD_REQUEST']
    body['error'] = 'No URL provided'
    body['data'] = False
    response.status_code = HTTP_CODES['BAD_REQUEST']
    return body

  # request is not JSON
  except AttributeError:
    body['code'] = HTTP_CODES['BAD_REQUEST']
    body['error'] = 'Invalid request'
    body['data'] = False
    response.status = HTTP_CODES['BAD_REQUEST']
    return body
