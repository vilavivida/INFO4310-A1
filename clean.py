import pandas as pd

data= pd.read_csv("Street_Tree_List-2022-01-30_FILTERED.csv")

print(data['PlantDate'].isna().sum())
data['PlantDate'].fillna('1/1/54 0:00', inplace = True) 
yearList = []
count = 0
for year in data['PlantDate']:
    year = int(year.split(' ')[0].split("/")[2])
    if year < 23:
        if (len(str(year)) == 1):
            year = '0' + str(year)
        year = int('20' + str(year))
    else:
        year = int('19' + str(year))

    if year < 1955:
        year = "Post 1955"
        count += 1
    elif 1955 <= year <= 1970:
        year = "From 1955 to 1970"
    elif 1970 < year <= 1985:
        year = "From 1970 to 1985"
    elif 1985 < year <= 2000:
        year = "From 1985 to 2000"
    elif 2000 < year <= 2015:
        year = "From 2000 to 2015"
    else:
        year = "Most Recent Years"

    yearList.append(year)

data['PlantYear'] = yearList

data.to_csv('Street_Tree_List-2022-01-30_CLEANED.csv', index=False)
