import re

def email_sender(text):
    match = re.search('From: .*<(.*)>', text)
    if match:
        return match.group(1)
    return None

def email_recipient(text):
    match = re.search('To: .*<(.*)>', text)
    if match:
        return match.group(1)
    return None

def email_subject(text):
    match = re.search('Subject:\s*(.*)', text)
    if match:
        return match.group(1)
    return None

def email_body(text):
    match = re.search('\n\n(.*)$', text, re.DOTALL) #dot matches \n
    if match:
        return match.group(1)
    return None


