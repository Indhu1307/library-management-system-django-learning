from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name='home'),
    path(
        'book/<int:book_id>/',   #http://127.0.0.1:8000/4
        views.book_detail,
        name='book detail'
    )
]
