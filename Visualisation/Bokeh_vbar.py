# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:15:10 2018

NOTE : in this version, only the text widget is functionnal,
when using the slider nothing happens (yet)

@author: Michael DARQUES
Use the ``bokeh serve`` command to run the example by executing:
    bokeh serve filename.py
at your anaconda prompt. Then navigate to the URL
    http://localhost:5006/
in your browser.
"""

import glob
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.plotting import figure, output_file, show, Figure, save
from bokeh.models import LinearAxis, Range1d, ColumnDataSource
from bokeh.models.widgets import Slider, TextInput

### DEFS


def update_title(attrname, old, new):


''' Update figure title when text box changes'''
    plot.title.text = text.value


def update_data(attrname, old, new):
    ''' Update graph using a slider '''
    # Get the current slider values
    q = quantile.value
    # Generate the new curve
    X = np.array(range(len(sample_data[q].Index)))+0.35
    Y = sample_data[q].Index_reported_Rate
    source.data = dict(x=X, y=Y)


path = 'C:/Users/...'
file = 'tab.csv'
file_to_open = path+file
data = pd.read_csv(file_to_open)
cols = data.columns
factors = data["FACTORS"].unique()

## SELECT PARAMETERS
#quant = 0
selected_A = '12-34-56'
selected_damage = "damage"
selected_factor = "Factor"

# Open all files and store in a single array
all_files = glob.glob('C:/Users/.../*.csv')
data = []
for f in all_files:
    data.append(pd.read_csv(f))

# Data for only one A, one factor and one damagetype
sample_data = []
for i in range(len(data)):
    _ = data[i].loc[(data[i].A == selected_A)
                            & (data[i].Damage == selected_damage)
                            & (data[i].FACTORS == selected_factor)]
    sample_data.append(_)
    
### DEFINE WIDGETS
text = TextInput(title="title", value='Enter text')
quantile = Slider(start=0, end=5, value=1, step=1, title="quantile")

### COORDINATES 
X = np.array(range(len(sample_data[quantile.value].Index)))+0.35
X2 = X+0.3
Y = sample_data[quantile.value].Index_reported_Rate
Y2 = sample_data[quantile.value].Index_nb_years_flown

source = ColumnDataSource(data=dict(x=X, y=Y))

# Definition of the figure
plot = figure(plot_width=500,
              plot_height=500,
              x_axis_label=selected_factor,
              x_range=sample_data[quantile.value].Index.values,
              title="Titre"
              )
# Firt bar plot (TRM rate)
plot.vbar(x=X,
          width=0.25,
          bottom=0,
          top=Y,
          color='red'
          )
  
plot.extra_y_ranges = {"Range1": Range1d(start=0, end=1)}
plot.vbar(x=X2,
          width=0.25,
          bottom=0,
          top=Y2,
          color='blue')
# Set up callbacks
text.on_change('value', update_title)
quantile.on_change('value', update_data)

### Set up layouts and add to document
inputs = widgetbox(text, quantile)  # insert here the list of controls/widgets
curdoc().add_root(row(inputs, plot, width=500))
curdoc().title = "Sliders"
