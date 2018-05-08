import pandas as pd
import numpy as np
import math

from bokeh.plotting import figure, show, output_file, save
from bokeh.models import ColumnDataSource, LabelSet, GeoJSONDataSource, HoverTool, LinearColorMapper, ColumnDataSource, Circle
from bokeh.io import show, output_notebook, output_file
from bokeh.palettes import Viridis11
from bokeh.models.widgets import Panel, Tabs

df = pd.read_csv('../Data/Community_Resiliency_Indicator_System.csv')
df = df[['Neighborhood', 'Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score',
     'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']].dropna()

vect1 = [np.cos(np.deg2rad(36*i)) for i in range(1, 11)]
vect2 = [np.sin(np.deg2rad(36*i)) for i in range(1, 11)]
scores = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
x = np.array(scores) * np.array(vect1)
y = np.array(scores) * np.array(vect2)

def radar_patch(scores, vect1, vect2):
    xt = np.array(scores) * np.array(vect1)
    yt = np.array(scores) * np.array(vect2)
    return xt, yt

p1 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p1.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p1.add_layout(labels)
f = np.array([1.0, 1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p1.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab1 = Panel(child=p1, title="Bayview")

p2 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p2.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p2.add_layout(labels)
f = np.array([3.0, 2.0, 3.0, 4.0, 3.0, 5.0, 3.0, 3.0, 3.0, 3.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p2.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab2 = Panel(child=p2, title="Bernal Heights")

p3 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p3.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p3.add_layout(labels)
f = np.array([5.0, 4.0, 4.0, 5.0, 5.0, 3.0, 4.0, 4.0, 5.0, 5.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p3.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab3 = Panel(child=p3, title="Castro/Upper Market")

p4 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p4.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p4.add_layout(labels)
f = np.array([1.0, 1.0, 5.0, 1.0, 3.0, 1.0, 1.0, 1.0, 1.0, 1.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p4.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab4 = Panel(child=p4, title="Chinatown")

p5 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p5.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p5.add_layout(labels)
f = np.array([3.0, 3.0, 1.0, 2.0, 1.0, 4.0, 1.0, 1.0, 1.0, 1.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p5.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab5 = Panel(child=p5, title="Crocker Amazon")

p6 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p6.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p6.add_layout(labels)
f = np.array([4.0, 5.0, 2.0, 5.0, 3.0, 4.0, 4.0, 4.0, 4.0, 5.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p6.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab6 = Panel(child=p6, title="Diamond Heights/Glen Park")

p7 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p7.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p7.add_layout(labels)
f = np.array([1.0, 1.0, 5.0, 1.0, 5.0, 1.0, 1.0, 1.0, 2.0, 1.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p7.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab7 = Panel(child=p7, title="Downtown/Civic Center")

p8 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p8.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p8.add_layout(labels)
f = np.array([3.0, 3.0, 2.0, 2.0, 1.0, 5.0, 2.0, 2.0, 1.0, 2.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p8.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab8 = Panel(child=p8, title="Excelsior")

p9 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p9.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p9.add_layout(labels)
f = np.array([1.0, 1.0, 5.0, 1.0, 5.0, 1.0, 2.0, 2.0, 1.0, 1.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p9.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab9 = Panel(child=p9, title="Financial District")

p10 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p10.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p10.add_layout(labels)
f = np.array([4.0, 4.0, 4.0, 5.0, 5.0, 3.0, 4.0, 4.0, 5.0, 5.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p10.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab10 = Panel(child=p10, title="Haight Ashbury")

p11 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p11.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p11.add_layout(labels)
f = np.array([5.0, 3.0, 3.0, 3.0, 4.0, 3.0, 3.0, 3.0, 4.0, 4.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p11.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab11 = Panel(child=p11, title="Inner Richmond")

p12 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p12.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p12.add_layout(labels)
f = np.array([5.0, 5.0, 2.0, 4.0, 3.0, 4.0, 5.0, 5.0, 4.0, 4.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p12.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab12 = Panel(child=p12, title="Inner Sunset")

p13 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p13.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p13.add_layout(labels)
f = np.array([4.0, 5.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 3.0, 2.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p13.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab13 = Panel(child=p13, title="Lakeshore")

p14 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p14.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p14.add_layout(labels)
f = np.array([2.0, 2.0, 4.0, 5.0, 4.0, 3.0, 3.0, 3.0, 5.0, 4.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p14.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab14 = Panel(child=p14, title="Marina")

p15 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p15.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p15.add_layout(labels)
f = np.array([2.0, 2.0, 4.0, 2.0, 4.0, 2.0, 3.0, 3.0, 3.0, 2.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p15.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab15 = Panel(child=p15, title="Mission")

p16 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p16.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p16.add_layout(labels)
f = np.array([1.0, 1.0, 4.0, 1.0, 3.0, 5.0, 5.0, 5.0, 4.0, 3.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p16.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab16 = Panel(child=p16, title="Mission Bay")

p17 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p17.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p17.add_layout(labels)
f = np.array([2.0, 2.0, 5.0, 3.0, 5.0, 1.0, 4.0, 4.0, 4.0, 3.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p17.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab17 = Panel(child=p17, title="Nob Hill")

p18 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p18.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p18.add_layout(labels)
f = np.array([5.0, 4.0, 3.0, 5.0, 4.0, 3.0, 5.0, 5.0, 5.0, 5.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p18.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab18 = Panel(child=p18, title="Noe Valley")

p19 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p19.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p19.add_layout(labels)
f = np.array([1.0, 3.0, 5.0, 2.0, 4.0, 1.0, 3.0, 3.0, 2.0, 2.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p19.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab19 = Panel(child=p19, title="North Beach")

p20 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p20.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p20.add_layout(labels)
f = np.array([4.0, 3.0, 1.0, 2.0, 1.0, 4.0, 1.0, 1.0, 2.0, 2.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p20.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab20 = Panel(child=p20, title="Ocean View")

p21 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p21.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p21.add_layout(labels)
f = np.array([2.0, 2.0, 2.0, 3.0, 2.0, 4.0, 4.0, 4.0, 1.0, 2.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p21.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab21 = Panel(child=p21, title="Outer Mission")

p22 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p22.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p22.add_layout(labels)
f = np.array([5.0, 3.0, 3.0, 3.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p22.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab22 = Panel(child=p22, title="Outer Richmond")

p23 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p23.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p23.add_layout(labels)
f = np.array([5.0, 4.0, 1.0, 3.0, 2.0, 5.0, 3.0, 3.0, 2.0, 3.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p23.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab23 = Panel(child=p23, title="Outer Sunset")

p24 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p24.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p24.add_layout(labels)
f = np.array([3.0, 4.0, 4.0, 4.0, 4.0, 2.0, 5.0, 5.0, 5.0, 5.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p24.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab24 = Panel(child=p24, title="Pacific Heights")

p25 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p25.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p25.add_layout(labels)
f = np.array([5.0, 4.0, 1.0, 4.0, 2.0, 5.0, 1.0, 1.0, 2.0, 3.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p25.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab25 = Panel(child=p25, title="Parkside")

p26 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p26.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p26.add_layout(labels)
f = np.array([2.0, 2.0, 3.0, 4.0, 2.0, 5.0, 2.0, 2.0, 5.0, 4.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p26.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab26 = Panel(child=p26, title="Potrero Hill")

p27 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p27.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p27.add_layout(labels)
f = np.array([4.0, 5.0, 3.0, 3.0, 2.0, 5.0, 5.0, 5.0, 5.0, 5.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p27.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab27 = Panel(child=p27, title="Presidio")

p28 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p28.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p28.add_layout(labels)
f = np.array([4.0, 4.0, 4.0, 5.0, 5.0, 2.0, 2.0, 2.0, 4.0, 4.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p28.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab28 = Panel(child=p28, title="Presidio Heights")

p29 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p29.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p29.add_layout(labels)
f = np.array([3.0, 3.0, 5.0, 4.0, 5.0, 1.0, 5.0, 5.0, 5.0, 4.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p29.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab29 = Panel(child=p29, title="Russian Hill")

p30 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p30.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p30.add_layout(labels)
f = np.array([3.0, 5.0, 2.0, 4.0, 2.0, 3.0, 5.0, 5.0, 2.0, 5.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p30.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab30 = Panel(child=p30, title="Seacliff")

p31 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p31.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p31.add_layout(labels)
f = np.array([1.0, 1.0, 5.0, 1.0, 4.0, 2.0, 4.0, 4.0, 3.0, 2.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p31.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab31 = Panel(child=p31, title="South of Market")

p32 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p32.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p32.add_layout(labels)
f = np.array([2.0, 1.0, 3.0, 1.0, 1.0, 4.0, 2.0, 2.0, 2.0, 1.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p32.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab32 = Panel(child=p32, title="Treasure Island/YBI")

p33 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p33.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p33.add_layout(labels)
f = np.array([4.0, 5.0, 2.0, 5.0, 3.0, 2.0, 2.0, 2.0, 4.0, 4.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p33.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab33 = Panel(child=p33, title="Twin Peaks")

p34 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p34.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p34.add_layout(labels)
f = np.array([3.0, 5.0, 1.0, 1.0, 1.0, 4.0, 1.0, 1.0, 1.0, 1.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p34.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab34 = Panel(child=p34, title="Visitacion Valley")

p35 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p35.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p35.add_layout(labels)
f = np.array([5.0, 5.0, 2.0, 5.0, 3.0, 5.0, 4.0, 4.0, 3.0, 5.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p35.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab35 = Panel(child=p35, title="West of Twin Peaks")

p36 = figure(title="Radar plot")
text = ['Haz_Score', 'Env_Score', 'Trans_Score', 'Com_Score', 'PR_Score', 'House_Score', 'Ec_Score', 'Health_Score', 'Dem_Score', 'Res_Score']
source = ColumnDataSource({'x':x, 'y':y, 'text':text})
p36.line(x="x", y="y", source=source)
labels = LabelSet(x="x",y="y",text="text",source=source)
p36.add_layout(labels)
f = np.array([2.0, 2.0, 5.0, 3.0, 5.0, 1.0, 5.0, 5.0, 3.0, 3.0])
flist = [f]
colors = ['blue']
for i in range(len(flist)):
    xt, yt = radar_patch(flist[i], vect1, vect2)
    p36.patch(x=xt, y=yt, fill_alpha=0.15, fill_color=colors[i])
tab36 = Panel(child=p36, title="Western Addition")

output_file("../Updated Website/radar.html")

tabs = Tabs(tabs=[tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10,
                 tab11, tab12, tab13, tab14, tab15, tab16, tab17, tab18, tab19, tab20,
                 tab21, tab22, tab23, tab24, tab25, tab26, tab27, tab28, tab29, tab30,
                 tab31, tab32, tab33, tab34, tab35, tab36])

save(tabs)