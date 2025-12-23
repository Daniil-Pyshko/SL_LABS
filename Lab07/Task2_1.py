import csv
from collections import defaultdict

# Чтение CSV файла
def read_csv(filename):
    movies = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            movies.append(row)
    return movies

# 1. Вывод содержимого
def print_movies(movies):
    print("СОДЕРЖИМОЕ ФАЙЛА:")
    print("=" * 60)
    for i, movie in enumerate(movies, 1):
        print(f"\nФильм #{i}:")
        for key, value in movie.items():
            print(f"  {key} → {value}")

# 2. Нахождение самого короткого и самого длинного фильма
def find_min_max_duration(movies):
    min_movie = min(movies, key=lambda x: int(x['Duration']))
    max_movie = max(movies, key=lambda x: int(x['Duration']))
    return min_movie, max_movie

# 3. Подсчет кассовых сборов для фильмов с рейтингом > 8.0
def calculate_high_rating_revenue(movies):
    total = 0
    for movie in movies:
        if float(movie['Rating']) > 8.0:
            total += int(movie['Box_Office'])
    return total

# 4. Вычисление среднего рейтинга для жанра "Drama"
def calculate_avg_drama_rating(movies):
    drama_movies = [m for m in movies if m['Genre'] == 'Drama']
    if not drama_movies:
        return 0
    total = sum(float(m['Rating']) for m in drama_movies)
    return total / len(drama_movies)

# 5. Подсчет количества фильмов по жанрам
def count_movies_by_genre(movies):
    counts = defaultdict(int)
    for movie in movies:
        counts[movie['Genre']] += 1
    return dict(counts)

# Основная программа
def main():
    # Чтение данных
    movies = read_csv('9.csv')
    
    # Вывод содержимого
    print_movies(movies)
    
    # Выполнение всех функций
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ АНАЛИЗА")
    print("=" * 60)
    
    # 1. Самый короткий и самый длинный фильм
    min_movie, max_movie = find_min_max_duration(movies)
    print(f"\n1. Самый короткий фильм: {min_movie['Title']} ({min_movie['Duration']} мин.)")
    print(f"   Самый длинный фильм: {max_movie['Title']} ({max_movie['Duration']} мин.)")
    
    # 2. Кассовые сборы фильмов с рейтингом > 8.0
    revenue = calculate_high_rating_revenue(movies)
    print(f"\n2. Общие кассовые сборы фильмов с рейтингом > 8.0: ${revenue:,}")
    
    # 3. Средний рейтинг для жанра "Drama"
    avg_rating = calculate_avg_drama_rating(movies)
    print(f"\n3. Средний рейтинг фильмов жанра 'Drama': {avg_rating:.2f}")
    
    # 4. Количество фильмов по жанрам
    genre_counts = count_movies_by_genre(movies)
    print(f"\n4. Количество фильмов по жанрам:")
    for genre, count in sorted(genre_counts.items()):
        print(f"   {genre}: {count} фильмов")

if __name__ == "__main__":
    main()