from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffetiera: Nuevo mensaje de cpntacto",#Asunto del mensaje
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content),#cuerpo,
                "no-contestar@inbox.mailtrap.io",#email_origen,
                ["fran_fran14@hotmail.com"], #email_destino,
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")
            

    return render (request, "contact/contact.html" , {'form':contact_form})
