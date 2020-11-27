# save-flow.py
mitmproxy script to save flows to disk

## Prerequisites

This script has been tested to work with mitmproxy v4.0 and Python v3.7.  It saves the flows to /tmp/XXXXXXXXX.flow, where 'XXXXXXXXX' is a filename generated based upon the HTTP request timestamp and URI.

## Usage

Here's I use the script:

`mitmproxy --listen-port 8080 --ssl-insecure --scripts ~/mitmproxy/scripts/save-flow.py`

## DISCLAIMER

This code is offered with no warranties or guarantees as to its effectiveness or reliability whatsoever.  It was produced for my own personal use and I offer it here in case others in the community might find it useful.  Use this code at your own risk.

## Contact Info

Please direct any questions/comments/concerns to https://twitter.com/TheRealNerdwell.
