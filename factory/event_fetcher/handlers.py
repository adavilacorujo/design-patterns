import os
import abc
import math
import requests
from datetime import datetime, timedelta

from dotenv import load_dotenv
load_dotenv('../.env')

headers = {"Content-Type": "application/json"}

class Connection(metaclass=abc.ABCMeta):
    """
    abstract class for connecting to apis
    """
    def connect(self, **config):
        """
        connect to api
        """
        pass

    def get_events(self, **config):
        """
        fetch events in the calendar
        """
        return [{}]


class GmailConnection(Connection):
    def __init__(self):
        self.last_conencted = datetime
        self.API_KEY = os.getenv('GMAIL_API_KEY')
        self.username = os.getenv('gmail_username')
        self.password = os.getenv('gmail_password')
        self.connect()

    def connect(self):
        # return if already authenticated
        if math.ceil((datetime.now() - (datetime.now() - timedelta(hours=3))).seconds/3600) < 2:
            # it's been less than two hours since last connection
            return True
        
        payload = {
            'api_key': self.API_KEY,
            'username': self.username,
            'password': self.password
        }
        response = requests.post(
                    'http://localhost:8000/gmail/authenticate',
                    json=payload,
                    headers=headers
                    )
        response_dict = response.json()
        if not response_dict.get('ok', False): 
            raise ConnectionError('Could not authenticate with Gmail server')
    
        self.last_conencted = datetime.now()

    def get_events(self, **config):
        payload = {
            'api_key': self.API_KEY
        }
        response = requests.post(
                'http://localhost:8000/gmail/events',
                json=payload,
                headers=headers
                )

        response_dict = response.json()
        if not response_dict.get('ok', False): 
            raise ConnectionError('Could not get events from Gmail server')
    
        return response_dict.get('events', [])

class YahooConnection(Connection):
    def __init__(self):
        self.last_conencted = datetime
        self.API_KEY = os.getenv('YAHOO_API_KEY')
        self.username = os.getenv('yahoo_username')
        self.password = os.getenv('yahoo_password')
        self.connect()

    def connect(self):
        # return if already authenticated
        if math.ceil((datetime.now() - (datetime.now() - timedelta(hours=1))).seconds/3600) < 1:
            # it's been less than two hours since last connection
            return True
        
        payload = {
            'api_key': self.API_KEY,
            'username': self.username,
            'password': self.password
        }
        response = requests.post(
                    'http://localhost:8000/yahoo/authenticate',
                    json=payload,
                    headers=headers
                    )
        response_dict = response.json()
        if not response_dict.get('ok', False): raise ConnectionError('Could not authenticate with Yahoo server')
    
        self.last_conencted = datetime.now()

    def get_events(self):
        payload = {
            'api_key': self.API_KEY
        }
        response = requests.post(
                'http://localhost:8000/yahoo/events',
                json=payload,
                headers=headers
                )

        response_dict = response.json()
        if not response_dict.get('ok', False): 
            raise ConnectionError('Could not get events from Yahoo server')
    
        return response_dict.get('events', [])
    
class ProtonConnection(Connection):
    def __init__(self):
        self.last_conencted = datetime
        self.API_KEY = os.getenv('PROTON_API_KEY')
        self.username = os.getenv('proton_username')
        self.password = os.getenv('proton_password')
        self.connect()

    def connect(self):
        # return if already authenticated
        if math.ceil((datetime.now() - (datetime.now() - timedelta(hours=1))).seconds/3600) < 1:
            # it's been less than two hours since last connection
            return True
        

        payload = {
            'api_key': self.API_KEY,
            'username': self.username,
            'password': self.password
        }
        response = requests.post(
                    'http://localhost:8000/proton/authenticate',
                    json=payload,
                    headers=headers
                    )
        response_dict = response.json()
        if not response_dict.get('ok', False): raise ConnectionError('Could not authenticate with Proton server')
    
        self.last_conencted = datetime.now()

    def get_events(self):
        payload = {
            'api_key': self.API_KEY
        }
        response = requests.post(
                'http://localhost:8000/proton/events',
                json=payload,
                headers=headers
                )

        response_dict = response.json()
        if not response_dict.get('ok', False): 
            raise ConnectionError('Could not get events from Proton server')
    
        return response_dict.get('events', [])

