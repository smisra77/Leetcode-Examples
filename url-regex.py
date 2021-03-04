#Find URL in HTML
import re

regex = r'<a[^>]* href="([^"]*)"'

html = '''
<a href="http://something" title="Development of the Python language and website">Core Development</a>
<a href="http://something.com" title="Development of the Python language and website">Core Development</a>
'''

match = re.findall(regex, html)
print("URLs: ", match)
