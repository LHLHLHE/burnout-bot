START_TEXT = ('Выберете тест для оценки уровня тревожности:\nPT - реактивной тревожности\n'
              'ЛТ - личностной тревожности\nСТ - сокращенный вариант оценки ситуативной тревожности\n\n'
              '<b>ИНСТРУКЦИЯ</b>:\nНа вопросы в тестах РТ и СТ следует отвечать в зависимости от того, '
              'как вы себя чувствуете в данный момент.\n\n'
              'На вопросы в тесте ЛТ следует отвечать в зависимости от того, как вы себя чувствуете обычно.'
              )
END_TEXT = 'По результатам теста Вы набрали {} баллов. Этот результат говорит о том, что у Вас {} уровень тревожности'

ANXIETY_LEVEL = {
    'low': '<b>низкий</b>',
    'middle': '<b>умеренный</b>',
    'high': '<b>высокий</b>'
}

START_BUTTONS = {
    'ЛТ': 'start_lt',
    'РТ': 'start_rt',
    'СТ сокр': 'start_st'
}

LT_OPINIONS = (
    'Я спокоен',
    'Мне ничто не угрожает',
    'Я нахожусь в напряжении',
    'Я испытываю сожаление',
    'Я чувствую себя свободно',
    'Я расстроен',
    'Меня волнуют возможные неудачи',
    'Я чувствую себя отдохнувшим',
    'Я не доволен собой',
    'Я испытываю чувство внутреннего удовлетворения',
    'Я уверен в себе',
    'Я нервничаю',
    'Я не нахожу себе места',
    'Я взвинчен',
    'Я не чувствую скованности, напряженности',
    'Я доволен',
    'Я озабочен',
    'Я слишком возбужден, и мне не по себе',
    'Мне радостно',
    'Мне приятно',
)
RT_OPINIONS = (
    'Я испытываю удовольствие',
    'Я очень быстро устаю',
    'Я легко могу заплакать',
    'Я хотел бы быть таким же счастливым, как и другие',
    'Нередко я проигрываю из-за того, что недостаточно быстро принимаю решения',
    'Обычно я чувствую себя бодрым',
    'Я спокоен, хладнокровен и собран',
    'Ожидаемые трудности обычно очень тревожат меня',
    'Я слишком переживаю из-за пустяков',
    'Я вполне счастлив',
    'Я принимаю все слишком близко к сердцу',
    'Мне не хватает уверенности в себе',
    'Обычно я чувствую себя в безопасности',
    'Я стараюсь избегать критических ситуаций',
    'У меня бывает хандра',
    'Я доволен',
    'Всякие пустяки отвлекают и волнуют меня',
    'Я так сильно переживаю свои разочарования, что потом долго не могу о них забыть',
    'Я уравновешенный человек',
    'Меня охватывает сильное беспокойство, когда я думаю о своих делах и заботах',
)
ST_OPINIONS = (
    'Я чувствую себя свободно',
    'Я нервничаю',
    'Я не чувствую скованности, напряженности',
    'Я доволен',
    'Я озабочен',
)

LT_SUM1_INDEXES = (22, 23, 24, 25, 28, 29, 31, 32, 34, 35, 37, 38, 40)
LT_SUM2_INDEXES = (21, 26, 27, 30, 33, 36, 39)

RT_SUM1_INDEXES = (3, 4, 6, 7, 9, 12, 13, 14, 17, 18)
RT_SUM2_INDEXES = (1, 2, 5, 8, 10, 11, 15, 16, 19, 20)

ST_SUM1_INDEXES = (2, 5)
ST_SUM2_INDEXES = (1, 3, 4)

ANSWERS = (
    'Нет, это не так',
    'Пожалуй, так',
    'Верно',
    'Совершенно верно'
)
