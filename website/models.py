import re
from django.db import models


class Enquiry(models.Model):

    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('closed', 'Closed'),
    ]

    name = models.CharField(max_length=200)

    email = models.EmailField(db_index=True)

    phone = models.CharField(max_length=20, db_index=True)

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

        constraints = [
            models.UniqueConstraint(
                fields=['email', 'phone'],
                name='unique_email_phone_enquiry'
            )
        ]

    def save(self, *args, **kwargs):

        if self.email:
            self.email = self.email.strip().lower()

        if self.phone:
            digits_only = re.sub(r'\D', '', self.phone.strip())

            if digits_only.startswith('91') and len(digits_only) == 12:
                digits_only = digits_only[2:]

            self.phone = digits_only

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.phone}"


class GalleryProject(models.Model):

    CATEGORY_CHOICES = [
        ('cctv', 'CCTV'),
        ('fire', 'Fire Safety'),
        ('biometric', 'Biometric'),
        ('solar', 'Solar'),
        ('enterprise', 'Enterprise'),
        ('maintenance', 'Maintenance'),
    ]

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    image = models.ImageField(upload_to='gallery/')

    location = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title