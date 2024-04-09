from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rentify import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("rentify.vanilla.urls")),
    path("accounts/", include("rentify.accounts.urls")),
    path('accounts/', include('allauth.urls')),
    path("cars/", include("rentify.cars.urls")),
    path("categories/", include("rentify.categories.urls")),
    path("brands/", include("rentify.brands.urls")),
    path("reviews/", include("rentify.reviews.urls")),
    path("booking/", include("rentify.bookings.urls")),
    path("contact/", include("rentify.mail.urls")),
    path("payment/", include("rentify.payments.urls"))
]
