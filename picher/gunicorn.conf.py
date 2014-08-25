import os.path

DIR = os.path.join(os.getcwd(), 'server')

bind = '127.0.0.1:9696'
daemon = True
pidfile = os.path.join(DIR, 'gunicorn.pid')
accesslog = os.path.join(DIR, 'access.log')
errorlog = os.path.join(DIR, 'error.log')
loglevel = 'debug'
