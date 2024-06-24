"""
Write a program that can display the name of selected browser
1. declare a String variable named browser_name
2. Assume that the valid browsers are: chrome, firefox, opera, safari, edge.
3. if the browser name does not match with the valid browser names, out put should be: Invalid Browser Name

Ex: String browser = "chrome";
Output: Chrome Browser is selected
Note: MUST use nested if
"""

browser_name = input('Enter your browser: ')
output = '{} Browser is selected'.format(browser_name)
if browser_name == 'chrome':
    print(output)
elif browser_name == 'firefox':
    print(output)
elif browser_name == 'opera':
    print(output)
elif browser_name == 'safari':
    print(output)
elif browser_name == 'edge':
    print(output)
else:
    print('Invalid browser {}'.format(browser_name))
