from django.db import models
from django.urls import reverse

# Create your models here.
class Poem(models.Model):
    title = models.CharField(help_text='Enter the title for the poem.', max_length=50)
    poet = models.CharField(help_text="Enter the poet/author name.", max_length=50)
    slug = models.SlugField(help_text="User for url config", max_length=63)
    poem = models.TextField()

    class Meta:
        unique_together=(('title','poet'),)
        ordering = ['-title']

    def get_absolute_url(self):
        return reverse('poem:detail', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('poem:delete', kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('poem:update', kwargs={'slug':self.slug})