# ##############################################
# Birthday Wisher
# #############################################
from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "razausmankhan.testing@gmail.com"
PASSWORD = "wtbskojaxschtwnk"

today = datetime.now()
today_tuple = ( today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = { (data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows() }

print(birthdays_dict)
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

# ##########################################################
# Random Motivational Quotes sender
# ##########################################################
#
#
# import datetime as dt
# from random import choice
# import smtplib
#
# current_day = dt.datetime.now().weekday()
#
# with open('quotes.txt') as file:
#     quotes = file.read().split('\n')
#     random_quote = choice(quotes)
#
# my_email = "razausmankhan.testing@gmail.com"
# password = "wtbskojaxschtwnk"
#
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="razausmankhan3@gmail.com",
#                         msg=f"Subject:Monday Motivation Quote \n\n {random_quote}")



# import smtplib
#
# my_email = "razausmankhan.testing@gmail.com"
# password = "wtbskojaxschtwnk"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="razausmankhan3@gmail.com",
#                         msg="Subject:this is the subject \n\n This is the body")
#     connection.close()
#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1997, month=2, day=20, hour= 4 )
# print(date_of_birth)