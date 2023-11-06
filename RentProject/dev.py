
DEBUG = True
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
# **** redis数据库配置 ****
redis_database = {"host": "127.0.0.1", "port": "6379", "password": "XXXXXX"}
baseUrl ='http://ops-test.yunx.ruhrtech.com'

