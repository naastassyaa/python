from Film import Film

film1 = Film("Титанік", "Джеймс Кемерон", 1997, 123, 15)
film2 = Film("До зустрічі з тобою", "Теа Шеррок", 2016, 166, 20)
film3 = Film("Гра престолів", "Марк Майлод", 2011, 190, 20)

print("Фільми з початковими параметрами:")

print(film1, film2, film3, sep="\n", end="\n\n")

film1.rate(9)
film2.rate(15)
film3.rate(-1)

print("Фільми зі зміненим рейтингом:")

print(film1, film2, film3, sep="\n", end="\n\n")

print("Загальний рейтинг фільмів:")

print(film1.get_current_rating(), film2.get_current_rating(), film3.get_current_rating(), sep="\n", end="\n\n")

print("Робота property:")

print(film1.title, end="\n\n")

print("Робота setter:")

film1.director = "Настася Глушко"

print(film1)
