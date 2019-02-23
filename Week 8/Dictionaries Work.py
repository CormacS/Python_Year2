fo = open("output.html", "w")
fo.write('<!DOCTYPE html>\
    <html>\
    <head lang="en">\
    <meta charset="UTF-8">\
    <title>Tag Cloud Generator</title>\
    </head>\
    <body>\
    <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')

import string

count_dict = {}
my_file = open("gettysburg.txt", "r")

lines = my_file.read()

lines = lines.lower()

bad_chars = string.punctuation

for i in bad_chars:
    lines = lines.replace(i, "")

lines = lines.split()

for word in lines:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1


for key, value in count_dict.items():
    fo.write('<span style="font-size: {}px"> {} </span>'.format(value * 10, key))


fo.write('</div>\
    </body>\
    </html>')

fo.close()
my_file.close()
