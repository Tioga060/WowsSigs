import mongoengine

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$c#)@f@nv845343(*7)cj-xqweesssdfsdvdfyihfbet_sdfaser5nio.kj^'

_MONGODB_USER = 'mongouser'
_MONGODB_PASSWD = 'password'
_MONGODB_HOST = 'localhost:27017'
_MONGODB_NAME = 'wows_sigs'
_MONGODB_DATABASE_HOST = \
    'mongodb://%s:%s@%s/%s' \
    % (_MONGODB_USER, _MONGODB_PASSWD, _MONGODB_HOST, _MONGODB_NAME)

mongoengine.connect(_MONGODB_NAME, host=_MONGODB_DATABASE_HOST)
