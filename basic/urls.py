from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
#from main.views import ChangeLanguageView

urlpatterns = [
    #path('language/', ChangeLanguageView.as_view(), name='change_language'),
    path('admin/', admin.site.urls),
    path('', include("first_nike.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
