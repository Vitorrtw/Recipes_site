from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipesViewsTeste(TestCase):
    def test_recipes_home_view_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipes_category_view_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={"category_id":1}))
        self.assertIs(view.func, views.category)

    def test_recipes_recipe_view_is_correct(self):
        view = resolve(reverse("recipes:recipe", kwargs={"id":1}))
        self.assertIs(view.func, views.recipes)