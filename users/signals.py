from django.db.models.signals import post_save
from .models import User, InstructorProfile, StudentProfile
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if instance.is_student:
		StudentProfile.objects.get_or_create(user = instance)
	else:
		InstructorProfile.objects.get_or_create(user = instance)
	

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	if instance.is_student:
		instance.student_profile.save()
	else:
		InstructorProfile.objects.get_or_create(user = instance)