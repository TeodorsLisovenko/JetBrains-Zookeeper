# put your python code here

out_hours = int(input())

out_minutes = int(input())

out_seconds = int(input())

rain_hours = int(input())

rain_minutes = int(input())

rain_seconds = int(input())

calc_one = (out_hours * 60 + out_minutes) * 60 + out_seconds

calc_second = (rain_hours * 60 + rain_minutes) * 60 + rain_seconds

print(calc_second - calc_one)

