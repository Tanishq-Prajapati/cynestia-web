from django.shortcuts import render
from django.views import View
from .utility.validators import Validators
from .models import CustomModel, BlogDetail

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
        try:
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

            # now if there are No Errors i have found so i will register the model with details.
            a_contacting_inst = CustomModel(
                full_name=full_name,
                email_id=email,
                phone=phone,
                subject=subject,
                message=message
            )
            a_contacting_inst.save()

            print("ERROR NOT FOUND")
            return render(
                request,
                "contact.html",
                context={
                    "error":"NO",
                    "message":"Message sent successfully."
                }
            )
        except Exception as error:
            return render(
                request,
                "contact.html",
                context={
                    "error":"YES",
                    "message":"something went wrong, please try again."
                }
            )
        
# creating the endpoint for the blogs over here
class BlogsGrid(View):
    def get(self, request):
        # getting a list of all blogs over here
        all_blogs = BlogDetail.objects.all()
        return render(
            request,
            "blog.html",
            context={
                "blogs": all_blogs
            }
        )
    
# Accessing the blog from here
class BlogDetails(View):
    def get(self, request, slug):
        try:
            # getting the details of the blog
            contextual_data = {
                "blog_title":"Blog not found. invalid url",
                "blog_data":"",
                "blog_by":"",
                "uploaded_at":"",
                "views":0
            }
            blog = BlogDetail.objects.get(slug=slug)
            if not blog:
                return render(
                    request,
                    "bdetails.html",
                    context=contextual_data
                )
            else:
                print(blog.by)
                contextual_data["blog_data"] = blog.data
                contextual_data["blog_title"] = blog.title
                contextual_data["blog_by"] = blog.by
                contextual_data["uploaded_at"] = blog.uploaded_at
                contextual_data["views"] = str(blog.views)
            
            # now sending the response over here now with comments
            return render(
                request,
                "bdetails.html",
                context=contextual_data
            )
        except Exception as error:
            return render(
                request,
                "bdetails.html",
                context=contextual_data
            )
