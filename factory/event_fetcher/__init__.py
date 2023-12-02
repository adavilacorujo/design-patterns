
from .handlers import GmailConnection, YahooConnection, ProtonConnection

class Events:
    """
    
    """
    def __init__(self):
        self.objects = {}
        self._connect()

    def _connect(self):
        """
        connect to all services
        """
        self.objects['gmail'] = GmailConnection()
        print('[*] connected to gmail')
        self.objects['yahoo'] = YahooConnection()
        print('[*] connected to yahoo')
        self.objects['proton'] = ProtonConnection()
        print('[*] connected to proton')


    def events(self):
        """
        get events for all calendars
        """
        events = []
        for key in self.objects.keys():
            events.extend(self.objects.get(key).get_events())
        return events