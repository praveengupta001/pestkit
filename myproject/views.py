from django.http import HttpResponse
from django.shortcuts import render, redirect
# from contactApp.models import Contactform
from django.core.mail import EmailMultiAlternatives


from django.template.loader import render_to_string
from django.shortcuts import render
from contactdetails.models import Contact

def HomePage(request):
  # show recent contacts on index page
  # recent = Contactform.objects.order_by('-created_at')[:6]
  return render(request,"index.html",)

def aboutPage(req):
  return render(req,"about.html")

def servicePage(req):
  return render(req, 'service.html')

def projectPage(req):
  return render(req, 'project.html')

def blogPage(req):
  return render(req, 'blog.html')

def pricePage(req):
  return render(req,'price.html')

def teamPage(req):
  return render(req,'team.html')

def testimonialPage(req):
  return render(req, 'testimonial.html')



# def contactPage(req):
#   if req.method == 'POST':
#     fullname = req.POST.get('fullname')
#     email = req.POST.get('email')
#     phone = req.POST.get('phone')
#     message = req.POST.get('message')
#     image = None
#     attachment = None
#     if 'image' in req.FILES:
#       image = req.FILES['image']
#     if 'attachment' in req.FILES:
#       attachment = req.FILES['attachment']
#     if fullname and email and message:
#       Contactform.objects.create(fullname=fullname, email=email, phone=phone, message=message, image=image, attachment=attachment)
#       return render(req, 'contact.html', {'success': True})
#   return render(req, 'contact.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        subject = request.POST.get('usersubject')
        message = request.POST.get('usertext')

        # Save contact to database
        allData = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        allData.save()

        # Create HTML email content
        html_content = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        })

        # Plain text fallback
        text_content = (
            f"Dear {name},\n\n"
            "Thank you for contacting Sangam University. "
            "We have received your message and will get back to you soon.\n\n"
            "Best regards,\nSangam University Support Team"
        )

        # Send confirmation email to user
        user_email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email="praveengupta6450@gmail.com",
            to=[email],
        )
        user_email.attach_alternative(html_content, "text/html")
        user_email.send(fail_silently=False)

        # Send notification to admin
        admin_subject = f"New Contact Form Submission from {name}"
        admin_message = (
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Subject: {subject}\n"
            f"Message:\n{message}\n"
        )

        admin_email = EmailMultiAlternatives(
            subject=admin_subject,
            body=admin_message,
            from_email="praveengupta6450@gmail.com",
            to=["praveengupta6450@gmail.com"],
        )
        admin_email.send(fail_silently=False)



        return HttpResponse("<script>alert('Thank you for your message!')</script>")

    
    return render(request, 'contact.html')
