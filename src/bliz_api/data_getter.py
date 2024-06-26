import requests
import time
from service.telebot import Telegram_log as Tellog

class Data_getter:

    def __init__(self, cfg) -> None:
        self.url = cfg['api_g']['url']
        self.headers = cfg['api_g']['headers']  
        self.tellog = Tellog(cfg)


    def get_cards(self):
        print('Start getting cards from Heartstone')
        start_time = time.time()
        response = requests.get(self.url, headers=self.headers)
        if response.ok:
            finish_time = time.time()
            print(f'Finish process. Time:{finish_time - start_time}')
            return response
        else:
            self.tellog.logger(f"Empty response. Code:{response.status_code}")
            return "Empty response"
    
    def get_cards_in_json(self):
        print('Start getting cards from Heartstone')
        start_time = time.time()
        response = requests.get(self.url, headers=self.headers)
        if response.ok:
            data = response.json()
            finish_time = time.time()
            print(f'Finish process. Time:{finish_time - start_time}')
            return data
        else:
            self.tellog.logger(f"Empty response. Code:{response.status_code}")
            return "Empty response"        
