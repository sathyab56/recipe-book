import requests
from django.http import JsonResponse
from django.shortcuts import render

API_KEY = "92f0263949a74da9877e2fb48b92fbf9"

def recipe_list(request):
    return render(request, 'recipes/recipe_list.html')

def get_recipes(request):
    try:
        response = requests.get(f'https://api.spoonacular.com/recipes/random?number=6&apiKey={API_KEY}')
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return JsonResponse({'recipes': data.get('recipes', [])})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)