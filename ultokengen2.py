__author__ = ''

import hashlib
import time
import hmac
import urllib
import random

# inputs
apiKey = raw_input('Enter your API key : ')  # from the CMS UI
url = raw_input('Enter the Playback URL : ')  # the playback URL from the upLynk CMS
ct = raw_input('Enter the content type, "a" for asset or "c" for live channel : ')  # the content type
cid = raw_input('Enter the GUID : ')  # the content ID from the upLynk CMS
#rays = raw_input('Enter the customization parameters, abc : ')  # customization parameter

# combine all of the parameters except the signature
queryStr = urllib.urlencode(dict(
    tc='1',  # token check algorithm version
    exp=int(time.time()) + 3136320000,  # expire 100 years from now
    rn=str(random.randint(0, 2**32)),  # random number
    ct=ct,  # an asset
    cid=cid,  # the asset's ID
    #rays=rays,  # customization parameter
))

# compute the signature and add it to the *end*
sig = hmac.new(apiKey, queryStr, hashlib.sha256).hexdigest()
queryStr = queryStr + '&sig=' + sig

# The token would then be added to a playback URL, e.g.
turl = url + '?' + queryStr
print ("Standard URL: "+turl)

# The following code provides a XML-compliant URL
new_string = turl.replace('&', '&#38;')
final_url = new_string.replace('?', '&#63;')
print ("XML-compliant URL: "+final_url)