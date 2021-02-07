subjects = []
koef = []
score = []
num = int(input("Введіть кількість дисциплін для обрахунку: "))
addPoints = 0

print()


def enterStats():
    for sub in range(num):
        subjects.append(input("Введіть дисципліну: "))
        koef.append(float(input("Введіть коефіцієнт: ")))
        score.append(float(input("Введіть бал: ")))
        print()

    answ1 = int(input('У вас є дод. бали? (0 - Ні, 1 - Так): '))
    if answ1 == 1:
        addPoints = float(input('Введіть к-ть дод. балів: '))
    else:
        addPoints = 0

def findSuccess():
    dbt = 0

    for sub in range(num):
        dbt += score[sub] * koef[sub]

    return dbt / sum(koef)


def findRate():
    return findSuccess() * 0.05

enterStats()
general = findSuccess() + addPoints

print('\n Бал успішності в групі:', '%.3f' % findSuccess())
print('Рейтинговий бал без додаткових балів:', '%.3f' % findRate())
print('Рейтинговий із додатковими балами:', '%.3f' % general)
