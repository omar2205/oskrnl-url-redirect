import json
from bottle import response

def generate_err(err):
  c = err.status_code or 9999
  m = err.status_line or 'unkown err!'
  res = { 'code': c, 'error': m }
  response.content_type = 'application/json'
  return json.dumps(res)

handler = {
  500: lambda err: generate_err(err),
  404: lambda err: generate_err(err),
  405: lambda err: generate_err(err),
}
