# update_site_adwords

### update_site_adwords.py
The update_site_adwords.py script does the following actions when run at the command line<br>
(e.g., $python update_site_adwords.py 'sample text')

1. updates the amps.md markdown file with new 'sample text'
2. pushes the update to GitHub
3. removes previous AdWord ad using previous 'sample text'
4. adds a new ad using new 'sample text' as the description text in the ad

### other important files
* get_expanded_text_ads.py (modified from Google example code) gets current ad ID numbers
* remove_ad.py (modified from Google example code) removes any current ads based on ID numbers returned above
* add_expanded_text_ads.py (modified from Google example code) creates a new ad using new 'sample text' as description for ad
* googleads.yaml stores credentials for AdWords account (credentials omitted on attached version)
* add_keywords (from Google example code) adds keywords to the ad group, in this case 'tube amps' and 'amps' are added

### other files
* add_ad_groups.py (from Google example code) adds new ad group
* add_campaigns.py (from Google example code) adds new campaign
* get_ad_groups.py (from Google example code) get the ad group ID, necessary to add/remove ads from correct place
* get_campaigns.py (from Google example code) get the campaign ID, necessary to add/remove ad groups from correct place
