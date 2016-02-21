#连接mongoDB
from django.conf import settings
try:
    from mongoengine import connect
    connect(db=settings.ACCOUNT_MONGO['DB'],
                    host=settings.ACCOUNT_MONGO['HOST'],
                    port=settings.ACCOUNT_MONGO['PORT'])
except:
    print('[WARNING]: You have not installed mongoengine. App\'s data store will not be used. Please use "easy_install mongoengine" or "pip install mongoengine" to install it')