import requests

# initial ulez

sites_in_ulez = ['BL0', 'IM1', 'CT4', 'CT2', 'CT3', 'CT6', 'MR8', 'SK6', 'WM5', 'WM0', 'MY1', 'WM6', 'NB1']
path_in_ulez = './no2_in_ulez.csv'

# expanded ulez
sites_exp_ulez = ['BT4', 'BT6', 'BT5', 'BL0', 'IM1', 'CD1', 'CT4', 'CT2', 'CT3', 'CT6', 'EA6', 'EA8', 'EI8', 'EI1', 'EN5', 'GR7', 'GR9', 'GR8', 'HK6', 'HG4', 'HG1', 'IS6', 'IS2', 'KC1', 'LB5', 'LB4', 'LW4', 'LW2', 'MR8', 'NM2', 'NM3', 'RB4', 'RI2', 'RI1', 'SK5', 'SK9', 'SK6', 'TH4', 'TH2', 'WAA', 'WAC', 'WA9', 'WA7', 'WA8', 'WA2', 'WM5', 'WM0', 'MY1', 'WM6', 'NB1']
path_exp_ulez = './no2_exp_ulez.csv'


# The function below goes through list of monitoring sites' codes, puts it in the link and extracts data for each site in the list,
# writes the data to the file. If...else allows us to get the first line (columns names) only from the first site,
# then we get rows with the actual data only to avoid duplicates of column names
def no2_extraction(sites, file_path):
    with open(file_path, 'w') as file:
        for i in range(len(sites)):
            site = sites[i]
            response = requests.get('https://www.londonair.org.uk/london/asp/downloadsite.asp?site={}&species1=NO2m=&start=1-jan-2017&end=1-jan-2023&res=6&period=daily&units=ugm3'.format(site))
            if i == 0:
                file.write(response.text)
            else:
                lines = response.text.split('\n')
                data_lines = '\n'.join(lines[1:])
                file.write(data_lines)

# initial ulez
no2_extraction(sites_in_ulez, path_in_ulez)

# expanded ulez
no2_extraction(sites_exp_ulez, path_exp_ulez)

