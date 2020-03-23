isAutomaticMode = False
print('isAutomaticMode=', isAutomaticMode)

is80PercentLight = True

isRainy = False

isDirectLight = False

lightsON = (isAutomaticMode and (is80PercentLight or isRainy or isDirectLight))
print("Traffic lights ON: ", lightsON)

v1=126

v2='126'

v3=126.0

v4='126.0'

print(type(v3))
print(v2+v4)
print(7-1*0+3+3)
print((4**5)/(2**3))

print(9+9+9**9)

q = 'THE EYES'
print(q[0] + q[1] + q[2] + q[5] + q[3] + q[7] + q[4] + q[6])

p = 'a gentleman'
print(p[3] +p[6] +p[7] +p[2] +p[0] +p[4] +p[5] +p[1] +p[8] + p[9:])

s = 'THE MORSE CODE'

print(s[1:3] + s[6] + s[13] + s[3] + s[10:12] + s[4] + s[2] + s[3] + s[12] + s[5] + s[0] + s[7])

line = 'Program "Kropka nad i" nadamy o: 22:00'

time = line.find(':')
print(line[time+2:time+7])

tmp = line[line.find('"')+1:]
print(tmp)

title = tmp[:tmp.find('"')]
print(title)
print(7+7/7+7*7-7)

obeconsćStudenta = 0.85
sredniaStudenta = 3.5
czyZaliczylEgzamin = False

czyZdal = (obeconsćStudenta >= 0.8 and sredniaStudenta >=3  and czyZaliczylEgzamin)
print(czyZdal)

hitsTitles = [ 'BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
hitsTitles.append( 'CHILD IN TIME')
hitsTitles.append('AGAIN')
hitsTitles.insert(2,'HOTEL CALIFORNIA')
hitsTitles.insert(0,'THE SOUND OF SILENCE')
print(hitsTitles.index('HOTEL CALIFORNIA'))
hitsTitles.remove(hitsTitles[3])

print(hitsTitles)

marketing = ['loyality program', 'client promotion', 'market research']
marketing.append('public relations')
marketing.insert(1, 'investor relations')
print(marketing)
emailMarketing = marketing.copy()
emailMarketing.sort()
print(emailMarketing)
internalEmails = ['internal communication']
emailMarketing.extend(internalEmails)
print(emailMarketing)
eMarketing = tuple(emailMarketing)
print(eMarketing)

channels = {'Google': '1480', 'Email': '300', 'Natural Traffic':'440', 'TV Spot':'700'}
print(channels)
print(channels['Email'])

channelsUpdate = {'Natural Traffic':'520', 'News':'600'}

channels.update(channelsUpdate)
print(channels)
print(channels.values())
channels.pop('Email')
print(channels)



