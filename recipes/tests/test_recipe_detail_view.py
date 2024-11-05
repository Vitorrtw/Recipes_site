from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase

class RecipesDetailViewsTest(RecipeTestBase):
    def test_recipes_recipe_view_is_correct(self):
        view = resolve(reverse("recipes:recipe", kwargs={"id":1}))
        self.assertIs(view.func, views.recipes)
 
    def test_recepe_detail_view_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id':10000}))
        self.assertEqual(response.status_code, 404)