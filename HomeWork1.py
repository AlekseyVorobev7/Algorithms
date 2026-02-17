def is_stable_matching(men_prefs, women_prefs, matching):
    # Создаём обратное соответствие: женщина -> мужчина
    women_to_men = {woman: man for man, woman in matching.items()}

    # Проверяем все возможные пары мужчина-женщина
    for man in men_prefs:
        for woman in men_prefs[man]:
            current_partner_man = matching[man]  # Текущая партнёрша мужчины
            current_partner_woman = women_to_men[woman]  # Текущий партнёр женщины

            # Проверяем, предпочитает ли мужчина эту женщину своей текущей партнёрше
            man_prefers_other = men_prefs[man].index(woman) < men_prefs[man].index(current_partner_man)

            # Проверяем, предпочитает ли женщина этого мужчину своему текущему партнёру
            woman_prefers_other = women_prefs[woman].index(man) < women_prefs[woman].index(current_partner_woman)

            # Если оба предпочитают друг друга текущим партнёрам - паросочетание неустойчиво
            if man_prefers_other and woman_prefers_other:
                print(f"Нестабильная пара: {man} и {woman}")
                print(f"  {man} предпочитает {woman} вместо {current_partner_man}")
                print(f"  {woman} предпочитает {man} вместо {current_partner_woman}")
                return False

    return True




# Пример 1: Устойчивое паросочетание
print("=== ПРИМЕР 1: Устойчивое паросочетание ===")
men_prefs_1 = {
    'M1': ['W1', 'W2', 'W3'],
    'M2': ['W2', 'W1', 'W3'],
    'M3': ['W1', 'W2', 'W3']
}

women_prefs_1 = {
    'W1': ['M2', 'M1', 'M3'],
    'W2': ['M1', 'M2', 'M3'],
    'W3': ['M1', 'M2', 'M3']
}

matching_1 = {'M1': 'W2', 'M2': 'W1', 'M3': 'W3'}

result_1 = is_stable_matching(men_prefs_1, women_prefs_1, matching_1)
print(f"Результат: {'Устойчивое' if result_1 else 'Неустойчивое'}\n")

# Пример 2: Неустойчивое паросочетание
print("=== ПРИМЕР 2: Неустойчивое паросочетание ===")
men_prefs_2 = {
    'M1': ['W1', 'W2'],
    'M2': ['W2', 'W1']
}

women_prefs_2 = {
    'W1': ['M1', 'M2'],
    'W2': ['M1', 'M2']
}

matching_2 = {'M1': 'W2', 'M2': 'W1'}  # Неустойчивое!

result_2 = is_stable_matching(men_prefs_2, women_prefs_2, matching_2)
print(f"Результат: {'Устойчивое' if result_2 else 'Неустойчивое'}\n")