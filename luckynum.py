#A number with only 1s,7s and 9s
#is considered a lucky number.The
#goal of the code is to check if
#input number is lucky or not.
#we consider that the number is
#positive integer.



n = int(input())
#the above line is used to check
#if the input does not contain
#letters and convert a flot to int.
#in the former cse it returns errors.
count = 0
check = str(2345680)
#common properties between string and
#list is exploited in below code
while (n>0):
    for char in str(n):
        if( str(char) in check):
                count = count-1
                break

    n = (n)-1
    count = count+1
print(count)
