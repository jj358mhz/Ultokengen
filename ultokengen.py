import hashlib, time, hmac, urllib

# inputs
ip = raw_input('Enter your IP address : ') # the user's IP address; normally obtained from the server itself
print ("Hi %s, I know where you live!" % ip);
apiKey = raw_input('Enter your API key : ') # from the CMS UI
print ("Shhhhh, be sure to keep %s secret!" % apiKey);
pbURL = raw_input('Enter the Playback URL : ') # the playback URL from the upLynk CMS
print ("%s, interesting URL" % pbURL);
ct = raw_input('Enter the content type, a for asset or c for live channel : ') # the content type
print ("%s. Cool" % ct);
cid = raw_input('Enter the GUID : ') # the content ID from the upLynk CMS
print ("Wow, %s is a big number!" % cid);
rays = raw_input('Enter the customization parameters, abc : ') # customization parameter
print ("With this %s, I can begin to compute" % rays);

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