# get user email address
# slice out username
# slice out domain
# format message
# display output message

email_validator = False
while not email_validator:
    email = input("What is your email address: ").strip()
    if '@' in email:
        email_validator = True
    else:
        print("This is not correct email address")

username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print("Your username is: {} and domain: {}".format(username, domain))
