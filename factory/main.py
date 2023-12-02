'''
This file implements the factory method using email accounts as the example
'''
from event_fetcher import Events


if __name__ == '__main__':
    # Get events for each of them
    calendar_events = Events()
    all_events = calendar_events.events()
    print(all_events)