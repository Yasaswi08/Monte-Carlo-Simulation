import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import statistics as st
import re
import time
from scipy.stats import binom
import seaborn as sns
sns.set(style="darkgrid")
import math


class HotelRoom:
    holiday_list = ['01-01', '01-21', '02-18', '05-27', '07-04', '09-02', '10-14', '10-11', '11-28', '12-25', '12-31']

    def __init__(self, hotel_capacity, holiday_boolean, standard_capacity, deluxe_capacity, superior_capacity,
                 standard_cost, deluxe_cost, superior_cost, superior_split_percentage, deluxe_split_percentage,
                 standard_split_percentage, date_of_booking, day_of_booking, hotel_category):
        self.hotel_capacity = hotel_capacity
        self.holiday_boolean = holiday_boolean
        self.standard_capacity = standard_capacity
        self.deluxe_capacity = deluxe_capacity
        self.superior_capacity = superior_capacity
        self.standard_cost = standard_cost
        self.deluxe_cost = deluxe_cost
        self.superior_cost = superior_cost
        self.superior_split_percentage = superior_split_percentage
        self.deluxe_split_percentage = deluxe_split_percentage
        self.standard_split_percentage = standard_split_percentage
        self.date_of_booking = date_of_booking
        self.day_of_booking = day_of_booking
        self.hotel_category = hotel_category

    @classmethod
    def attribute_collector(class_object):
        present_date = time.strftime('%m-%d', time.localtime(time.time()))
        date_of_booking_temp = input("Enter the date you want to book (MM-DD-YYYY):")
        holiday_boolean = date_of_booking_temp[0:5] in HotelRoom.holiday_list
        if holiday_boolean:
            print(
                "You're booking on a public holiday! Since the hotel runs in high demand during this time, your customer will not get the full amount in refund_per_cancellation if they wish to cancel at anytime.")
        if date_of_booking_temp[3:4] == '0' and date_of_booking_temp[0:1] == '0':
            month_of_booking = date_of_booking_temp[1:2]
            day_of_booking = date_of_booking_temp[4:5]
            year_of_booking = date_of_booking_temp[-4:]
        elif date_of_booking_temp[3:4] == '0' and date_of_booking_temp[0:1] != '0':
            month_of_booking = date_of_booking_temp[0:2]
            day_of_booking = date_of_booking_temp[4:5]
            year_of_booking = date_of_booking_temp[-4:]
        elif date_of_booking_temp[3:4] != '0' and date_of_booking_temp[0:1] == '0':
            month_of_booking = date_of_booking_temp[1:2]
            day_of_booking = date_of_booking_temp[3:5]
            year_of_booking = date_of_booking_temp[-4:]
        else:
            month_of_booking = date_of_booking_temp[0:2]
            day_of_booking = date_of_booking_temp[3:5]
            year_of_booking = date_of_booking_temp[-4:]
        date_of_booking = month_of_booking + "-" + day_of_booking + "-" + year_of_booking
        list_date = date_of_booking.split("-")
        day_of_booking = dayofweek(int(list_date[1]), int(list_date[0]), int(list_date[2]))
        satisfy = True
        while satisfy == True:
            print(
                'You will now be required to create your own hotel, please give required input as per the prompt. According to this program, you can create a hotel with 3 types of rooms (Standard|Deluxe|Superior). The system will ask you for the split of each category and room and their corresponding costs.')
            hotel_capacity = int(input('Enter the total number of rooms:'))
            superior_capacity = int(input("Enter the superior room split:"))
            superior_split_percentage = superior_capacity / hotel_capacity
            deluxe_capacity = int(input("Enter the deluxe room split:"))
            deluxe_split_percentage = deluxe_capacity / hotel_capacity
            standard_capacity = int(input("Enter the standard room split:"))
            standard_split_percentage = standard_capacity / hotel_capacity
            if hotel_capacity == (superior_capacity + deluxe_capacity + standard_capacity):
                satisfy = False
            else:
                print("The split isn't right. Please try again:")

        superior_cost = int(input("Enter the price of Superior room:"))
        deluxe_cost = int(input("Enter the price of deluxe room:"))
        standard_cost = int(input("Enter the standard room price:"))

        hotel_category = input("What is your hotel's type? Business/Vacation")

        return class_object(hotel_capacity, holiday_boolean, standard_capacity, deluxe_capacity, superior_capacity,
                            standard_cost, deluxe_cost, superior_cost, superior_split_percentage,
                            deluxe_split_percentage, standard_split_percentage, date_of_booking, day_of_booking,
                            hotel_category)