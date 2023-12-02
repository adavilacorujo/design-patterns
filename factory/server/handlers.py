
import datetime

class GmailHandler():
    @classmethod
    def handle(self, route : str, payload : dict):
        routes = {}
        routes['authenticate'] = self._authenticate
        routes['events'] = self._events
        return routes[route](payload)

    def _authenticate(payload):
        return {
                'status_code': 200,
                'ok': True,
            }
    def _events(payload):
        return {
                "status_code": 200,
                "ok": True,
                "events": [
                {
                    'id': 1,
                    'title': 'Clean apartment',
                    'description': 'Need to clean apartment',
                    'date': datetime.datetime.now().__str__()
                }
            ]}
    
class YahooHandler():
    @classmethod
    def handle(self, route : str, payload : dict):
        routes = {}
        routes['authenticate'] = self._authenticate
        routes['events'] = self._events
        return routes[route](payload)

    def _authenticate(payload):
        return {
                'status_code': 200,
                'ok': True,
            }
    def _events(payload):
        return {
                "status_code": 200,
                "ok": True,
                "events": [
                {
                    'id': 1,
                    'title': 'Clean apartment',
                    'description': 'Need to clean apartment',
                    'date': datetime.datetime.now().__str__()
                }
            ]}    
    
class ProtonHandler():
    @classmethod
    def handle(self, route : str, payload : dict):
        routes = {}
        routes['authenticate'] = self._authenticate
        routes['events'] = self._events

        return routes[route](payload)

    def _authenticate(payload):
        return {
                'status_code': 200,
                'ok': True,
            }
    def _events(payload):
        return {
                "status_code": 200,
                "ok": True,
                "events": [
                {
                    'id': 1,
                    'title': 'Clean apartment',
                    'description': 'Need to clean apartment',
                    'date': datetime.datetime.now().__str__()
                }
            ]}    
    