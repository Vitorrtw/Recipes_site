from django.test import TestCase
from recipes.models import Category, Recipe, User

class RecipeTestBase(TestCase):
    def setUp(self) -> None:
            return super().setUp()

    def make_category(self, name='Category'):
          return Category.objects.create(name=name)

    def make_author(
        self,
        first_name="user",
        last_name='user',
        username="username",
        password='12345',
        email="username@gmail.com"
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )
    
    def make_recipe(
        self,
        title = "Recipe Title",
        category_data = None,
        description = 'recipe description',
        slug = 'recipe-slug',
        preparation_time = 10,
        preparation_time_unit = 'Minutos',
        servings = 5,
        servings_unit = 'Porções',
        preparation_steps = "Preparation steps",
        preparation_steps_is_html = False,
        is_published = True,
        cover = "recipes/covers/2024/01/28/pudim-de-leite-condensado.png",
        author_data = None,
    ):
        if category_data is None:
            category_data = {}

        if author_data is None:
             author_data = {}

        return Recipe.objects.create(
            title = title,
            category = self.make_category(**category_data),
            description = description,
            slug = slug,
            preparation_time = preparation_time,
            preparation_time_unit = preparation_time_unit,
            servings = servings,
            servings_unit = servings,
            preparation_steps = preparation_steps,
            preparation_steps_is_html = preparation_steps_is_html,
            is_published = is_published,
            cover = cover,
            author = self.make_author(**author_data),
        )