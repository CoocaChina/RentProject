
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ruhrAdmin',
        'USER': 'ruhr_test',
        'PASSWORD': 'Ruhr@1234',
        'HOST': '47.100.162.9',
        'PORT': '3306',
    }
}
redis_database = {"host": "10.84.100.23", "port": "6379", "password": "XXXXX"}
baseUrl ='http://ops-test.yunx.ruhrtech.com'

