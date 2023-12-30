from django.db import models

class PrimaryData(models.Model):
    Lead_Status = models.CharField(max_length=100, primary_key=True)
    duplicate_lead = models.CharField(max_length=100)
    new_lead = models.CharField(max_length=100)
    grand_total = models.CharField(max_length=100)
    overall_qualification = models.CharField(max_length=100)
    new_lead_qualification = models.CharField(max_length=100)

    class Meta:
        db_table = 'primary_data'


