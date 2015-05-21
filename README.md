# Ultokengen

Ultokengen is a **Python** program (based on the upLynk API) that when executed, prompts the user for a series of parameters and then compiles a playback URL for DRM-protected content.

Two versions of the program are included that are optimized to run in different environments:

* **native UNIX/Linux (ultokengen2.py)**

* **native Windows (ultokengen2_win.py)**

The programs mints the token based on a number of parameters and appends them to the end of the playback URL.

The expiration time of the token hard-coded at current UTC time + 100 year (3,136,320,000 seconds).

## Installation

Browse to your desired install sub-directory and run the following code:

* For **UNIX/Linux**

```PYTHON
curl "https://raw.githubusercontent.com/jj358mhz/Ultokengen/master/ultokengen2.py" -o ultokengen2.py
```

* For **Windows**

```PYTHON
curl "https://raw.githubusercontent.com/jj358mhz/Ultokengen/master/ultokengen2_win.py" -o ultokengen2_win.py
```

## What you will be prompted for is:
* The API key (found in upLynk CMS)
* The protected playback URL
* Asset type
