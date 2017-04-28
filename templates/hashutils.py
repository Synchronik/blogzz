import random
import string
import hashlib
import hmac

def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = ''.join(random.choice(string.letters) for x in xrange(5))

    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)
