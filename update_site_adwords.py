#!/usr/bin/env python
from sys import argv
import subprocess
import re
import get_expanded_text_ads
import remove_ad
import add_expanded_text_ads
from googleads import adwords

# this script updates amps website with new promotion text and pushes changes to github
# then it removes AdWord text ads with previous promotion
# finally it adds a new text ad with new promotion text
# new_promotion entered on command line when running script
new_promotion = argv[1]

# for AdWords, retrieved id using get_add_groups.py
AD_GROUP_ID = '53064600918'

# open and read the amps webpage markdown file, where page is stored
f = open('../Documents/heiberger.github.io/docs/amps.md', 'r')
text = f.read()
f.close()

# using regex, split the text into sections around the Promotions text
# text has this pattern <b>Promotions</b><br>some text here<span>
sections = re.split('<br>|<span>', text)

# open markdown down for writing (erasing previous copy)
f = open('../Documents/heiberger.github.io/docs/amps.md', 'w')

# write the first section of the page before ### Promotions Section
f.write(sections[0])

# write <br> (stripped during the reg.split operation)
f.write('<br>')

# write the new_promotion text
f.write(new_promotion)

# write the <span> (stripped during re.split) and the final section of text
f.write('<span>')

f.write(sections[2])
f.close()

# push the changed markdown file to GitHub to be served for webpage
subprocess.Popen(
    ['git', 'add', 'docs/amps.md'],
    cwd='../Documents/heiberger.github.io'
    ).wait()
subprocess.Popen(
    ['git', 'commit', '-m "Update amps.md Promotions"'],
    cwd='../Documents/heiberger.github.io'
    ).wait()
subprocess.Popen(['git', 'push'], cwd='../Documents/heiberger.github.io').wait()

# loads AdWords credentials (default is googleads.yaml under home directory)
adwords_client = adwords.AdWordsClient.LoadFromStorage()

# get existing ad ids
ids = get_expanded_text_ads.main(adwords_client, AD_GROUP_ID)

# remove any existing ads based on their id number
for id in ids:
    remove_ad.main(adwords_client, AD_GROUP_ID, id)

# add a new ad with new_promotion text
add_expanded_text_ads.main(adwords_client, AD_GROUP_ID, new_promotion)

print('finished')