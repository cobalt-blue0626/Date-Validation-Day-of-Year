# Date-Validation-Day-of-Year

The days of the year are often numbered from 1 to through 365 (or 366). In this problem, you
are asked to write a program that accepts a date as year/month/day (yyyy/mm/dd),
verifies whether it is a legal (valid) date or not (invalid), and then calculates the corresponding
day number of the year. The task consists of two parts: (1) verifying the input yyyy/mm/dd is
valid or invalid, and (2) compute the day number of the year.

In part (1), for example, 1962/05/24 is valid, but 2000/09/31 is invalid (September has
only 30 days), and 2016/13/00 is also invalid (only 12 months in a year, and there is no 0 in
days). You need to take care of the leap year. For example, 2016/02/29 is valid but
2015/02/29 is invalid.

In part (2), for example, 2015/10/01 is the No. 274 day of the year, and 2014/05/20 is
the No. 140 day of the year. In addition, 2016/12/31 is the No. 366 day of the year and
2015/12/31 is the No. 365 day of the year (because the former is a leap year and the latter is
not a leap year). Moreover, 1000/03/01 is the No. 60 day of the year, and 1200/03/01 is
the No. 61 day of the year (because the former is not a leap year and the latter is a leap year).

The challenge comes in leap years (when there are 29 days in February). In leap years, the 29th
of February is a valid date, and every day after that is one day later in the year. The rule for which
years are leap years is more complicated than a lot of people realize:

Years divisible by 4 are leap years,
except, years divisible by 100 are not leap years,
except, years divisible by 400 are leap years.

In this problem, you will practice to use conditionals (if, elif, else), string slicing, logic
operations (and, or, not), and relational operations (>, <, >=, <=, ==, !=).
