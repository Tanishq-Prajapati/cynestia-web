from django.shortcuts import render
from django.views import View
from .utility.validators import Validators

# Create your views here.
validator = Validators()

class CustomView(View):
    def get(self, request):
        return render(
            request,
            "index.html"
        )
    
class ContactView(View):
    def get(self, request):
        return render(
            request,
            "contact.html"
        )

    def post(self, request):
        # getting the form DATA over here
        full_name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        print(subject)

        message = request.POST.get("message")

        # errors over here
        form_errors = {
            "name":validator.valdiate_full_name(full_name),
            "email":validator.validate_email_id(email),
            "phone":validator.phone_number(phone),
            "subject":validator.subject(subject),
            "message":validator.subject(message)
        }

        # iterating on error over here
        for a_error in form_errors.values():
            if a_error:
                print("ERROR FOUND")
                return render(
                    request,
                    "contact.html",
                    context={
                        "error":"YES",
                        "message":a_error
                    }
                )

        print("ERROR NOT FOUND")
        return render(
            request,
            "contact.html",
            context={
                "error":"NO",
                "message":"Message sent successfully."
            }
        )