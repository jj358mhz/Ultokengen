Ultokengen
==========

04-22-2014

The Ultokengen is a Python script (based on the upLynk API) that when executed, prompts the user for a series of parameters and then compiles a playback URL for DRM-protected content.

The script mints the token based on a number of parameters and appends them to the end of the playback URL.

The expiration time of the token hard-coded at current UTC time + 120 seconds.

  What you will be prompted for is:
    1.       Your WAN IP address
    2.       The API key (found in upLynk CMS)
    3.       The protected playback URL
    4.       Asset type
    5.       GUID (found in the upLynk CMS)
    6.       Customization parameters (see upLynk CMS documentation: http://support.uplynk.com/doc_digital_rights_management.html)
