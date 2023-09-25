import requests

# url from London Air
url = 'http://api.erg.ic.ac.uk/AirQuality/Information/MonitoringSites/GroupName=London/Json'

response = requests.get(url)

sites = response.json()

# code to extract all available data about monitoring sites in London area, every site will be on a new line
with open("./sites.tsv", "w") as file:
    file.write('LocalAuthorityName\tSiteCode\tSiteName\tSiteType\tDateClosed\tDateOpened\tLatitude\tLongitude\n')
    for site in sites['Sites']['Site']:
        file.write(site['@LocalAuthorityName'])
        file.write('\t')
        file.write(site['@SiteCode'])
        file.write('\t')
        file.write(site['@SiteName'])
        file.write('\t')
        file.write(site['@SiteType'])
        file.write('\t')
        file.write(site['@DateClosed'])
        file.write('\t')
        file.write(site['@DateOpened'])
        file.write('\t')
        file.write(site['@Latitude'])
        file.write('\t')
        file.write(site['@Longitude'])
        file.write("\n")

