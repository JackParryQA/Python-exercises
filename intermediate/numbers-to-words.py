import math

num2words={1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen', 20:'Twenty', 30:'Thirty', 40:'Fourty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety', 100:'One Hundred'}

def number(num):
    div=divmod(num, 10)
    if num>=1 and num<=19:
        return num2words[num]
    elif num>19 and num<=100:
        return num2words[(div[0])*10] + " " + num2words[div[1]]
    elif num>100 and num<=110:
        return num2words[(div[0])*10] + " and " + num2words[div[1]]
    else:
        return "Number out of range!"

num=int(input())


# print(div)
print(number(num))
