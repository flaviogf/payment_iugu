import configparser

cfg = configparser.ConfigParser()
cfg.read('settings.ini')
cfg = cfg['DEFAULT']

CLIENT_ID = cfg.get('CLIENT_ID')
CLIENT_SECRET = cfg.get('CLIENT_SECRET')
SECRET_KEY = cfg.get('SECRET_KEY')
