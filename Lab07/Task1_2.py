import string

def remove_lines_without_punctuation(input_file, output_file):
    """
    Удаляет строки без пунктуации и сохраняет результат
    """
    punctuation_chars = string.punctuation + '«»—…'
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        
        # Фильтруем строки
        filtered_lines = []
        for line in lines:
            # Проверяем, есть ли в строке знаки пунктуации (кроме пробела)
            if any(char in punctuation_chars for char in line):
                filtered_lines.append(line)
        
        # Сохраняем результат
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.writelines(filtered_lines)
        
        print(f"Обработка завершена!")
        print(f"Исходных строк: {len(lines)}")
        print(f"Сохранено строк: {len(filtered_lines)}")
        print(f"Удалено строк: {len(lines) - len(filtered_lines)}")
        
        return True
        
    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")
        return False
    except Exception as e:
        print(f"Ошибка: {e}")
        return False


# Создаем минимальный тестовый файл
def create_minimal_test():
    test_content = """Строка без пунктуации
Строка с запятой, вот так
Еще одна простая строка
Третья строка. С точкой
Четвертая строка! С восклицанием"""
    
    with open('input.txt', 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    print("Тестовый файл 'input.txt' создан")


# Основная программа
if __name__ == "__main__":
    # Создаем тестовый файл (если нужно)
    create_minimal_test()
    
    # Выполняем задание
    remove_lines_without_punctuation('input.txt', 'output.txt')
    
    # Показываем результат
    print("\nРезультат:")
    print("-" * 30)
    
    with open('input.txt', 'r', encoding='utf-8') as f:
        print("input.txt:")
        for i, line in enumerate(f, 1):
            print(f"{i}: {line.rstrip()}")
    
    print("\noutput.txt:")
    with open('output.txt', 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            print(f"{i}: {line.rstrip()}")