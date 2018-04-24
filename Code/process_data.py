import pandas as pd
import json

df = pd.read_csv('../Data/Community_Resiliency_Indicator_System.csv')
df = df.fillna(0)
with open('../Data/san-francisco.json', 'r') as f:
    jo = json.loads(f.read())

score_dict = {'Haz_Score':['Flood_Per', 'Heat_Per', 'Liq_Per'], 
'Env_Score':['Imp_Per', 'Tree_Per', 'PM_Conc', 'Tox_Per'], 
'Trans_Score':['AT_Min', 'PTrans_Sco'], 
'Com_Score':['VCrim_Rate', 'Vot_Rate', 'NewSF_Per', 'Citz_Per', 'Eng_Per'], 
'PR_Score':['Food_Score', 'HS_Per', 'Pharm_Per'],
'House_Score':['LivAl_Per', 'EldLivAl_Per', 'OC_Per', 'Viol_Rate', 'AC_Per', 'Rent_Per'], 
'Ec_Score':['Emp_per'], 
'Health_Score':['Shelt_Rate', 'SheltDay_Rate','Dis_Per', 'PrevHos'], 
'Dem_Score':['Over85_Per', 'Over65_Per', 'Under18_Per', 'Under5_Per', 'NonWhi_Per', 'Lat_Per', 'Black_Per', 'Asian_Per', 'Pov_Per', 'PopDens', 'DayPopDens'], 
'Res_Score':['Haz_Score', 'Env_Score', 'Trans_Sco', 'Com_Score', 'PR_Score',
            'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score']}

for s in score_dict:
    for i in jo['features']:
        if i['properties']['name'] in df.Neighborhood.tolist():
            i['properties'][s] = str(int(df.loc[df['Neighborhood'] == i['properties']['name']][s]))

    if i['properties']['name'] == 'Glen Park':
        i['properties'][s] = str(int(0))

with open('../Data/san-francisco_scores.json', 'w') as f:
    json.dump(jo, f)