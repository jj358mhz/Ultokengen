# ultokengen2
# Version 1.1.4

# Copyright (C) 2014-2017 Jeff Johnston <jj358mhz@gmail.com>

'''
This program will tokenize a DRM-protected URL
provided a valid API key is entered when prompted.
It will present both a standard tokenized playback URL and
one that is XML-compliant for XML feed readers.
'''

import hashlib
import time
import hmac
import urllib
import random

# inputs
apiKey = raw_input('Enter your API key : ')  # from the CMS UI
url = raw_input('Enter the Playback URL : ')  # the playback URL from the upLynk CMS
ct = raw_input('Enter the content type, "a" for asset or "c" for live channel or "e" for live event : ')  # the content type
cid = url.split('/')[-1][:-5]  # extracts the GUID
print ("The extracted GUID is: "+cid)
rays = raw_input('Enter the customization parameters, abc : ')  # customization parameter, uncomment if needed
ad = raw_input('Enter the ad server name : ')  # customization parameter, uncomment if needed

# combine all of the parameters except the signature
queryStr = urllib.urlencode(dict(
    tc='0',  # token check algorithm version; 0 = no check, 1 = check
    exp=int(time.time()) + 3136320000,  # expire 100 years from now
    rn=str(random.randint(0, 2**32)),  # random number
    ct=ct,  # an asset
    cid=cid,  # the asset's ID
    rays=rays,  # customization parameter, uncomment if needed
    ad=ad,  # customization parameter, uncomment if needed
))

# compute the signature and add it to the *end*
sig = hmac.new(apiKey, queryStr, hashlib.sha256).hexdigest()
queryStr = queryStr + '&sig=' + sig

# the token would then be added to a playback URL, e.g.
turl = url + '?' + queryStr
print ('Standard URL: '+turl)

# the following code provides a XML-compliant URL
new_string = turl.replace('&', '&#38;')
final_url = new_string.replace('?', '&#63;')
print ('XML-compliant URL: '+final_url)
