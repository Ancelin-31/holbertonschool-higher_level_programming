import os

def generate_invitations(template, attendees):
    
    if not isinstance(template, str):
        raise TypeError('The template must be a string')
    
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        raise TypeError('Attendees must be a list of dictionaries')
    
    if not template.strip():
        raise ValueError('Template is empty')
    
    if not attendees:
        raise ValueError('No data given')
    
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

