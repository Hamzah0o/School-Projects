from twilio.rest import Client

account_sid = 'AC21ce80937c471dc8' #account_sid
auth_token = '[Insert your token]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_ = '+13132087829' ,
    body='Heloo I love you baby', #nessaeg
    to = '' ) #phone number

print(message.sid)