from django.shortcuts import render
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from django.http import HttpResponse

# Create your views here.
account_sid = 'ACe5b1956988bcc540eb356ccf1af62d8f' 
auth_token = 'dccda33f170266dc0708df9d2d4bcaff' 
client = Client(account_sid, auth_token)
@csrf_exempt
def bott(request):
    message = request.POST['Body'].lower()
    sender_name = request.POST['ProfileName']
    sender_num = request.POST['From']
    print (request.POST)
    print (message)
    responded = False
    
    if message == "hola" in message:
        message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body="Bien venido 🙌 {},  servicio de chat\n automatico 🤖 de Laboratorios clinicos semin \n para continuar porfavor mande la palabra  *continuar*".format(sender_name),      
                              to=sender_num
                          ) 
        responded = True
    if message == "continuar" in message:
            message = client.messages.create(
            from_='whatsapp:+14155238886',  
            body='''👏Gracias {} por continuar\n por favor eliga una de las siguientes opciones\n   🔬1.-ver catalogo de estudios disponibles\n   🎁2.-ver promociones disponibles \n   📕3.-realizar una cita \n   📞4.-contactar a persona fisica\n para elegir la opcion desada solo \n escriba el numer que tiene la opcion.\n elemplo : 1'''.format(sender_name),
                to=sender_num
                          )
            responded = True
    if message== '4' in message:
            message = client.messages.create(
            from_='whatsapp:+14155238886',  
            body='📝Para poder contactar a un personal de soporte fisico por favor marcque el siguiente numero de contacto 22222255454 ☎',
            to=sender_num
                          )
            responded = False
    elif message== '3' in message:
            message = client.messages.create(
            from_='whatsapp:+14155238886',  
            body='📝Has seleccionado la opcion 3 muy bien crack 😘',
            to=sender_num
                          )
            responded = True
            


    return HttpResponse("👍")
    