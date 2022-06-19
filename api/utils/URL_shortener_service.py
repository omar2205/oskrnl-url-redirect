from dotenv import load_dotenv; load_dotenv('../../.env')
from nanoid import generate as generate_nanoid
from .models import URL

def shorten_url(url):
  '''Shorten URL and return it's UID'''
  u = URL(url=url, uid=generate_nanoid(size=8))
  u.save()
  return u.uid


def get_url(uid):
  '''Get URL by it's UID'''
  u = URL.find(URL.uid == uid).all()
  if u:
    return u[0].url
