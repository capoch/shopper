from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.

def upload_location(obj, filename):
    return "%s/%s" %(obj.id,filename)

class Item(models.Model):
    item_name = models.CharField(max_length=250)
    description = models.CharField(null=True, blank=True, max_length=250)
    amount = models.CharField(null=True, blank=True, max_length=250)
    image = models.ImageField(upload_to = upload_location, null=True, blank=True, height_field="image_height", width_field="image_width")
    image_height = models.IntegerField(default=300)
    image_width = models.IntegerField(default=300)
    private = models.BooleanField(default=False)
    pending = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="updated_user",null=True, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by = models.ForeignKey('auth.User', related_name='items', on_delete=models.CASCADE)
    due_date = models.DateField(null=True, blank=True)
    finalized = models.DateTimeField(null=True, blank=True)
    finalized_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="finalized_user", null=True, blank=True)


    class Meta:
        ordering = ['-pending','-due_date','-updated', 'created']

    def __str__(self):
        return self.item_name

    # def get_absolute_url(self):
    #     return reverse('shoppinglist:detail', kwargs = {"id": self.id}) #namespace:url_name


    def buy(self):
        self.pending = False
        self.finalized = timezone.now
