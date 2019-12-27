from django.urls import path, include
from .views import  Register, Main
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()

app_name='devaccounts'
#Add Django site authentication urls (for login, logout, password management)
# APPEND_SLASH = True
urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('', Main.as_view(), name='main'),
    # path('accounts/', include('django.contrib.auth.urls')),
    


    # path('register', DevRegisterSet.as_view(), name='register'),

    # path('', DevViewSet.as_view({'get': 'list'}), name='home'),
    # path('login/', DevViewSet.as_view(), name='login'),
    # path('', DevViewSet.as_view({'get': 'list'}), name='register'),
    # path('login/', DevViewSet.as_view({'get': 'retrieve'}), name='login'),
    # path('register', DevViewSet.as_view({'post': 'create'}), name='registerpost'),
    # path('register', DevViewSet.as_view({'post': 'create'}), name='register'),
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
