from django.db import models
from users.models import User
from documents.models import Document

class AccessControl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    permission = models.CharField(max_length=50)  # e.g., "read", "write", "delete"
