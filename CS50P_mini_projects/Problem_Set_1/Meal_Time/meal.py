"""
Suppose that you’re in a country where it’s customary to eat breakfast between 
7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 
19:00. Wouldn’t it be nice if you had a program that could tell you what to eat 
when?

In meal.py, implement a program that prompts the user for a time and outputs 
whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a 
meal, don’t output anything at all. Assume that the user’s input will be 
formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time 
range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or 
anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be 
called by main) that converts time, a str in 24-hour format, to the 
corresponding number of hours as a float. For instance, given a time like "7:30" 
(i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

If up for a challenge, optionally add support for 12-hour times, allowing the 
user to input times in these formats too:

1) #:## a.m. and ##:## a.m.
2) #:## p.m. and ##:## p.m.

7:00 -------------> breakfast time

7:30 -------------> breakfast time

12:42 ------------> lunch time

18:32 ------------> dinner time

11:11 ------------> no output
"""


def main():
    meal_time = input("What time is it? ").strip().lower().replace(" ", "")
    meal_time = convert(meal_time)
    if meal_time is None:
        print("invalid time")
    elif 7 <= meal_time <= 8:
        print("breakfast time")
    elif 12 <= meal_time <= 13:
        print("lunch time")
    elif 18 <= meal_time <= 19:
        print("dinner time")


def convert(time):
    time = time.split(":")
    hour = float(time[0])
    if hour < 0 or hour > 23:
        return None
    if len(time[1]) > 2:
        minutes = float(time[1][:2])
        if 0 <= minutes <= 59:
            if time[1].endswith("p.m."):
                if hour > 12:
                    return None
                if hour < 12:
                    hour += 12
                    return hour + (minutes / 60)

                return hour + (minutes / 60)
            if time[1].endswith("a.m."):
                if hour > 12:
                    return None
                if hour == 12:
                    hour -= 12
                    return hour + (minutes / 60)

                return hour + (minutes / 60)

        else:
            return None
    else:
        minutes = float(time[1])
        if 0 <= minutes <= 59:
            return hour + (minutes / 60)

        return None


if __name__ == "__main__":
    main()
