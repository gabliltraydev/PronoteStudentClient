import pronotepy

try:
    client = pronotepy.Client(
        'pronote.url',
        username='test',
        password='test',
    )
    print(client.start_day)
except pronotepy.CryptoError:
    exit(1)  # the client has failed to log in

if not client.logged_in:
    exit(1)  # the client has failed to log in


