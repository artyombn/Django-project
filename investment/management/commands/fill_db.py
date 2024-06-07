# from django.core.management.base import BaseCommand
# from animals.models import Category, Animal
#
#
# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         # здесь мы можем писать любые скрипты, связанные с проектом
#         print("Filling db ...")
#         # 1. Удаление
#         Category.objects.all().delete()
#
#         # 2. Создание
#         bear = Category.objects.create(name="Медведь Неправильный")
#
#         # 3. Изменение
#         bear.name = "Медведь"
#         bear.save()
#
#         # 4. Все данные
#         print(Category.objects.all())
#
#         Animal.objects.all().delete()
#
#         # 5. Получить только 1 объект
#         # bear = Category.objects.get(id=bear.id)  # если известно
#         bear = Category.objects.get(name="Медведь")  # по имени
#
#         Animal.objects.create(
#             name="Маша",
#             category=bear,
#         )
#         print("Done")
