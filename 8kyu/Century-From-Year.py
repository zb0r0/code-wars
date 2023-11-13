# Introduction
# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.
#
# Task
# Given a year, return the century it is in.

#https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097
#my solution:

def century(year):
    if year % 100 >= 1:
        return year // 100 + 1
    else:
        return year // 100