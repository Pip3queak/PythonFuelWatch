import requests
from pprint import pprint
from feedparser import parse

#today's fuel prices
t = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Region=26')
tp=parse(t.text)
#ptp,indent=4)

#tomorrow's fuel prices
tom = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Region=26&Day=tomorrow')
tomp=parse(tom.text)
#ptomp,indent=4)

#ptp['entries'][0]['price'])
#ptomp['entries'][0]['price'])


todaylist = []
for px in tp['entries']:
    todaydict = {'price' : px['price'],'location' : px['location'],'address' : px['address'],'brand' : px['brand'],'updated' : px['updated']}
    todaylist.append(todaydict)

tomorrowlist = []
for px in tomp['entries']:
    tomorrowdict = {'price' : px['price'],'location' : px['location'],'address' : px['address'],'brand' : px['brand'],'updated' : px['updated']}
    tomorrowlist.append(tomorrowdict)

merge = todaylist + tomorrowlist

def sort_name(merge):
    return merge['price']
sorted(merge, key=sort_name)


html = '''
<html>
<style>
table,
td {
    border: 1px solid #333;
}

tbody tr:nth-child(odd) {
  background-color: #e6e6ff;
  color: #333399;
}

thead,
tfoot {
    background-color: #333;
    color: #fff;
}
</style>

    <body>
        <table>
'''
headcol = []
headcol.append('<thead><tr>')
for headers in merge[0]:
    headcol.append('<th>' + headers + '</th>')
headcol.append('</tr></thead>' + '\n')

rowcol = []
for rows in merge:
    rowcol.append('<tr>')
    for col in rows.values():
        rowcol.append('<td>' + col + '</td>')
    rowcol.append('</tr>' + '\n')

html_join = ''.join(headcol + rowcol)

html_footer = '''
        </table>
    </body>
</html>
'''

file = open('something2.html', 'w')
file.write(html + html_join + html_footer)
file.close()






'''
NOTES
---------------

for i in merge:
    print('<tr>')
    for x in i.values():
        print('<td>',x,'</td>')
    print('</tr>')
'''

'''
----
To Write into a file
----
>>> file = open('something2.html', 'w')
>>> file.write('<h1>Hello!</h1>')
15
>>> file.close()

'''
'''
l = [1,2,4] # this is a list
l[2] = 4 # this bracket is to access the index in the list

d = {'name':'Robin', 'age':44} # this is a dict
d['age'] = 44 # this square bracket is to access the value of the key 'age'
'''

'''
for keyz in tp['entries']:
    tp.keys(keyz))
type(keyz))
'''
'''
-----
String Manipulation
-----

>>> 'My name is ' + name
'My name is Robin'
>>> 'My first name is ' + first_name + ' and my last name is ' + last_name
'My first name is Robin and my last name is Chew'
>>> 'My first name is {} and my last name is {}'.format(first_name, last_name)
'The name is {1}. {0} {1}.'.format(firstname, lastname)
>>> 'The name is Chew. Robin Chew.'
'The name is {lname}. {fname} {lname}.'.format(fname=firstname, lname=lastname)
>>> 'The name is Chew. Robin Chew.'
'''


'''
l2 = [55,78,11]
l2.Sort() #sorts on the dictionary itself
sortedL2 = l2.Sorted() #needs to store sorted to remain sorted
SortMe = [{"num":4,"name":"xyz"}, {"num":1,"name":"eee"}, {"num":5,"name":"abc"}]
def sort_name(d):
    return d['name']
out(sorted(SortMe, key=sort_name))
out(sorted(SortMe, key=lambda d: d['num']))

#for today in t['price']:
#    todayprice.append(today)

#pmerge,indent=4)
'''
