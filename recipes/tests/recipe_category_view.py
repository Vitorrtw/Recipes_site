from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase

class RecipesCategoryViewTest(RecipeTestBase):
    def test_recipes_category_view_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={"category_id":1}))
        self.assertIs(view.func, views.category)

    def test_recipes_category_templete_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:category', kwargs={'category_id':1}))
        self.assertEqual(len(response.context['recipes']), 1)

    def test_recipe_category_status_code(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id':1000}))
        self.assertEqual(response.status_code, 404)