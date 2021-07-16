from . import views
from django.urls  import path

app_name='narticle'
urlpatterns=[
path('',views.articlesList,name="lizt"),
path('<sluggg>',views.artictest,name="dedail")
]
