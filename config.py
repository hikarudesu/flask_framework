class SystemConfig:

  DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
      'user': 'hikaru',
      'password': 'hikaru',
      'host': 'localhost',
      'db_name': 'db'
  })

Config = SystemConfig