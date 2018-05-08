import pandas as pd
import json

from bokeh.io import show, output_notebook, output_file
from bokeh.models import GeoJSONDataSource, HoverTool, LinearColorMapper, ColumnDataSource, Circle
from bokeh.plotting import figure, output_file, save
from bokeh.palettes import Viridis11
from bokeh.models.widgets import Panel, Tabs

output_file("../Updated Website/map.html")

with open('../Data/san-francisco_scores.json', 'r') as f:
    jo = json.loads(f.read())

geo_source = GeoJSONDataSource(geojson=json.dumps(jo))
TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
color_mapper = LinearColorMapper(palette='Blues9', low=5, high=0)
p1 = figure(title='%s Choropleth Map'%'Haz_Score', tools=TOOLS, x_axis_location=None, y_axis_location=None, width=1000, height=600)
p1.grid.grid_line_color = None
p1.patches('xs', 'ys', fill_alpha=0.7, fill_color={'field':'Haz_Score', 'transform':color_mapper}, line_color='white', line_width=0.5, source=geo_source)
hover = p1.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [("Name:", "@name"), ("%s:"%'Haz_Score', "@%s"%'Haz_Score')]
tab1 = Panel(child=p1, title="Haz_Score")

geo_source = GeoJSONDataSource(geojson=json.dumps(jo))
TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
color_mapper = LinearColorMapper(palette='Blues9', low=5, high=0)
p2 = figure(title='%s Choropleth Map'%'Env_Score', tools=TOOLS, x_axis_location=None, y_axis_location=None, width=1000, height=600)
p2.grid.grid_line_color = None
p2.patches('xs', 'ys', fill_alpha=0.7, fill_color={'field':'Env_Score', 'transform':color_mapper}, line_color='white', line_width=0.5, source=geo_source)
hover = p2.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [("Name:", "@name"), ("%s:"%'Env_Score', "@%s"%'Env_Score')]
tab2 = Panel(child=p2, title="Env_Score")

geo_source = GeoJSONDataSource(geojson=json.dumps(jo))
TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
color_mapper = LinearColorMapper(palette='Blues9', low=5, high=0)
p3 = figure(title='%s Choropleth Map'%'Trans_Score', tools=TOOLS, x_axis_location=None, y_axis_location=None, width=1000, height=600)
p3.grid.grid_line_color = None
p3.patches('xs', 'ys', fill_alpha=0.7, fill_color={'field':'Trans_Score', 'transform':color_mapper}, line_color='white', line_width=0.5, source=geo_source)
hover = p3.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [("Name:", "@name"), ("%s:"%'Trans_Score', "@%s"%'Trans_Score')]
tab3 = Panel(child=p3, title="Trans_Score")

geo_source = GeoJSONDataSource(geojson=json.dumps(jo))
TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
color_mapper = LinearColorMapper(palette='Blues9', low=5, high=0)
p4 = figure(title='%s Choropleth Map'%'Com_Score', tools=TOOLS, x_axis_location=None, y_axis_location=None, width=1000, height=600)
p4.grid.grid_line_color = None
p4.patches('xs', 'ys', fill_alpha=0.7, fill_color={'field':'Com_Score', 'transform':color_mapper}, line_color='white', line_width=0.5, source=geo_source)
hover = p4.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [("Name:", "@name"), ("%s:"%'Com_Score', "@%s"%'Com_Score')]
tab4 = Panel(child=p4, title="Com_Score")

geo_source = GeoJSONDataSource(geojson=json.dumps(jo))
TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
color_mapper = LinearColorMapper(palette='Blues9', low=5, high=0)
p5 = figure(title='%s Choropleth Map'%'PR_Score', tools=TOOLS, x_axis_location=None, y_axis_location=None, width=1000, height=600)
p5.grid.grid_line_color = None
p5.patches('xs', 'ys', fill_alpha=0.7, fill_color={'field':'PR_Score', 'transform':color_mapper}, line_color='white', line_width=0.5, source=geo_source)
hover = p5.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [("Name:", "@name"), ("%s:"%'PR_Score', "@%s"%'PR_Score')]
tab5 = Panel(child=p5, title="PR_Score")

geo_source = GeoJSONDataSource(geojson=json.dumps(jo))
TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
color_mapper = LinearColorMapper(palette='Blues9', low=5, high=0)
p6 = figure(title='%s Choropleth Map'%'House_Score', tools=TOOLS, x_axis_location=None, y_axis_location=None, width=1000, height=600)
p6.grid.grid_line_color = None
p6.patches('xs', 'ys', fill_alpha=0.7, fill_color={'field':'House_Score', 'transform':color_mapper}, line_color='white', line_width=0.5, source=geo_source)
hover = p6.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [("Name:", "@name"), ("%s:"%'House_Score', "@%s"%'House_Score')]
tab6 = Panel(child=p6, title="House_Score")


geo_source = GeoJSONDataSource(geojson=json.dumps(jo))
TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
color_mapper = LinearColorMapper(palette='Blues9', low=5, high=0)
p7 = figure(title='%s Choropleth Map'%'Ec_Score', tools=TOOLS, x_axis_location=None, y_axis_location=None, width=1000, height=600)
p7.grid.grid_line_color = None
p7.patches('xs', 'ys', fill_alpha=0.7, fill_color={'field':'Ec_Score', 'transform':color_mapper}, line_color='white', line_width=0.5, source=geo_source)
hover = p7.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [("Name:", "@name"), ("%s:"%'Ec_Score', "@%s"%'Ec_Score')]
tab7 = Panel(child=p7, title="Ec_Score")

geo_source = GeoJSONDataSource(geojson=json.dumps(jo))
TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
color_mapper = LinearColorMapper(palette='Blues9', low=5, high=0)
p8 = figure(title='%s Choropleth Map'%'Dem_Score', tools=TOOLS, x_axis_location=None, y_axis_location=None, width=1000, height=600)
p8.grid.grid_line_color = None
p8.patches('xs', 'ys', fill_alpha=0.7, fill_color={'field':'Dem_Score', 'transform':color_mapper}, line_color='white', line_width=0.5, source=geo_source)
hover = p8.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [("Name:", "@name"), ("%s:"%'Dem_Score', "@%s"%'Dem_Score')]
tab8 = Panel(child=p8, title="Dem_Score")

geo_source = GeoJSONDataSource(geojson=json.dumps(jo))
TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
color_mapper = LinearColorMapper(palette='Blues9', low=5, high=0)
p9 = figure(title='%s Choropleth Map'%'Res_Score', tools=TOOLS, x_axis_location=None, y_axis_location=None, width=1000, height=600)
p9.grid.grid_line_color = None
p9.patches('xs', 'ys', fill_alpha=0.7, fill_color={'field':'Res_Score', 'transform':color_mapper}, line_color='white', line_width=0.5, source=geo_source)
hover = p9.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [("Name:", "@name"), ("%s:"%'Res_Score', "@%s"%'Res_Score')]
tab9 = Panel(child=p9, title="Res_Score")

geo_source = GeoJSONDataSource(geojson=json.dumps(jo))
TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
color_mapper = LinearColorMapper(palette='Blues9', low=5, high=0)
p10 = figure(title='%s Choropleth Map'%'Health_Score', tools=TOOLS, x_axis_location=None, y_axis_location=None, width=1000, height=600)
p10.grid.grid_line_color = None
p10.patches('xs', 'ys', fill_alpha=0.7, fill_color={'field':'Health_Score', 'transform':color_mapper}, line_color='white', line_width=0.5, source=geo_source)
hover = p10.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [("Name:", "@name"), ("%s:"%'Health_Score', "@%s"%'Health_Score')]
tab10 = Panel(child=p10, title="Health_Score")

tabs = Tabs(tabs=[tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10])

save(tabs)