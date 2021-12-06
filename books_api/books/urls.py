from django.urls import path
from .views import BookCRUD

urlpatterns = [
    path('', BookCRUD.as_view(), name='books-api'),
    path('<int:pk>', BookCRUD.as_view(), name='books-api'),
]
