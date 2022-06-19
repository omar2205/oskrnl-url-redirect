import time
from redis_om import HashModel, Field, Migrator
from pydantic import AnyUrl

class URL(HashModel):
  '''URL model'''
  url: AnyUrl = Field(index=True)
  uid: str = Field(index=True)
  created_at: int = int(time.time())

  class Meta:
    global_key_prefix = "urls"


class Admin(HashModel):
  '''Admin model'''
  username: str = Field(index=True)
  password: str

  class Meta:
    global_key_prefix = "users-admin"

Migrator().run()
