# Write a program that uses regular expressions to fetch and print:

# sender email address
# recipient email address
# email subject
# email body
import emails

try:
    with open('email.txt', 'r') as f:
        email_text = f.read()

    # Fetch and print the required fields
    sender = emails.email_sender(email_text)
    recipient = emails.email_recipient(email_text)
    subject = emails.email_subject(email_text)
    body = emails.email_body(email_text)

    # Print the results
    print(f"Sender: {sender}")
    print(f"Recipient: {recipient}")
    print(f"Subject: {subject}")
    print(f"Body:\n{body}")
    
except Exception as e:
    print(f"An error occurred: {e}")
