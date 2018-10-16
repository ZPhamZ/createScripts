Applications = ['app1',
'app2',
'app3',
'app4',
'app5']

for App in Applications:    
    devFile = open('%s.py' % App, 'w+')
    devFile.write('import requests\r\n')
    devFile.write('requests.get(http://***domain=Production&application='+App+'&status=start)\r\n')
    devFile.write('print('"'"+'Starting Application'+App+"'"+')\r\n\n')
    devFile.close()