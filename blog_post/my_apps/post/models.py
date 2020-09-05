from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    date = models.DateField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return 'Post id: ' + str(self.id)
    