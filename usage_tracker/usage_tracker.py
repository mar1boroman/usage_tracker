import redis
from datetime import datetime
import time
import socket
import getpass


def silent_tracker(
    redis_port, redis_host, redis_username, redis_password, appname='generic', payload="", email=""
):
    r = redis.Redis(
        host=redis_host,
        port=redis_port,
        username=redis_username,
        password=redis_password,
        decode_responses=True,
    )

    # Identify the user
    user = getpass.getuser()
    
    # User Profile Key
    userkey = f"{appname}:profile:{user}"
    
    # App Stream
    streamkey = f"{appname}"

    # Check if the profile already exists for this app, 
    # if yes, increase the counter
    # if not, create the profile and increase the counter
    
    if r.exists(userkey) > 0:
        r.hincrby(userkey, "counter", 1)
    else:
        r.hset(userkey, mapping={"user": user, "counter": 1})
        r.hincrby(userkey, "counter", 1)

    r.xadd(
        streamkey,
        {
            "appname": appname,
            "user": user,
            "email" : email,
            "host": socket.gethostname(),
            "ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "unix_ts": time.mktime(datetime.now().timetuple()),
            "payload" : payload
        },
    )
