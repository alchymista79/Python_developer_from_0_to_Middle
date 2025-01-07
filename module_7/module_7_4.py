from arcade.key import PRINT

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

challenge_result = result

tasks_total = score_1 + score_2

time_avg = round(((team1_time + team2_time) / tasks_total), 1)

print('В команде Мастера кода участников: %(num1)s!' % {'num1': team1_num})
print('Итого сегодня в командах участников: %(num1)s и %(num2)s!' % {'num1': team1_num, 'num2': team2_num})
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {}!'.format(round(team2_time, 1)))
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')