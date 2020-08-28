from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(default='',max_length=100, null=True, blank=True)
	cover_photo = models.ImageField(default='default.jpg', upload_to='cover_pic')
	profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
	phone_number = models.CharField(max_length=10,null=True,blank=True)
	whatsapp_number = models.CharField(max_length=10,null=True,blank=True)
	facebook = models.URLField()
	linked_in = models.URLField()



	def __str__(self):
		return f'{self.user.username} Profile'

	def get_absolute_url(self):
		return reverse('profile', kwargs={'username': self.user.username})


	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		img = Image.open(self.profile_pic.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.profile_pic.path)