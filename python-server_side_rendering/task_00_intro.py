import os
import logging

def generate_invitations(template, attendees):
    
    if not isinstance(template, str):
        logging.error("Invalid input: template must be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        logging.error("Invalid input: attendees must be a list of dictionaries.")
        return

    
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return
    
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return
    
    for index, attendee in enumerate(attendees, start=1):
        invitation = template
        for key in {'name', 'event_title', 'event_date', 'event_location'}:
            value = attendee.get(key, '')
            if value == None:
                value = 'N/A'
            invitation = invitation.replace('{', '')
            invitation = invitation.replace('}', '')
            invitation = invitation.replace(key, value)

        result = f'output_{index}.txt'
        try:
            with open(result, 'w') as file:
                file.write(invitation)
        except Exception as e:
            raise Exception('Could not open file')

