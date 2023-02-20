table_ = [['zirak5[at]mail.ru&Нет', '2002-07-24'], ['fumusli29[at]yahoo.com&Нет', '1999-03-01'],
          ['simocin5[at]mail.ru&Да', '2003-08-05'], ['zumevic72[at]yandex.ru&Нет', '2003-04-16']]

import datetime


def delete_empty_rows(table):
    return [row for row in table if row[0] is not None]


def transformer(row):
    s_1 = row[0]
    s_2 = row[1]
    s_1_split = s_1.split('&')
    check = s_1_split[1]
    mail = s_1_split[0].split('[at]')[1]
    new_date = datetime.datetime.strptime(s_2, '%Y-%m-%d').strftime('%d.%m.%Y')
    if (check == 'Нет'):
        return [mail, 'N', new_date]
    else:
        return [mail, 'Y', new_date]


def transform(table):
    new_table = []
    for i in table:
        new_table.append(transformer(i))
    return new_table


def main(table):
    return transform(
        delete_empty_rows(table)
    )


print(main(table_))
