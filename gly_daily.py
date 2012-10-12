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
html="""
<head>
<title>鼓浪屿每日在岛人数</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<script type="text/javascript">

  var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-33732606-3']);
      _gaq.push(['_trackPageview']);

        (function() {
                var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
                    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
                        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
                          })();

        </script>
</head>

<b>鼓浪屿每日在岛人数峰值</b>(包括常住人口1.5万左右)<br/>
由<a href="http://weibo.com/zhangkaixu">@张开旭XMU</a>发布<br/>
"""
print(html,file=file)
for d,s in daily[-30:]:
    x=round(s//1000)
    date=(datetime.date(*map(int,d.split('-'))))
    
    weekend=date.weekday()>4

    d=d if not weekend else "<font color=red>%s</font>"%(d,)
    print(d,'<span style="background:blue;display:inline-block;display:-moz-inline-box;width:%ipx;" >%i</span>'%(x*2,s),"<br/>",file=file)
