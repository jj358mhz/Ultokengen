import hashlib, time, hmac, urllib

# inputs
ip = '72.27.179.200' # the user's IP address; normally obtained from the server itself
apiKey = 'WxQpQhHFmE4hTWA4TGLu6rYeNuKgYrWwlCLmSKRb' # from the CMS UI

# combine all of the parameters except the signature
queryStr = urllib.urlencode(dict(
    exp = int(time.time()) + 120, # expire 120 seconds from now
    ct = 'a', # an asset
    cid = 'ea10fa402fec4bbe996019a0827e6c38', # the asset's ID
    iph = hashlib.sha256(ip).hexdigest(), # the user's IP address hash
    rays = 'abc', # customization parameter
))

# compute the signature and add it to the *end*
sig = hmac.new(apiKey, queryStr, hashlib.sha256).hexdigest()
queryStr = queryStr + '&sig=' + sig

# The token would then be added to a playback URL, e.g.
url = 'http://content.uplynk.com/ea10fa402fec4bbe996019a0827e6c38.m3u8'
url = url + '?' + queryStr
