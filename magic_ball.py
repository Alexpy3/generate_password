from random import choice
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
                   "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
                   "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
                   "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
print('Приветствую, я Magic Ball, и я знаю ответ на интересующий тебя вопрос.')
name = input('Как тебя зовут мой друг?\n').capitalize()
name_defolt = 'Паразитус'
print(f"Весьма посредственное имя у тебя {name}, буду звать тебя {name_defolt}!")


while True:
    ans = choice(answers)
    question = input(f'Какой вопрос Вас интересует {name_defolt}?\n')
    if question != '':
        print(ans)
    else:
        print(f'{name_defolt}, ты не задал вопрос!')
        continue
    print(f'Хочешь задать еще вопрос, {name_defolt}?')
    repair = input('Для продолжения набери "да" или "нет"\n')
    if repair == 'да':
        choice(answers)
        continue
    if repair == 'нет':
        print('Всего доброго', name_defolt, 'скоро увидимся...')
        break
# конец