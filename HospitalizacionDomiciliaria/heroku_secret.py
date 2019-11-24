import random
secret="".join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
print("heroku config:set SECRET_KEY=\"{0}\"".format(secret))
