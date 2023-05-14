from Film import Film

films = [
    Film(),
    Film("До зустрічі з тобою", "Теа Шеррок", 2016, 166, 20),
    Film.get_instance(),
    Film.get_instance()]

print("Фільми з початковими параметрами:")
for film in films:
    print(film)
print()

print("Фільм зі зміненим рейтингом:")

films[1].rate(9)

print(films[1])
print()

print("Загальний рейтинг фільму:")

print(films[1].get_current_rating())
print()

print("Робота setter:")

films[2].title = "Barabashka"

for film in films:
    print(film)

