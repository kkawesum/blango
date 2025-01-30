from django.urls import path# other imports
import blog.views

urlpatterns = [
    # other patterns
    path("", blog.views.index)
]