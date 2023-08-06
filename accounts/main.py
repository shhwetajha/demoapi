import os
from twilio.rest import Client
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def sendsms(self):
    account_sid="ACf822c736e9a8462b1610f30a14897211"
    auth_token="129512f6eb53fff3e3c8fca21c1453a2"
    client=Client(account_sid,auth_token)
    message=client.messages.create(body="Congrats!,your api is working",from_='+14066258166',to='+919354523215')
    print(message.sid)
    return Response({'data':message.sid})