from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # <-- أضف هذا

def home(request):  # <-- دالة بسيطة للعرض
    return HttpResponse("مرحبًا بك في النظام الصحي!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('', home),  # <-- أضف هذا السطر لمسار الصفحة الرئيسية
]



