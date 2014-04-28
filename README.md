# Ultokengen

The Ultokengen is a **Python** program (based on the upLynk API) that when executed, prompts the user for a series of parameters and then compiles a playback URL for DRM-protected content.

Two versions of the program are included that are optimized to run in different environments:

* **native UNIX/Linux (ultokengen.py)**

* **native Windows (ultokengen_win.py)**

The programs mints the token based on a number of parameters and appends them to the end of the playback URL.

The expiration time of the token hard-coded at current UTC time + 1 year (31,557,600 seconds).

## What you will be prompted for is:
* Your WAN IP address
* The API key (found in upLynk CMS)
* The protected playback URL
* Asset type
* GUID (found in the upLynk CMS)
* Customization parameters - see upLynk CMS documentation: (http://support.uplynk.com/doc_digital_rights_management.html)
