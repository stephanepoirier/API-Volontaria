from django.conf import settings
from ics import Calendar, Event

def generate_participation_ics(participation, path_event_file):
    calendar = Calendar()
    event = Event()

    event.name = settings.CONSTANT["CALENDAR_EVENT_NAME"] + \
                 participation.event.cycle.name
    event.begin = participation.event.start_date
    event.end = participation.event.end_date
    calendar.events.add(event)

    # create a ics file
    with open(path_event_file, 'w') as my_file:
        my_file.writelines(calendar)