from datetime import datetime


from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser, FacultyHomePage, FacultyPage, StudentHomePage, StudentPage, AlumniHomePage, AlumnusPage, StaffHomePage, StaffPage

######################################################

@receiver(post_save, sender=CustomUser) #Can't use pre save cuz then user model won't be created and then the user onetoonekey field will raise error
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		if instance.user_type == '0':
			home = FacultyHomePage.objects.all()[0]  # Now be careful here as if there will be more than one facultyHomePage then there will be a problem

			base_slug = instance.username
			if not instance.email:
				mail_id=instance.username + "@iitg.ac.in"
			else:
				mail_id=instance.email
			website='http://www.iitg.ac.in'
			new_faculty = FacultyPage(
				title= instance.first_name +" "+ instance.last_name,
				slug=FacultyPage()._get_autogenerated_slug(base_slug),
				user=instance,
				first_name=instance.first_name,
				last_name=instance.last_name,
				email_id=mail_id,
				website=website,
			)
			home.add_child(instance=new_faculty)
			home.save()
		elif instance.user_type == '1':
			home = StudentHomePage.objects.all()[0]
			base_slug = instance.username
			enrolment_year = datetime.strptime('Aug 1 20'+base_slug[0:2]+' 12:00PM', '%b %d %Y %I:%M%p')
			PROG = {'01':'0', '41':'1', '61':'2'}
			try:
				programme = PROG[base_slug[2:4]]
			except KeyError:
				programme = '3'

			if not instance.email:
				mail_id=instance.username + "@iitg.ac.in"
			else:
				mail_id=instance.email
			new_student = StudentPage(
				title= instance.first_name +" "+ instance.last_name,
				slug=StudentPage()._get_autogenerated_slug(base_slug),
				user=instance,
				first_name=instance.first_name,
				last_name=instance.last_name,
				email_id=mail_id,
				roll_no=base_slug, #see some lines above
				enrolment_year=enrolment_year,
				programme=programme,
			)
			home.add_child(instance=new_student)
			home.save()
		elif instance.user_type == '2':
			home = AlumniHomePage.objects.all()[0]
			base_slug = instance.username
			enrolment_year = datetime.strptime('Aug 1 20'+base_slug[0:2]+' 12:00PM', '%b %d %Y %I:%M%p')
			PROG = {'01':'0', '41':'1', '61':'2'}
			try:
				programme = PROG[base_slug[2:4]]
			except KeyError:
				programme = '3'

			if not instance.email:
				mail_id=instance.username + "@iitg.ac.in"
			else:
				mail_id=instance.email
			new_alum = AlumnusPage(
				title= instance.first_name +" "+ instance.last_name,
				slug=AlumnusPage()._get_autogenerated_slug(base_slug),
				user=instance,
				first_name=instance.first_name,
				last_name=instance.last_name,
				email_id=mail_id,
				roll_no=base_slug, #see some lines above
				enrolment_year=enrolment_year,
				programme=programme,
			)
			home.add_child(instance=new_alum)
			home.save()
		elif instance.user_type == '3':
			home = StaffHomePage.objects.all()[0]
			base_slug = instance.username
			if not instance.email:
				mail_id=instance.username + "@iitg.ac.in"
			else:
				mail_id=instance.email
			new_staff = StaffPage(
				title= instance.first_name +" "+ instance.last_name,
				slug=StaffPage()._get_autogenerated_slug(base_slug),
				user=instance,
				first_name=instance.first_name,
				last_name=instance.last_name,
				email_id=mail_id,
			)
			home.add_child(instance=new_staff)
			home.save()
		else:
			pass
