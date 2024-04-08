from django.db import models
from django.db.models import ForeignKey
from django.utils.text import slugify

from rentify.brands.models import Brand
from rentify.categories.models import Category


class Cars(models.Model):

    GEARBOX = (
        ("Manual", "Manual"),
        ("Auto", "Auto"),
    )

    brand = ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name="cars",
    )

    model = models.CharField(
        max_length=20,
        blank=False,
        null=False,
    )

    image = models.ImageField(
        upload_to="cars_image",
        null=True,
        blank=True,
    )

    year = models.IntegerField(
        default=2020,
        null=False,
        blank=False,
    )

    category = ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="cars",
    )

    gearbox = models.CharField(
        max_length=20,
        choices=GEARBOX,
        null=False,
        blank=False,
    )

    price = models.PositiveIntegerField(
        blank=False,
        null=False,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=False,
        editable=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.pk} {self.brand.name}-{self.model}")




