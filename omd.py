# Guido van Rossum <guido@python.org>

def yes_no():
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    return options[option]


game_over = 'Вы проиграли!\n'
ending = 'Говорят, именно поэтому мы, люди, не видим уток в барах в наши дни.'


def step2_umbrella():
    duck = ''
    duck_msg = 'Еще одна утка-маляр 🦆 решила выпить зайти в бар. Взять ей зонтик? ☂️'
    duck_cnt = 5
    umbrella_count = 0
    for i in range(duck_cnt):
        duck += '🦆'
        print(f'{duck}\n{duck_msg}')
        answer = yes_no()
        if answer:
            umbrella_count += 1

    if umbrella_count == duck_cnt:
        print(
            f'{game_over}'
            'Уток-маляров с зонтиками стало слишком много.\n'
            'Зонтики настолько плотно наполняли бар, что стали царапать стены.\n'
            'Утки это заметили, и попытались закрасить царапины - ведь это не просто утки, '
            'а утки-маляры.\n'
            'Но людям, сидевшим в баре, не понравился утячий дизайн.\n'
            'Они забрали все их зонты и '
            'прокололи уток острым концом зонтов, запекли в духовке и очень вкусно поужинали.\n'
            'Эта страшная история '
            'передается утками от поколения к поколению. '
            f'{ending}'
        )

    else:
        print(
            f'{game_over}'
            'Утки без зонтика стали завидовать уткам с зонтиком.\n'
            'С горя они напились текилы, '
            'обозлились на собратьев, и устроили махач.\n'
            'На следующее утро ни уток, ни бара не осталось - только '
            'перья. '
            f'{ending}'
        )


def step2_no_umbrella():
    print(f'{game_over}'
          'Утка посмотрела на бармена.\n'
          'Бармен посмотрел на утку.\n'
          'Бармен сглотнул слюну и напрягся, готовый к действию '
          '(вы бы знали, как редко он ест мясо - последний раз это было в позапрошлую среду).\n'
          'Эх, если бы у утки был '
          'зонтик, бармен бы относился к ней серьезнее, не рассматривал бы как еду...\n'
          'На следующий день бригада '
          'уток-маляров нашла утячьи кости в мусорном баке за баром. '
          f'{ending}')


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False, 'кря': None}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option] is None:
        print('Вы выиграли!\n'
              'Это была проверка на своего, и теперь весь бар знает, что вы и есть утка. Хотите вы этого, '
              'или нет 🦆')
        return

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
