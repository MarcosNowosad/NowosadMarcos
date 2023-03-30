from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages
from portafolio.settings import EMAIL_HOST_USER
# Create your views here.

def contact(request):
    if request.method== 'POST':
        subject = request.POST['subject']
        message = request.POST['message'] + " Direccion de correo " + request.POST['email'] + " De " + request.POST['name']
        from_email = EMAIL_HOST_USER
        
        # if subject and message and from_email:
        recipient_list= ['nowosadmarcos9@gmail.com']
        send_mail(subject,message, from_email, recipient_list)

        if request.method == 'POST':
            messages.success(request, "Thanks for contacting me")
            return redirect('contactos')
     
    return render(request, 'contact.html')