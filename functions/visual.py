import flask
import dash
import plotly

import dash_html_components as html
import plotly.graph_objs as go
from flask import Flask, render_template #this has changed

import pandas as pd
import numpy as np
import json

def create_plot():
    years = [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
         2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012]

    data = go.Figure()
    
    data.add_trace(go.Bar(x=years,
                y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263, 350, 430, 474, 526, 488, 537, 500, 439],
                name='Linio',
                marker_color='rgb(55, 83, 109)'
                ))

    data.add_trace(go.Bar(x=years,
                y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                   299, 340, 403, 549, 499],
                name='Claroshop',
                marker_color='rgb(26, 118, 255)'
                ))
    data.update_layout(
    	title='Categorías relevantes de claroshop',
    	xaxis_tickfont_size=14,
    	yaxis=dict( title='USD (millions)', titlefont_size=16, tickfont_size=14,), legend=dict( x=0, y=1.0, bgcolor='rgba(255, 255, 255, 0)', bordercolor='rgba(255, 255, 255, 0)'), barmode='group',
    	bargap=0.15, # gap between bars of adjacent location coordinates.
    	bargroupgap=0.1 # gap between bars of the same location coordinate.
	)

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON