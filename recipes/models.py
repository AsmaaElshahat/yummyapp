from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse


class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='recipes_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    ingredients = models.TextField(blank=True)
    steps = models.TextField(blank=True)
    duration = models.TextField(blank=True)
    servings = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True,db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='recipes_liked',
                                        blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('recipes:detail', args=[self.id, self.slug])
