isbn = str(input("Enter first 12 digits of isbn: "))
check_num=0
count=0

for i in isbn:
    if count%2==0:
        check_num+=int(i)
    elif count%2!=0:
        check_num+=(int(i))*3
    count+=1
print(check_num)
check_num = check_num % 10
print(check_num)
check_num = 10-check_num

print(f"{isbn}{check_num}")