from django.db import models
from cloudinary.models import CloudinaryField

class Destination(models.Model):
    """Destination model"""
    name = models.CharField(
        max_length=100,
        null=False,
        unique=True,
        verbose_name='Destination Name',
        help_text='Required. Max length: 100 characters'
    )
    description = models.TextField(
        null=False,
        verbose_name='Destination Description',
        help_text='Required'
    )
    location = models.CharField(
        max_length=100,
        null=False,
        verbose_name='Destination Location',
        help_text='Required. Max length: 100 characters'
    )

    class Meta:
        verbose_name = 'Destination'
        verbose_name_plural = 'Destinations'
        ordering = ['name']

    def __str__(self):
        return self.name

class DestinationImage(models.Model):
    """Destination image model"""
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Destination',
        help_text='Choose the destination for this image'
    )
    image = CloudinaryField(
        'destination_image',
        folder='destination_images',
        null=True,
        blank=True,
    )
    alt_text = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        unique=False,
        verbose_name='Alt text',
        help_text='Optional. Max length: 300 characters'
    )
    default_image = models.BooleanField(
        default=False,
        verbose_name='Default Image'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Is Active'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated at'
    )

    class Meta:
        """Meta class for Destination image model"""
        verbose_name = 'Destination image'
        verbose_name_plural = 'Destination images'
        ordering = ['destination']

    def __str__(self):
        """String representation of Destination image model"""
        return f"Image for {self.destination.name}"

    def save(self, *args, **kwargs):
        """Check if there is a default image"""
        super().save(*args, **kwargs)
        if self.default_image:
            for image in self.destination.images.all().exclude(id=self.id):
                image.default_image = False
                image.save()

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return 'static/images/default_destination_image.jpeg'  
    
    class Detailed_destination(models.Model):
        """Detailed Destination model"""
        name = models.CharField(
            max_length=100,
            null=False,
            unique=True,
            verbose_name='Destination Name',
            help_text='Required. Max length: 100 characters'
        )
        place = models.CharField(
            max_length=100,
            null=False,
            verbose_name='Place',
            help_text='Required. Max length: 100 characters'
        )
        days = models.IntegerField(
            default=5,
            verbose_name='Days'
        )
        price = models.DecimalField(
            max_digits=9,
            decimal_places=2,
            default=20000,
            verbose_name='Price'
        )
        rating = models.DecimalField(
            max_digits=3,
            decimal_places=2,
            default=5.0,
            verbose_name='Rating'
        )
        description = models.TextField(
            null=False,
            verbose_name='Description',
            help_text='Required'
        )
        reviews = models.TextField(
            null=True,
            blank=True,
            verbose_name='Reviews'
        )
        package_instructions = models.TextField(
            null=True,
            blank=True,
            verbose_name='Package Instructions'
        )