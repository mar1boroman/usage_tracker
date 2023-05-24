# Track your python file usage!
Python package to track the usage of any python script, generate events and send them to a redis stream!

# Sample usage in your script

```python
from usage_tracker.usage_tracker import silent_tracker

silent_tracker(
    redis_host='<YOUR REDIS HOST>',
    redis_port='<YOUR REDIS PORT>',
    redis_username='<YOUR REDIS USERNAME>',
    redis_password='<YOUR REDIS PASSWORD>',
    appname='<APP/FILE NAME [ OPTIONAL | Default : generic ]>',
    email='<EMAIL ADDRESS [ OPTIONAL | Default : empty]>',
    payload='<PAYLOAD STRING[ OPTIONAL | Default : empty]>'
)
```