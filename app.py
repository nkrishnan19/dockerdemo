from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host=os.environ['REDIS_HOST'], port=6379)

@app.route('/')
def hello():
   redis.incr('hits')
   return 'Hello Compose! I have been seen %s times\n' % redis.get('hits')

if __name__ == "__main__":
   app.run(host="0.0.0.0", debug=True)
