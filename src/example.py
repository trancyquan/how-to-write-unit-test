from datetime import datetime
import time
import os
from src.dataset import load_data
from src.db_connection import DBConnector


def sleep_awhile(duration):
    """sleep for couple of seconds"""
    time.sleep(duration)
    # some other processing steps  
 
def get_time_of_day():
    """return string Night/Morning/Afternoon/Evening depending on the hours range"""
    time = datetime.now()
    if 0 <= time.hour <6:
        return "Night"
    if 6 <= time.hour < 12:
        return "Morning"
    if 12 <= time.hour <18:
        return "Afternoon"
    return "Evening"

def process_data():
    data = load_data()
    # process the data in certain ways ...
    processed_data = data["key1"]
    return processed_data

class Engine:
    def __init__(self):
        self.connector = DBConnector()

    def load_data(self):
        data = self.connector.get(123)
        print(data)
        # do some processing
        data = data + "xxx"
        return data

def use_env_var():
    contract_class = os.environ['CONTRACT_CLASS']
    if contract_class == 'en_cloud':
        # do some processing
        return "this is en_cloud"
    if contract_class == 'en_onprem':
        # do some processing
        return "this is en_onprem"
    raise ValueError(f"contract class {contract_class} not found")

def use_thirdparty_func():
    """assuming you are using a thrid party library & that throws some corner case exception (ValueError)
    You would like to test whether the corner case exception can be catched"""
    try:
        time.sleep(4)
    except ValueError as e:
        print(e)
