from django.db import models

# Create your models here.
class LandingPage(models.Model):
    name = models.CharField(max_length=255)
    conversion_rate = models.DecimalField(max_digits=5, decimal_places=2)
    html = models.TextField()

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    user_ideas = models.TextField()
    traffic_description = models.TextField()
    base_landing_page = models.ForeignKey(LandingPage, on_delete=models.SET_NULL, null=True, blank=True, related_name="a_test")
    base_landing_page2 = models.ForeignKey(LandingPage, on_delete=models.SET_NULL, null=True, blank=True, related_name="b_test")
