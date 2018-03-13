# site24x7-miner
MineMeld Miner for gathering Site24x7 web monitoring public IPs, implemented as an extension

## How it works

This Miner periodically checks Site24x7's public JSON list of monitoring service public IP ranges (https://www.site24x7.com/multi-location-web-site-monitoring.html) for updates to the list.

## Requirements
MineMeld >= 0.9.44

## Installation
In SYSTEM > EXTENSIONS (the little grid icon on the left), install the extension using the "git" button and pasting this url:
https://github.com/bilalbox/site24x7-miner.git

## Miner
To use the Miner, go to CONFIG > "enable expert mode" button > "add node" button. You can create a new miner node by searching for "site24x7.IPv4" or "site24x7.IPv6" under the MINER Prototypes. Send it through a processing node or output node that accepts HC GREEN and you can begin using the new indicators. Don't forget to COMMIT!
