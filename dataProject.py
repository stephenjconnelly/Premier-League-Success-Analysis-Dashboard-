import pandas as pd
from functools import partial
import warnings
import requests as r

#warnings.filterwarnings("error")
urls = [
    "https://www.football-data.co.uk/mmz4281/2223/E0.csv",
    "https://www.football-data.co.uk/mmz4281/2122/E0.csv",
    "https://www.football-data.co.uk/mmz4281/2021/E0.csv",
    "https://www.football-data.co.uk/mmz4281/1920/E0.csv",
    "https://www.football-data.co.uk/mmz4281/1819/E0.csv",
    "https://www.football-data.co.uk/mmz4281/1718/E0.csv",
    "https://www.football-data.co.uk/mmz4281/1617/E0.csv",
    "https://www.football-data.co.uk/mmz4281/1516/E0.csv",
    "https://www.football-data.co.uk/mmz4281/1415/E0.csv",
    "https://www.football-data.co.uk/mmz4281/1314/E0.csv",
    "https://www.football-data.co.uk/mmz4281/1213/E0.csv",
    "https://www.football-data.co.uk/mmz4281/1112/E0.csv",
    "https://www.football-data.co.uk/mmz4281/1011/E0.csv",
    "https://www.football-data.co.uk/mmz4281/0910/E0.csv",
    "https://www.football-data.co.uk/mmz4281/0809/E0.csv",
    "https://www.football-data.co.uk/mmz4281/0708/E0.csv",
    "https://www.football-data.co.uk/mmz4281/0607/E0.csv",
    "https://www.football-data.co.uk/mmz4281/0506/E0.csv",
    "https://www.football-data.co.uk/mmz4281/0405/E0.csv",
    "https://www.football-data.co.uk/mmz4281/0304/E0.csv",
    "https://www.football-data.co.uk/mmz4281/0203/E0.csv",
    "https://www.football-data.co.uk/mmz4281/0102/E0.csv",
    "https://www.football-data.co.uk/mmz4281/0001/E0.csv",
    "https://www.football-data.co.uk/mmz4281/9900/E0.csv",
    "https://www.football-data.co.uk/mmz4281/9899/E0.csv",
    "https://www.football-data.co.uk/mmz4281/9798/E0.csv",
    "https://www.football-data.co.uk/mmz4281/9697/E0.csv",
    "https://www.football-data.co.uk/mmz4281/9596/E0.csv",
    "https://www.football-data.co.uk/mmz4281/9495/E0.csv",
    "https://www.football-data.co.uk/mmz4281/9394/E0.csv",
]

mapfunc = partial(pd.read_csv, encoding='unicode_escape', on_bad_lines='skip', usecols = ['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'FTAG', 'FTHG'])
df = pd.concat(map(mapfunc,urls), ignore_index=True).dropna().iloc[::-1]
df = df.replace('/', '-', regex=True)
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y')
# print(pd.asdate("05/08/2022"))%d-%m-

print(df)
teams = [
    "Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton", "Chelsea", "Crystal Palace",
    "Everton", "Fulham","Leeds", "Leicester", "Liverpool", "Man City", "Man United", "Newcastle", "Nott'm Forest",
    "Southampton", "Tottenham", "West Ham", "Wolves", "Barnsley", "Birmingham", "Blackburn",
    "Blackpool", "Bolton", "Bradford", "Burnley", "Cardiff", "Charlton", "Coventry", "Derby",
    "Huddersfield", "Ipswich", "Middlesbrough", "Norwich", "Oldham", "Portsmouth",
    "QPR","Reading", "Sheffield United", "Sheffield Weds", "Stoke", "Sunderland", "Swansea",
    "Swindon", "Watford","West Brom", "Wigan", "Wimbledon"
]

teamWin = [[]]
teamPn = [[]]
for t in teams:
    #select_team_goals = df.loc[(df['HomeTeam'] == t) | (df['AwayTeam'] == t)]
    #df['obj1_count'] = (df['object'] == 'obj1').cumsum()
    df[t] = (((df['HomeTeam'] == t) & (df['FTR'] == 'H'))|((df['AwayTeam'] == t) & (df['FTR'] == 'A'))).cumsum()
    select_team = df.loc[((df['HomeTeam'] == t) & (df['FTR'] == 'H'))|((df['AwayTeam'] == t) & (df['FTR'] == 'A'))]
    sumGoals = df.loc[((df['HomeTeam'] == t), 'FTHG')].sum() + df.loc[((df['AwayTeam'] == t), 'FTAG')].sum()
    teamPn.append([t, sumGoals])
    numRows = len(select_team)
    teamWin.append([t, numRows])
print(df)
teamWin.pop(0)
teamPn.pop(0)
teamWin.sort(key=lambda x: x[1], reverse=True)
teamPn.sort(key=lambda x: x[1], reverse=True)
print(teamWin)
print(teamPn)

