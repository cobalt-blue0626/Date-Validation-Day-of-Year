data=input("Input a date (yyyy/mm/dd):")
data_year=data[0:4]#to get the year,we have to cut down the string of data
data_month=data[5:7]#to get the month,we have to cut down the string of data
data_day=data[8:]#to get the day,we have to cut down the string of data
d=0

#to make the year become integer
i=0
while i<4 and int(data_year[:1])==0:
	data_year=data_year[1:]
	i=i+1

#to make the month become integer
if int(data_month[:1])==0:  
	data_month=data_month[1:]

#to make the day become integer
if int(data_day[:1])==0:
	data_day=data_day[1:]



#if int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)):
	#data_year_leap=int(data_year)
	#print(data_year_leap)

#the program below is to detect whether month and day are valid
if not 1<=int(data_month)<=12:
	print("Month Invalid.")
elif (int(data_month)==1 or  int(data_month)==3 or  int(data_month)==5 or int(data_month)==7 or  int(data_month)==8 or  int(data_month)==10 or int(data_month)==12) and (not 1<=int(data_day)<=31):
	print("Day Invalid.")
elif (int(data_month)==4 or int(data_month)==6 or int(data_month)==9 or int(data_month)==11) and (not 1<=int(data_day)<=30):
	print("Day Invalid.")
elif(int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0))) and int(data_month)==2 and (not 1<=int(data_day)<=29):
	print("Day Invalid.")
elif (not(int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==2 and (not 1<=int(data_day)<=28):
	print("Day Invalid.")
elif not 1<=int(data_day)<=31:
	print("Day Invalid.")
else:
	print("Yes! The date is Valid!")

if not 1<=int(data_month)<=12:
	if not 1<=int(data_day)<=31:
		print("Day Invalid.")



#the program below is to count the day(normal year)
if (not(int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==1 and 1<=int(data_day)<=31:
	d=int(data_day)
elif (not(int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==2 and 1<=int(data_day)<=28:
	d=31+int(data_day)
elif (not(int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==3 and 1<=int(data_day)<=31:
	d=31+28+int(data_day)
elif (not(int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==4 and 1<=int(data_day)<=30:
	d=31+28+31+int(data_day)
elif (not(int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==5 and 1<=int(data_day)<=31:
	d=31+28+31+30+int(data_day)
elif (not(int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==6 and 1<=int(data_day)<=30:
	d=31+28+31+30+31+int(data_day)
elif (not(int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==7 and 1<=int(data_day)<=31:
	d=31+28+31+30+31+30+int(data_day)
elif (not(int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==8 and 1<=int(data_day)<=31:
	d=31+28+31+30+31+30+31+int(data_day)
elif (not(int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==9 and 1<=int(data_day)<=30:
	d=31+28+31+30+31+30+31+31+int(data_day)
elif (not(int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==10 and 1<=int(data_day)<=31:
	d=31+28+31+30+31+30+31+31+30+int(data_day)
elif (not(int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==11 and 1<=int(data_day)<=30:
	d=31+28+31+30+31+30+31+31+30+31+int(data_day)
elif (not(int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==12 and 1<=int(data_day)<=31:
	d=31+28+31+30+31+30+31+31+30+31+30+int(data_day)
else:
	d=0





#the program below is to count the day(leap year)
if ((int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==1 and 1<=int(data_day)<=31:
	d=int(data_day)
elif ((int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==2 and 1<=int(data_day)<=29:
	d=31+int(data_day)
elif ((int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==3 and 1<=int(data_day)<=31:
	d=31+29+int(data_day)
elif ((int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==4 and 1<=int(data_day)<=30:
	d=31+29+31+int(data_day)
elif ((int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==5 and 1<=int(data_day)<=31:
	d=31+29+31+30+int(data_day)
elif ((int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==6 and 1<=int(data_day)<=30:
	d=31+29+31+30+31+int(data_day)
elif ((int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==7 and 1<=int(data_day)<=31:
	d=31+29+31+30+31+30+int(data_day)
elif ((int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==8 and 1<=int(data_day)<=31:
	d=31+29+31+30+31+30+31+int(data_day)
elif ((int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==9 and 1<=int(data_day)<=30:
	d=31+29+31+30+31+30+31+31+int(data_day)
elif ((int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==10 and 1<=int(data_day)<=31:
	d=31+29+31+30+31+30+31+31+30+int(data_day)
elif ((int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==11 and 1<=int(data_day)<=30:
	d=31+29+31+30+31+30+31+31+30+31+int(data_day)
elif ((int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==12 and 1<=int(data_day)<=31:
	d=31+29+31+30+31+30+31+31+30+31+30+int(data_day)

#the program below is to show the day of the year
if d!=0:
	print(data+" is the No.",d,"day of the year.")



