from django.conf.urls import include,url
from . import views


urlpatterns = [
    url('list/',views.ApiViews.as_view()),

]
