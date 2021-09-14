from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name="post"
urlpatterns=[
	path('',views.index,name="index"),
	path('post/<int:id>/',views.show,name="show"),
	path('update/post/<int:id>/',views.update,name="update"),
	path('post/new/',views.new,name='new')
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)