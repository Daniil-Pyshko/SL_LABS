import pickle

# 1. Создание словаря с данными
olympics = {
    "США": {"2000": 97, "2004": 102, "2008": 112, "2012": 104, "2016": 121, "2020": 113},
    "Китай": {"2000": 59, "2004": 63, "2008": 100, "2012": 88, "2016": 70, "2020": 88},
    "Россия": {"2000": 89, "2004": 92, "2008": 72, "2012": 82, "2016": 56, "2020": 71},
    "Великобритания": {"2000": 28, "2004": 30, "2008": 47, "2012": 65, "2016": 67, "2020": 65},
    "Германия": {"2000": 56, "2004": 48, "2008": 41, "2012": 44, "2016": 42, "2020": 37},
    "Франция": {"2000": 38, "2004": 33, "2008": 40, "2012": 34, "2016": 42, "2020": 33},
    "Япония": {"2000": 18, "2004": 37, "2008": 25, "2012": 38, "2016": 41, "2020": 58}
}

print("=" * 70)
print("АНАЛИЗ МЕДАЛЬНЫХ ЗАПАСОВ НА ЛЕТНИХ ОЛИМПИЙСКИХ ИГРАХ (2000-2020)")
print("=" * 70)

# 2. Вывод списка стран и суммарного количества медалей
print("\n1. СУММАРНОЕ КОЛИЧЕСТВО МЕДАЛЕЙ ПО СТРАНАМ:")
print("-" * 50)

total_medals_by_country = {}
for country, years in olympics.items():
    total = sum(years.values())
    total_medals_by_country[country] = total
    print(f"{country}: {total} медалей")

# 3. Страны с максимальным и минимальным средним числом медалей
print("\n2. СРЕДНЕЕ КОЛИЧЕСТВО МЕДАЛЕЙ ЗА 6 ОЛИМПИАД:")
print("-" * 50)

average_medals = {}
for country, years in olympics.items():
    avg = sum(years.values()) / len(years)
    average_medals[country] = avg
    print(f"{country}: {avg:.2f} медалей в среднем")

max_avg_country = max(average_medals, key=average_medals.get)
min_avg_country = min(average_medals, key=average_medals.get)

print(f"\nСтрана с максимальным средним: {max_avg_country} ({average_medals[max_avg_country]:.2f} медалей)")
print(f"Страна с минимальным средним: {min_avg_country} ({average_medals[min_avg_country]:.2f} медалей)")

# 4. Год с наибольшим количеством медалей для каждой страны
print("\n3. ГОД С НАИБОЛЬШИМ КОЛИЧЕСТВОМ МЕДАЛЕЙ ПО СТРАНАМ:")
print("-" * 50)

best_years = {}
for country, years in olympics.items():
    best_year = max(years, key=years.get)
    best_medals = years[best_year]
    best_years[country] = (best_year, best_medals)
    print(f"{country}: {best_year} год - {best_medals} медалей")

# 5. Страны с ростом более чем на 20% по сравнению с 2000 годом
print("\n4. СТРАНЫ С РОСТОМ БОЛЕЕ ЧЕМ НА 20% (2000 vs 2020):")
print("-" * 50)

growth_countries = []
for country, years in olympics.items():
    medals_2000 = years["2000"]
    medals_2020 = years["2020"]
    
    if medals_2000 == 0:  # Чтобы избежать деления на ноль
        growth_percent = 0
    else:
        growth_percent = ((medals_2020 - medals_2000) / medals_2000) * 100
    
    if growth_percent > 20:
        growth_countries.append((country, growth_percent))
        print(f"{country}: рост на {growth_percent:.1f}% (с {medals_2000} до {medals_2020} медалей)")

if not growth_countries:
    print("Нет стран с ростом более чем на 20%")

# 6. Дополнительная статистика
print("\n5. ДОПОЛНИТЕЛЬНАЯ СТАТИСТИКА:")
print("-" * 50)

# Общее количество медалей за все годы
all_medals = []
for years in olympics.values():
    all_medals.extend(years.values())

print(f"Всего медалей распределено: {sum(all_medals)}")
print(f"Среднее медалей на страну за все годы: {sum(all_medals) / len(all_medals):.1f}")

# Самый успешный год в целом
year_totals = {}
for country, years in olympics.items():
    for year, medals in years.items():
        year_totals[year] = year_totals.get(year, 0) + medals

best_overall_year = max(year_totals, key=year_totals.get)
print(f"Самый медальный год в целом: {best_overall_year} ({year_totals[best_overall_year]} медалей)")

# 7. Сохранение в бинарный файл
with open('data.pickle', 'wb') as file:
    pickle.dump(olympics, file)
    print(f"\nСловарь сохранен в файл 'data.pickle' ({len(olympics)} стран)")

# 8. Проверка чтения из файла
print("\n6. ПРОВЕРКА СОХРАНЕННЫХ ДАННЫХ:")
print("-" * 50)
with open('data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)
    print(f"Загружено {len(loaded_data)} стран из файла")
    print(f"Первая страна в словаре: {list(loaded_data.keys())[0]}")

print("\n" + "=" * 70)
print("АНАЛИЗ ЗАВЕРШЕН")
print("=" * 70)