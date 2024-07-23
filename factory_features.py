from faker import Faker

fake = Faker('ru_Ru')

print(fake.name())
print(fake.first_name())
print(fake.last_name())
print(fake.middle_name())

print(fake.date_time().date()) # 1972-05-18
