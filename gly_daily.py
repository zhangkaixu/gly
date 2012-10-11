#!/usr/bin/python3

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
for d,s in daily[-30:]:
    x=round(s//1000)
    print(d,s,"<br/>",file=file)
