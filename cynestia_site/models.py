import uuid
from django.db import models

# Create your models here.
class CustomModel(models.Model):
    full_name = models.CharField(max_length=100,blank=False)
    email_id = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=50, blank=False)
    subject = models.CharField(max_length=200, blank=False)
    message = models.TextField(blank=False)

    def __str__(self) -> str:
        return f"{self.full_name}, {self.email_id}"
    
# creating a DB-Schema for Blog Details
class BlogDetail(models.Model):
    bid = models.UUIDField(default=uuid.uuid4, unique=True)
    by = models.CharField(blank=False,max_length=50,null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=False)
    slug = models.CharField(
        blank=False,
        max_length=200,
        unique=True,
        primary_key=True,
        null=False
    )
    title = models.CharField(
        blank=False,
        max_length=200,
        unique=False,
        primary_key=False
    )
    data = models.TextField(blank=False)
    views = models.IntegerField()

    # creating a function for the decoration of row
    def __str__(self) -> str:
        return f"{self.title} ({self.bid})"

# creating a DB-Schema for Blog-Comments
class BlogComment(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    ip_addr = models.GenericIPAddressField(
        protocol="both",
        unpack_ipv4=True,
        null=False,
        blank=False,
        unique=True
    )
    comment_data = models.TextField(null=False)
    comment_of = models.ForeignKey(
        BlogDetail,
        related_name="comments",
        on_delete=models.CASCADE
    )