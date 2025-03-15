from django.db import models

NATIONALITY_CHOICES = (
    ("USA", "United States"),
    ("BR", "Brazil"),
    ("FR", "France"),
    ("DE", "Germany"),
    ("IT", "Italy"),
    ("ES", "Spain"),
    ("MX", "Mexico"),
    ("PT", "Portugal"),
    ("GB", "United Kingdom"),
    ("CA", "Canada"),
    ("AU", "Australia"),
    ("AR", "Argentina"),
    ("PE", "Peru"),
    ("CL", "Chile"),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name
