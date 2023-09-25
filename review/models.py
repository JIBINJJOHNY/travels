from django.db import models
from django.contrib.auth.models import User  # Assuming you are using the built-in User model

class Review(models.Model):
    destination = models.ForeignKey(
        'Destination',
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Destination',
        help_text='Select the destination for this review'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='User',
        help_text='Select the user who wrote this review'
    )
    rating = models.PositiveIntegerField(
        default=5,
        verbose_name='Rating',
        help_text='Enter a rating between 1 and 5'
    )
    comments = models.TextField(
        verbose_name='Comments',
        help_text='Enter your comments about the destination'
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
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-created_at']

    def __str__(self):
        return f'Review by {self.user.username} for {self.destination.name}'
