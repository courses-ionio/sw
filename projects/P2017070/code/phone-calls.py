# kwdikas mesw tou opoiou mporoun na ginoun kliseis apo ena thlefwno sto diko mou 
from twilio.rest import Client

account_sid = 'ACd20c68b5a047e9a1357e3e6b1f09afa0'
auth_token = '77dd84d215d5124a01ae1e51b740b93c'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+306972653045',
                        from_='12057406383'
                    )

print(call.sid)

