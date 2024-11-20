from django.db import models

class category(models.Model):
    name=models.CharField(max_length=50,verbose_name="دسته بندی")
    class Meta:
        verbose_name="دسته بندی"
        verbose_name_plural="دسته بندی ها"
    def __str__(self) -> str:
        return self.name


class product(models.Model):
    onvan=models.CharField(max_length=30,verbose_name="نام محصول")
    category=models.ManyToManyField(category,verbose_name="دسته بندی")
    gheymat=models.DecimalField(max_digits=10,decimal_places=0,verbose_name="قیمت")
    off=models.IntegerField(default=1,verbose_name="تخفیف")
    aks=models.ImageField(upload_to='shop/static/shop/assets/images/aks',verbose_name="عکس")
    tosif=models.TextField(verbose_name="توصیف")
    noe=models.IntegerField(default=1)

    def __str__(self):
        return self.onvan