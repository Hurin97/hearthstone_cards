import yaml
from telebot import Telegram_log

with open('config.yml') as c:
        config = yaml.safe_load(c)

tellog = Telegram_log(config)

tellog.logger("lol")