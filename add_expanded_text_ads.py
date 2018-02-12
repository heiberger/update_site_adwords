#!/usr/bin/env python
#
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This example adds expanded text ads to a given ad group.

To get ad_group_id, run get_ad_groups.py.

The LoadFromStorage method is pulling credentials and properties from a
"googleads.yaml" file. By default, it looks for this file in your home
directory. For more information, see the "Caching authentication information"
section of our README.

"""

import uuid

from googleads import adwords


AD_GROUP_ID = '53064600918'
NUMBER_OF_ADS = 1


def main(client, ad_group_id, ad_description):
  # Initialize appropriate service.
  ad_group_ad_service = client.GetService('AdGroupAdService', version='v201710')

  operations = [
      {
          'operator': 'ADD',
          'operand': {
              'xsi_type': 'AdGroupAd',
              'adGroupId': ad_group_id,
              'ad': {
                  'xsi_type': 'ExpandedTextAd',
                  'headlinePart1': ('Custom Tube Amps'),
                  'headlinePart2': 'Best in Hong Kong',
                  'description': ad_description,
                  'finalUrls': ['http://danielheiberger.com/docs/amps.html'],
              },
              # Optional fields.
              'status': 'ENABLED'
          }
      } for i in range(NUMBER_OF_ADS)
  ]
  ads = ad_group_ad_service.mutate(operations)

  # Display results.
  for ad in ads['value']:
    print ('Ad of type "%s" with id "%d" was added.'
           '\n\theadlinePart1: %s\n\theadlinePart2: %s\n\tdescription: %s'
           % (ad['ad']['Ad.Type'], ad['ad']['id'],
              ad['ad']['headlinePart1'], ad['ad']['headlinePart2'],
              ad['ad']['description']))


if __name__ == '__main__':
  # Initialize client object.
  adwords_client = adwords.AdWordsClient.LoadFromStorage()

  main(adwords_client, AD_GROUP_ID)
