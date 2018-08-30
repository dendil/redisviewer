import redis

r = redis.Redis(
    host='localhost',
    port=6379)


def viewkey(job):

    keystuff = r.hgetall(str(job) + "-state")
    return keystuff

def set2error(job):

    keystuff = r.hset(str(job) + "-state", "man-stoped", "ERROR")
    return
