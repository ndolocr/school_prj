from django.db import models

# Create your models here.

"""
This is the design of the school model

School
	- name
	- location
	- created_on
	- school_type (Gov, or Private)
	- school_category (primary, secondary, nursery, junior_secondary)
"""
class School(models.Model):
    COUNRY_CHOICES = [        
        ("Lamu", "Lamu"),
        ("Meru", "Meru"),
        ("Embu", "Embu"),
        ("Kisii", "Kisii"),
        ("Bomet", "Bomet"),
        ("Narok", "Narok"),
        ("Nyeri", "Nyeri"),
        ("Kitui", "Kitui"),
        ("Kwale", "Kwale"),
        ("Wajir", "Wajir"),
        ("Nandi", "Nandi"),
        ("Busia", "Busia"),
        ("Siaya", "Siaya"),
        ("Kiambu", "Kiambu"),
        ("Isiolo", "Isiolo"),
        ("Kilifi", "Kilifi"),
        ("Nakuru", "Nakuru"),
        ("Vihiga", "Vihiga"),
        ("Kisumu", "Kisumu"),
        ("Migori", "Migori"),
        ("Nairobi", "Nairobi"),
        ("Nyamira", "Nyamira"),
        ("Baringo", "Baringo"),
        ("Samburu", "Samburu"),
        ("Turkana", "Turkana"),
        ("Garissa", "Garissa"),
        ("Mombasa", "Mombasa"),
        ("Mandera", "Mandera"),
        ("Makueni", "Makueni"),
        ("Kajiado", "Kajiado"),
        ("Kericho", "Kericho"),
        ("Bungoma", "Bungoma"),
        ("Homa Bay", "Homa Bay"),
        ("Kakamega", "Kakamega"),
        ("Laikipia", "Laikipia"),
        ("Marsabit", "Marsabit"),
        ("Machakos", "Machakos"),
        ("Murang’a", "Murang’a"),        
        ("Kirinyaga", "Kirinyaga"),
        ("Nyandarua", "Nyandarua"),        
        ("Tana River", "Tana River"),
        ("West Pokot", "West Pokot"),
        ("Trans-Nzoia", "Trans-Nzoia"),
        ("Uasin Gishu", "Uasin Gishu"),
        ("Tharaka-Nithi", "Tharaka-Nithi"),
        ("Taita Taveta", "Taita Mak Taveta"),
        ("Elgeyo-Marakwet", "Elgeyo-Marakwet"),
        
    ]
    SCHOOL_FOR_CHOICES = [
        ("Boys", "Boys"),
        ("Girls", "Girls"),
        ("Mixed", "Mixed"),
        ("Special School", "Special School"),
    ]
    SCHOOL_TYPE_CHOICES = [
        ("Public", "Public"),
        ("Private", "Private"),
    ]
    SCHOOL_CATEGORY_CHOICES = [
        ("Nursery", "Nursery"),
        ("Primary", "Primary"),
        ("Secondary", "Secondary"),
        ("Baby class", "Baby class"),
        ("Junior Secondary", "Junior Secondary"),

    ]
    
    name = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=True)
    school_type = models.CharField(max_length=255, choices=SCHOOL_TYPE_CHOICES, null=False)
    school_category = models.CharField(max_length=255, choices=SCHOOL_CATEGORY_CHOICES, null=False)
    county = models.CharField(max_length=255, choices=COUNRY_CHOICES, null=False, default="Mombasa")
    school_for = models.CharField(max_length=255, choices=SCHOOL_FOR_CHOICES, null=False, default="Mixed")

    updated_on = models.DateTimeField( auto_now = True)
    created_on = models.DateTimeField( auto_now_add = True)

    def __str__(self):
        return self.name + " - " + self.location