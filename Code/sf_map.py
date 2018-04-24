import pandas as pd
import json

from bokeh.io import show, output_notebook, output_file
from bokeh.models import GeoJSONDataSource, HoverTool, LinearColorMapper, ColumnDataSource, Circle
from bokeh.plotting import figure, output_file, save
from bokeh.palettes import Viridis11


score_dict = {'Haz_Score':['Flood_Per', 'Heat_Per', 'Liq_Per'], 
'Env_Score':['Imp_Per', 'Tree_Per', 'PM_Conc', 'Tox_Per'], 
'Trans_Sco':['AT_Min', 'PTrans_Sco'], 
'Com_Score':['VCrim_Rate', 'Vot_Rate', 'NewSF_Per', 'Citz_Per', 'Eng_Per'], 
'PR_Score':['Food_Score', 'HS_Per', 'Pharm_Per'],
'House_Score':['LivAl_Per', 'EldLivAl_Per', 'OC_Per', 'Viol_Rate', 'AC_Per', 'Rent_Per'], 
'Ec_Score':['Emp_per'], 
'Health_Score':['Shelt_Rate', 'SheltDay_Rate','Dis_Per', 'PrevHos'], 
'Dem_Score':['Over85_Per', 'Over65_Per', 'Under18_Per', 'Under5_Per', 'NonWhi_Per', 'Lat_Per', 'Black_Per', 'Asian_Per', 'Pov_Per', 'PopDens', 'DayPopDens'], 
'Res_Score':['Haz_Score', 'Env_Score', 'Trans_Sco', 'Com_Score', 'PR_Score',
            'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score']}

for s in score_dict:
    with open('../Data/san-francisco_scores.json', 'r') as f:
        jo = json.loads(f.read())
    
    geo_source = GeoJSONDataSource(geojson=json.dumps(jo))
    TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
    color_mapper = LinearColorMapper(palette='Blues9', low=5, high=0)
    p = figure(title='%s Choropleth Map'%s, tools=TOOLS, x_axis_location=None, y_axis_location=None,
          width=1000, height=600)
    p.grid.grid_line_color = None
    p.patches('xs', 'ys', fill_alpha=0.7, fill_color={'field':s, 'transform':color_mapper},
         line_color='white', line_width=0.5, source=geo_source)
    hover = p.select_one(HoverTool)
    hover.point_policy = "follow_mouse"
    hover.tooltips = [("Name:", "@name"), ("%s:"%s, "@%s"%s)]
    
    output_file("../Updated Website/%s.html" %s)
    save(p)
