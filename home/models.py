from django.db import models
# Create your models here.
statusChoice = ((1, 'Show'), (2, 'Hide'))
class newCatagory(models.Model):
	cat_name = models.CharField(max_length = 255)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank = True)
	created_at = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField(choices = statusChoice, null=True)

	def __str__(self):
		return "%s, --%s" % (self.parent, self.cat_name)

class newProducts(models.Model):
	pro_name = models.CharField(max_length = 255, null =True)
	sub_cat_id = models.ForeignKey(newCatagory, on_delete=models.CASCADE, null=True, blank = True)
	pro_image = models.ImageField(null = True)
	pro_price = models.FloatField(null = True)
	description = models.TextField(null = True)
	status = models.SmallIntegerField(choices = statusChoice, null=True)
	created_at = models.DateTimeField(auto_now_add=False, null=True)

	def __str__(self):
		return "%s, --%s" % (self.sub_cat_id, self.pro_name)
