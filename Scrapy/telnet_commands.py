"""
TELNET IS VERY SLOW IN WINDOWS SO NEVER TRIED ANY OF THESE BUT IT SHOULD WORK IN LINUX
WHILE YOU ARE CRAWLING USING ONE TERMINAL OPEN ANOTHER AND USE BELOW
FIRST ENABLE TELNET
"https://community.talend.com/t5/Migration-Configuration-and/Telnet-is-not-recognized-as-an-internal-or-external-command/ta-p/117226"
dism /online /Enable-Feature /FeatureName:TelnetClient
telnet localhost 6023
default username: scrapy

crawler.stats.get_stats()
print("\n\n\n\n\\n\n") - just workarounf for clear screen
p(crawler.stats.get_stats()) - p works like pprint
est()
p(slot.inprogress)
engine.pause()
engine.unpause()
engine.stop()
"""