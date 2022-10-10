# INITIALIZATION
import datetime
import csv

hand = open('test_files_monthly.csv')
file_reader = csv.reader(hand, delimiter=',')

month = datetime.datetime.now().month
months = ['Janurary', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
month_chr = months[int(month) - 1]

# html tags needed for creating a bulleted list, bolding text, using paragraph and link formatting,
list_open = '<ul>'
list_close = '</ul>'
bullet_open = '<li>'
bullet_close = '</li>'
link_open = '<a href="'
link_url = '">'
link_close = '</a>'
bold_open = '<strong>'
bold_close = '</strong>'
div_open = '<div>'
div_close = '</div>'
par_open = '<p>'
par_close = '</p>'

section = ''
section_closer = list_close + div_close

monthly_email = open('monthly_email.html', 'w')

# MANIPULATION
# filter file_reader to current month by date date_modified

# ist of assets by product / sotluion
dict = {}
for row in file_reader:
    if row[7] == 'folder_par':
        continue
    else:
        section = row[7]
        section_opener = div_open + par_open + bold_open + section + bold_close + par_close + list_open
        name = row[3]
        url = row[4]
        desc = row[5]
        type = row[6]
        bullet = bullet_open + type + ' - ' + link_open + url + link_url + name + link_close + ': ' + desc + bullet_close
        # print(bullet)
        dict[section] = dict.get(section, section_opener) + bullet

body = ''
for section in dict:
    dict[section] = dict.get(section) + section_closer
    body = body + dict[section]

# HTML_TEMPLATE
salutation = '<p>Hi there, Sales Team:</p>'
opening_par = '<p>Hope you all are doing well! The last month has been busy for marketing in terms of developing new and updated materials. To make sure you have access to the latest and greatest, below is a summary.</p>'
body
closing_par = '<p>Thanks, and please let me know if you have any questions!</p>'

html_template = salutation + opening_par + body + closing_par
monthly_email.write(html_template)
