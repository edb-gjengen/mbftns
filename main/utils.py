import random, string
import hashlib

from main.models import UserPass

def generate_username():
    # FIXME dangerous and stupid @ above 5k usernames
    length = 4
    username = "guest{0}".format(''.join(random.choice(string.digits) for x in range(length)))
    # unique
    if len(UserPass.objects.filter(username=username)) == 0:
        return username
    else:
        return generate_username()

def generate_password():
    myrg = random.SystemRandom()
    length = 8
    alphabet = string.letters[0:52] + string.digits
    pw = str().join(myrg.choice(alphabet) for _ in range(length))
    return pw

def ntpass_hash(raw_password):
    # found in the wild.
    nt_password = hashlib.new('md4', raw_password.encode('utf-16le')).hexdigest()
    return nt_password
