import json
from collections import defaultdict

def read_json_file(filename):
    """Чтение JSON файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        print(f"Ошибка чтения файла {filename}")
        return {}

def find_clients_by_surname_prefix(clients, prefix):
    """Поиск клиентов по первым 3 буквам фамилии"""
    prefix = prefix.lower()
    result = []
    for client in clients:
        if client['last_name'].lower().startswith(prefix):
            result.append(client)
    return result

def calculate_avg_budget_by_company(clients):
    """Вычисление среднего бюджета по компаниям"""
    company_stats = defaultdict(lambda: {'total': 0, 'count': 0})
    
    for client in clients:
        company = client['company']
        budget = client['budget']
        company_stats[company]['total'] += budget
        company_stats[company]['count'] += 1
    
    avg_budgets = {}
    for company, stats in company_stats.items():
        avg_budgets[company] = stats['total'] / stats['count']
    
    return avg_budgets

def count_clients_by_industry(clients):
    """Подсчет количества клиентов по отраслям"""
    industry_counts = defaultdict(int)
    for client in clients:
        industry = client['industry']
        industry_counts[industry] += 1
    return dict(industry_counts)

def save_filtered_data(clients, filename='out.json', min_budget=0):
    """Сохранение отфильтрованных данных"""
    filtered_clients = [c for c in clients if c['budget'] >= min_budget]
    
    data_to_save = {
        'filtered_clients': filtered_clients,
        'total_count': len(filtered_clients),
        'filter_criteria': f'budget >= {min_budget}'
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data_to_save, f, indent=4, ensure_ascii=False)
    
    return len(filtered_clients)

def main():
    # 1. Чтение файла
    data = read_json_file('9.json')
    if not data:
        return
    
    clients = data.get('clients', [])
    print(f"Прочитано клиентов: {len(clients)}")
    
    # 2. Поиск по префиксу фамилии
    print("\nПоиск клиентов по префиксу фамилии:")
    prefix = "vol"
    found = find_clients_by_surname_prefix(clients, prefix)
    print(f"Найдено с фамилией на '{prefix}': {len(found)}")
    for client in found:
        print(f"  - {client['first_name']} {client['last_name']}")
    
    # 3. Средний бюджет по компаниям
    print("\nСредний бюджет по компаниям:")
    avg_budgets = calculate_avg_budget_by_company(clients)
    for company, avg in avg_budgets.items():
        print(f"  {company}: ${avg:,.2f}")
    
    # 4. Клиенты по отраслям
    print("\nКлиенты по отраслям:")
    industry_counts = count_clients_by_industry(clients)
    for industry, count in industry_counts.items():
        print(f"  {industry}: {count}")
    
    # 5. Сохранение отфильтрованных данных
    print("\nСохранение отфильтрованных данных...")
    saved_count = save_filtered_data(clients, 'out.json', min_budget=30000)
    print(f"Сохранено {saved_count} клиентов в out.json")

if __name__ == "__main__":
    main()