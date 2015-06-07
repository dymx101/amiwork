import pygn

clientID = '13118464-4E8A3151390D6E9F3979F8715F51F7F3' # Enter your Client ID from developer.gracenote.com here
userID = '27678420343239243-6E83356B7E66B2E6A2BF0B9B54C551AD' # Get a User ID from pygn.register() - Only register once per end-user

exit(0)
userID = pygn.register(clientID)
print userID