import yaml
from bliz_api.data_getter import Data_getter
from service.service import Service 


try:
    with open('config.yml') as c:
        config = yaml.safe_load(c)
except OSError as err:
    print("OS error:{0}".format(err))


cards = Data_getter(config).get_cards_in_json()
if cards != "Empty response":
    Service(config).set_data_in_database(cards)