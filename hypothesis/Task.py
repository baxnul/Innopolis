import pandas as pd
import psycopg2

my_hypothesis = [3, 5]  # Население России сократилось на 3-5% с 2017 по 2021 год
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password='admin')

cursor = conn.cursor()
postgreSQL_select_Query = '''select *
                                from population_by_country pbc
                                where "year" between 2017 and 2022
                                and pbc.country_code = 'RUS';'''
cursor.execute(postgreSQL_select_Query)
population_by_country = cursor.fetchall()

population_dict_list = []
table_title = ['Country_cod', 'Country_Name', 'Year', 'Value']

for row in population_by_country:
    population_dict_list.append(dict(zip(table_title, row)))

df = pd.DataFrame(data=population_dict_list)

value_people = df['Value'].tolist()  # Получаем массивом всю колонку Value

decrease_people = value_people[0] - value_people[
    -1]  # На столько человек уменьшилось население России с 2017 по 2021 год
print('На столько человек уменьшилось население России с 2017 по 2021 год:', decrease_people)
percent_decrease = decrease_people / value_people[-1] * 100  # Уменьшение населения России в % соотношении
print('Уменьшение населения России в % соотношении с 2017 по 2021 год:', percent_decrease, '%')
if my_hypothesis[0] <= percent_decrease <= my_hypothesis[-1]:
    print('Ваша гипотеза "Население России сократилось на 3%-5% с 2017 по 2021 год" верна')
else:
    print('Ваша гипотеза "Население России сократилось на 3%-5% с 2017 по 2021 год" неверная')
