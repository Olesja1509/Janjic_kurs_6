from django.urls import path

from blog.apps import BlogConfig
from blog.views import (ArticleDetailView)

app_name = BlogConfig.name

urlpatterns = [
    path('view/<int:pk>', ArticleDetailView.as_view(), name='view'),
]
