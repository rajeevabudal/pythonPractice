# import sys
# print("Python version");
# print(sys.version);
# print("Version info:");
# print(sys.version_info);

# radius = int(input("Enter the radius = "));
# PI = 3.14;
# area = PI * radius**2;
#
# print(area);

# firstName = input("Enter your first name = ");
# lastName = input("Enter your last name = ")
#
# print(lastName + " " + firstName);


# values = input("Enter the numbers to convert to the list and tuples = ");
#
# list = values.split(",");
# tuples = tuple(list);
#
# print(list,"\n", tuples);


# fileName = input("Enter the file name")
# print(fileName.split(".")[1])


# color_list = ["Red","Green","White" ,"Black"]
#
# print(color_list[0], color_list[3])

# n = int(input("Enter the input to compute"));
#
# n1 = int("%s" %n);
# n2 = int("%s%s" %(n,n))
# n3 = int("%s%s%s" %(n,n,n))
# result = n1+n2+n3
# print(result);


# print(abs.__init__);

import calendar

from datetime import date

# year = 2023
# month = 12
#
# print(calendar.month(year, month))


firstDate = date(2018, 7, 9);
lastDate = date(2023, 12, 12);

print((lastDate-firstDate).days ,"days")