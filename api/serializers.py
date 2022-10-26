from rest_framework import serializers
from menu.models import Pizza, Salad, Pasta, Garnier, Cocktail, Drinks, Subs


class PizzaSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Pizza
        field = "__all__"

class SaladSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Salad
        field = "__all__"

class PastaSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Pasta
        field = "__all__"

class GarnierSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Garnier
        field = "__all__"

class CocktailSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Cocktail
        field = "__all__"

class DrinksSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Drinks
        field = "__all__"

class SubsSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Subs
        field = "__all__"