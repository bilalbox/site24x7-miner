# incapsula-miner
MineMeld Miner for Incapsula public IPs implemented as an extension

## How it works

This Miner periodically checks Imperva's Incapsula API (https://my.incapsula.com/api/integration/v1/ips) for updates to the list of IP addresses associated with their WAF service.

## Requirements
MineMeld >= 0.9.44

## Installation
In SYSTEM > EXTENSIONS (the little grid icon on the left), install the extension using the "git" button and pasting this url:
https://github.com/bilalbox/incapsula-miner.git

## Miner
To use the Miner, go to CONFIG > "enable expert mode" button > "add node" button. You can create a new miner node by searching for "incapsula.IPv4" or "incapsula.IPv4" under the MINER Prototypes. Send it through a processing node or output node that accepts HC GREEN and you can begin using the new indicators. Don't forget to COMMIT!
