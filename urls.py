from django.urls import path # type: ignore
from .views import recipe_list, get_recipes

urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('api/recipes/', get_recipes, name='get_recipes'),
]