#!/usr/bin/env python

# Version 1.02 (28-Apr-2014)

import hashlib, time, hmac, urllib

# inputs
ip = raw_input('Enter your IP address : ') # the user's IP address
apiKey = raw_input('Enter your API key : ') # from the CMS UI
pbURL = raw_input('Enter the Playback URL : ') # the playback URL from the upLynk CMS
ct = raw_input('Enter the content type, a for asset or c for live channel : ') # the content type
cid = raw_input('Enter the GUID : ') # the content ID from the upLynk CMS
rays = raw_input('Enter the customization parameters, abc : ') # customization parameter

# combine all of the parameters except the signature
queryStr = urllib.urlencode(dict(
    exp = int(time.time()) + 31557600, # expire 1 year from now
    ct = ct, # an asset
    cid = cid, # the asset's ID
    iph = hashlib.sha256(ip).hexdigest(), # the user's IP address hash
    rays = rays, # customization parameter
))

# compute the signature and add it to the *end*
sig = hmac.new(apiKey, queryStr, hashlib.sha256).hexdigest()
queryStr = queryStr + '&sig=' + sig

# The token would then be added to a playback URL, e.g.
url = pbURL + '?' + queryStr
print (url)
