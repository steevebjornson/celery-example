from os import environ
from celery import Celery

app = Celery()
app.config_from_object('celery_config')

@app.task
def add(x, y):
    return x + y

@app.task
def tsum(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args[0])
