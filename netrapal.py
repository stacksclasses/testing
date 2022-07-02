# dat=this is my name")
# st=""
# num=
# for i in range(0,len(dat)):
#     ch = dat[i]
#     st+=num
#     num=num-1
#
# print(st)

# arr1=[2,5,8,19]
# arr2=[3,6,10,12]
# z=[]
# for i in range(0,len(arr1)):
#     z.append(arr1)
#     z.append(arr2)
# print(z)
import datetime

class MyDate:

    week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    x=["","jan","feb","mar","april","may","june","july","august","sept","oct","nov","dec"]
    def __init__(self,Date):
        z=Date.split("/")
        a=list(map(int,z))
        self.date=a[0]
        self.mon=a[1]
        self.year=a[2]

    def printDate(self):
        print(self.date,self.mon,self.year)
    def printDateMon(self):
        print(self.date,MyDate.x[self.mon],self.year)
    def getDate(self):
        return self.printDate()
    def getMon(self):
        return self.mon
    def getMonthName(self):
         return MyDate.x[self.mon]
    def getYear(self):
        return self.year
    def isLeapYear(self):
        if self.year%400==0:
            print("Leap year")
        elif self.yaer%4==0 and self.year%100!=0:
            print("leap Year")
        else:
            print("Not LeapYear")
    def getDay(self):
        week_num=datetime.date(self.year,self.mon,self.date).weekday()
        print(MyDate.week_days[week_num])

    def after(self,d2):
        z=d2.split("/")
        a=list(map(int,z))
        self.date2=a[0]
        self.mon2=a[1]
        self.year2=a[2]
        if (self.year < self.year2)or(self.year < self.year2 and self.mon < self.mon2 ) or\
                (self.year==self.year2 and self.mon==self.mon2 ) or self.date < self.date2:
            print("True")
    def before(self,d2):
        z=d2.split("/")
        a=list(map(int,z))
        self.date2=a[0]
        self.mon2=a[1]
        self.year2=a[2]
        if (self.year >self.year2)or(self.year > self.year2 and self.mon >self.mon2 ) or\
                (self.year==self.year2 and self.mon==self.mon2 ) or self.date >self.date2:
            return true
    def compareTo(self,d2):
        z=d2.split("/")
        a=list(map(int,z))
        self.date2=a[0]
        self.mon2=a[1]
        self.year2=a[2]
        if self.year==self.year2 or self.mon==self.mon2 or self.date==self.date2:
            return True
        elif self.year >self.year2 or self.mon > self.mon2 or self.date > self.date2:
            return("1")
        else:
            return ("-1")
    # def diff(self,d2):
    #     day_30 = [4,6,9,11]
    #     z=d2.split("/")
    #     a=list(map(int,z))
    #     days = 0
    #     temp = self.year
    #     while(a[2]>temp+1) or (a[2]==temp+1 and a[1]>self.mon) or (a[2]==temp+1 and a[1]==self.mon and a[1]>=self.mon):
    #         if temp%400 ==0 or (temp%4 == 0 and temp!=100):days +=366
    #         else:days+=365
    #         temp+=1
    #     mon_loop = a[1]-self.mon if self.mon<=a[1] else 12-self.mon+a[1]
    #     mo_temp = a[1]
    #     for _ in range(1,mon_loop):
    #         if mo_temp ==2 :
    #             if temp%400 ==0 or (temp%4 == 0 and temp!=100):
    #                 days +=29
    #             else:
    #                 days +=29
    #         if temp in mo_temp:
    #         if mo_temp ==12:mo_temp=1
    #         else:temp +=1

#
#         print(days,mon_loop)
# t=MyDate("1/5/2000")
# t.diff("1/2/2002")
#



st = "100/6+90/5" #21
def val():
    global st
    sign = ['+','-','/','*']
    temp = ''
    for i in st:
        if i not in sign:
            temp +=i
            st = st[1:]
        else:
            return  temp
    else:
        return  temp

def valu(v1,v2,v3):
    if v3=='*':
        return  int(v1)*int(v2)
    if v3 == '+':
        return int(v1)+int(v2)
    if v3 == '-':
        return  int(v1)-int(v2)
    if v3 == '/':
        return  int(v1)//int(v2)
v1 = val()
v3 = st[0]
st = st[1:]
v2 = ''
for i in range(len(st)):
    if v1 and v2 and v3:
        v1 = valu(v1,v2,v3)
        v2 = ""
        v3 = st[0] if st else ''
        st = st[1:] if st else ''
    else:v2 = val()
else:
    if v1 and v2 and v3:
        v1 = valu(v1,v2,v3)
print(v1)
