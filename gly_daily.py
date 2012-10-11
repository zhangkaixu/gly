#!/usr/bin/python3
import datetime

records=[]

for line in open('gly.txt'):
    line=line.strip()
    if '-' in line:
        records.append([line])
    else:
        records[-1].append(int(line.split(':')[-1][:-1]))

id=0
daily={}
records=[x for x in records if len(x)==4]
for t,i,o,s in records:
    t=t.split()[0]
    if t not in daily:daily[t]=[]
    daily[t].append(s)

daily=[[k,max(v)] for k,v in daily.items()]
daily=sorted(daily)
file=open("gly30.html",'w')
html="""<b>鼓浪屿每日最高在岛人数</b><br/>"""
print(html,file=file)
for d,s in daily[-30:]:
    x=round(s//1000)
    date=(datetime.date(*map(int,d.split('-'))))
    
    weekend=date.weekday()>4

    d=d if not weekend else "<font color=red>%s</font>"%(d,)
    print(d,'<span style="background:blue;display:inline-block;display:-moz-inline-box;width:%ipx;" >%i</span>'%(x*2,s),"<br/>",file=file)
