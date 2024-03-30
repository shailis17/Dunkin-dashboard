import dash
from dash import dcc, html, Input, Output

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


bak_url='https://drive.google.com/file/d/1YROIywlL7KOPenUgmMLYbt1acZ2zP5su/view?usp=sharing'
bak_path = 'https://drive.google.com/uc?export=download&id='+bak_url.split('/')[-2]
bakery_df = pd.read_csv(bak_path)
drinks_url='https://drive.google.com/file/d/1Os-fZ6eV6Ky0XjiqwnAtY2zQAFEIFPFA/view?usp=sharing'
drinks_path = 'https://drive.google.com/uc?export=download&id='+drinks_url.split('/')[-2]
drinks_df = pd.read_csv(drinks_path)

drink_cats = drinks_df['Category'].unique()
drinks_df.fillna('None', inplace=True)
default_cat = drink_cats[0] if len(drink_cats) == 1 else None


app = dash.Dash(__name__, external_stylesheets=['https://fonts.googleapis.com/css?family=Fredoka+One', 'https://fonts.googleapis.com/css?family=Fredoka','https://fonts.googleapis.com/css?family=Lato'])

app.layout = html.Div([
    # Header Div
    html.Div(
        [
            html.Div(
                html.Img(src='/assets/dunkin-logo.png', className='header logo'),
            ),
            html.Div(
                [
                html.H1("Nutritional Values"),  # First line of text
                html.H2("Donuts, Drinks, and other menu items - including your customized drink orders"),  # Second line of text
                html.H3("Get information about Calories, Calories from Fat, Total Fat, Saturated Fat, Trans Fat, Cholesterol, Sodium, Carbs, Fiber, Sugars, Protein, and Weight Watchers Points")  # Third line of text
                ],
                className='title-desc'
            )
        ],
        className="header"
    ),

    html.Div([
        html.H2(
            "Dairy/Sweetener Changer",
            className="box"
        ),
        html.H2(
            "Flavor Changer",
            className="box"
        ),
    ], className='box-holder'),

    html.Div([
        html.Div(
            [
                html.Div(
                [
                    html.Div([
                        html.Label('Nutrition Category'),  # Label for Category Dropdown
                        dcc.Dropdown(
                            id='ds_nutrition', className='dropdown2',
                            options=['Calories', 'Total Fat (g)',' Saturated Fat (g)', 'Cholesterol (mg)', 'Sodium (mg)', 'Carbs (g)', 'Fiber (g)', 'Sugars (g)', 'Protein (g)', 'Weight Watcher Pnts'],
                        ),
                    ], className='dropdown-container'),  # Container for Category Dropdown

                    html.Div([
                        html.Label('Drink Type'),  # Label for Category Dropdown
                        dcc.Dropdown(
                            id='ds_category', className='dropdown2',
                            options=[{'label': cat, 'value': cat} for cat in drink_cats],
                            value=default_cat
                        ),
                    ], className='dropdown-container'),  # Container for Flavor Dropdown
                    html.Div([
                        html.Label('Flavor'),  # Label for Flavor Dropdown
                        dcc.Dropdown(id='ds_flavor', className='dropdown2'),
                    ], className='dropdown-container'),  # Container for Flavor Dropdown
                ], className='drink_item'),
                html.Div(dcc.Checklist(id='ds_size', options=['Small', 'Medium', 'Large'], value=['Small', 'Medium', 'Large'], inline=True), className='sizes_holder'),
                html.Br(),
                html.Div(dcc.Graph(id='ds-changer'))
            ],
            className="box box1"
        ),
        html.Div(
            [
                html.Div(
                [
                    html.Div([
                        html.Label('Nutrition Category'),  # Label for Category Dropdown
                        dcc.Dropdown(
                            id='f_nutrition', className='dropdown2',
                            options=['Calories', 'Total Fat (g)',' Saturated Fat (g)', 'Cholesterol (mg)', 'Sodium (mg)', 'Carbs (g)', 'Fiber (g)', 'Sugars (g)', 'Protein (g)', 'Weight Watcher Pnts'],
                        ),
                    ], className='dropdown-container'),  # Container for Category Dropdown

                    html.Div([
                        html.Label('Drink Type'),  # Label for Category Dropdown
                        dcc.Dropdown(
                            id='f_category', className='dropdown2',
                            options=[{'label': cat, 'value': cat} for cat in drink_cats],
                            value=default_cat
                        ),
                    ], className='dropdown-container'),  # Container for Flavor Dropdown

                    html.Div([
                        html.Label('Dairy'),  # Label for Dairy Dropdown
                        dcc.Dropdown(id='f_dairy', className='dropdown2'),
                    ], className='dropdown-container'),  # Container for Dairy Dropdown

                    html.Div([
                        html.Label('Sweetener'),  # Label for Sweetener Dropdown
                        dcc.Dropdown(id='f_sweetener', className='dropdown2'),
                    ], className='dropdown-container'),  # Container for Sweetener Dropdown
                ], className='drink_item'),
                html.Div(dcc.Checklist(id='f_size', options=['Small', 'Medium', 'Large'], value=['Small', 'Medium', 'Large'], inline=True), className='sizes_holder'),
                html.Br(),
                html.Div(dcc.Graph(id='flavor-changer'))
            ],
            className="box box2"
        ),
    ], className='box-holder'),

    html.H2(
            "Compare Two Custom Drinks",
            className='subtitle'
        ),
    # Custom Drink Comparer
    html.Div(
    [
        html.Div([
            html.Div(
                [
                    html.Div(html.Div([html.Div(className='color_rectangle purple'), html.H3('Drink #1')], className='item_label'), className='drink_item_labels_holder' ),
                    html.Div([
                        html.Div(
                            [
                                html.Div([
                                    html.Label('Drink Type'),  # Label for Category Dropdown
                                    dcc.Dropdown(
                                        id='d1_category', className='dropdown2',
                                        options=[{'label': cat, 'value': cat} for cat in drink_cats],
                                        value=default_cat
                                    ),
                                ], className='dropdown-container'),  # Container for Category Dropdown

                                html.Div([
                                    html.Label('Flavor'),  # Label for Flavor Dropdown
                                    dcc.Dropdown(id='d1_flavor', className='dropdown2'),
                                ], className='dropdown-container'),  # Container for Flavor Dropdown

                                html.Div([
                                    html.Label('Dairy'),  # Label for Dairy Dropdown
                                    dcc.Dropdown(id='d1_dairy', className='dropdown2'),
                                ], className='dropdown-container'),  # Container for Dairy Dropdown

                                html.Div([
                                    html.Label('Sweetener'),  # Label for Sweetener Dropdown
                                    dcc.Dropdown(id='d1_sweetener', className='dropdown2'),
                                ], className='dropdown-container'),  # Container for Sweetener Dropdown

                            ], className='drink_item'),  # Container for Drink #1 Dropdowns
                    ]),
                    html.Div(dcc.RadioItems(id='drink1_size', options=['Small', 'Medium', 'Large'], value='Small', inline=True), className='sizes_holder'),
                ], className="box box1"
            ),
            html.Div(
                [
                    html.Div(html.Div([html.Div(className='color_rectangle pink'), html.H3('Drink #2')], className='item_label'), className='drink_item_labels_holder' ),
                    html.Div([
                        html.Div(
                            [
                                html.Div([
                                    html.Label('Drink Type'),  # Label for Category Dropdown
                                    dcc.Dropdown(
                                        id='d2_category', className='dropdown2',
                                        options=[{'label': cat, 'value': cat} for cat in drink_cats],
                                        value=default_cat
                                    ),
                                ], className='dropdown-container'),  # Container for Category Dropdown

                                html.Div([
                                    html.Label('Flavor'),  # Label for Flavor Dropdown
                                    dcc.Dropdown(id='d2_flavor', className='dropdown2'),
                                ], className='dropdown-container'),  # Container for Flavor Dropdown

                                html.Div([
                                    html.Label('Dairy'),  # Label for Dairy Dropdown
                                    dcc.Dropdown(id='d2_dairy', className='dropdown2'),
                                ], className='dropdown-container'),  # Container for Dairy Dropdown

                                html.Div([
                                    html.Label('Sweetener'),  # Label for Sweetener Dropdown
                                    dcc.Dropdown(id='d2_sweetener', className='dropdown2'),
                                ], className='dropdown-container'),  # Container for Sweetener Dropdown

                            ], className='drink_item'),  # Container for Drink #1 Dropdowns
                    ]),
                    html.Div(dcc.RadioItems(id='drink2_size', options=['Small', 'Medium', 'Large'], value='Small', inline=True), className='sizes_holder'),
                ], className="box box1"
            ),
        ], className='box-holder'),

        html.Br(),
        html.Div([dcc.Graph(id='drinks_cal-ww'), dcc.Graph(id='drinks_grams'), dcc.Graph(id='drinks_mg')], className='full-span-graphs'),

    ], className="full-span"
    ),

    #two bakery comparison
    html.H2("Compare Two Bakery Items", className='subtitle'),
    html.Div(
        [
            html.Div(
                [
                    html.Div([
                        html.Div(html.Div([html.Div(className='color_rectangle red'), html.H3('Item #1')], className='item_label'), className='drink_item_labels_holder'),
                        html.Div(
                        [
                            html.Div([
                            dcc.Dropdown(
                            id='item1_cat', className='dropdown',
                            options=[{'label': category, 'value': category} for category in bakery_df['Category'].unique()],
                            value=bakery_df['Category'].iloc[0],  # Default value
                            placeholder='Select a category'
                            ),
                        
                            dcc.Dropdown(id='item1', className='dropdown', placeholder='Select an item'),
                            ], 
                            className='bak_item_holder'),
                        ]),
                    ], className='label1'),
                    html.Div([
                        html.Div(html.Div([html.Div(className='color_rectangle orange'), html.H3('Item #2')], className='item_label'), className='drink_item_labels_holder'),
                        html.Div(
                            [
                                html.Div([
                                    dcc.Dropdown(
                                    id='item2_cat', className='dropdown',
                                    options=[{'label': category, 'value': category} for category in bakery_df['Category'].unique()],
                                    value=bakery_df['Category'].iloc[0],  # Default value
                                    placeholder='Select a category'
                                    ),
                                
                                    dcc.Dropdown(id='item2', className='dropdown', placeholder='Select an item'),
                                    ], 
                                className='bak_item_holder'),
                            ]
                        ),
                    ], className='label2')
                ], className='label_holder'
            ),

            html.Br(),
            html.Div([dcc.Graph(id='bakery_cal-ww'), dcc.Graph(id='bakery_grams'), dcc.Graph(id='bakery_mg')], className='full-span-graphs'),

        ], className="full-span"
    ),
])

# Define callback functions to update ds-changer dropdown options dynamically
@app.callback(Output('ds_flavor', 'options'), Input('ds_category', 'value'))
def update_flavor_options(selected_category):
    filtered_df = drinks_df[drinks_df['Category'] == selected_category]
    flavor_options = filtered_df['Flavor'].unique()
    return [{'label': flavor, 'value': flavor} for flavor in flavor_options]

#update ds-changer graph
@app.callback(Output('ds-changer', 'figure'), 
              [Input('ds_nutrition', 'value'), Input('ds_category', 'value'), Input('ds_flavor', 'value'), Input('ds_size', 'value')])
def update_graph(nutrition_category, drink_type, flavor, sizes):
    # Filter the drinks_df based on selected values
    filtered_df = drinks_df[
        (drinks_df['Category'] == drink_type) &
        (drinks_df['Flavor'] == flavor) &
        (drinks_df['Size'].isin(sizes))
    ]

    filtered_df['Dairy_Sweetener'] = filtered_df['Dairy'] + ' + ' + filtered_df['Sweetener']

    colors = {'Small': '#EA4598', 'Medium': '#874710', 'Large': '#F58425'}

    fig = px.bar(filtered_df, x='Dairy_Sweetener', y=nutrition_category, labels={'Dairy_Sweetener': 'Dairy + Sweetener', 'value': nutrition_category}, 
                 barmode='group', color='Size', color_discrete_map=colors)
    
    return fig


#Define callback functions to update flavor changer dropdowns
@app.callback(Output('f_dairy', 'options'), [Input('f_category', 'value')])
def update_dairy_options_f(selected_category):
    filtered_df = drinks_df[(drinks_df['Category'] == selected_category)]
    dairy_options = filtered_df['Dairy'].unique()
    return [{'label': d, 'value': d} for d in dairy_options]

@app.callback(Output('f_sweetener', 'options'), [Input('f_category', 'value'), Input('f_dairy', 'value')])
def update_sweetener_options_f(selected_category, selected_dairy):
    filtered_df = drinks_df[(drinks_df['Category'] == selected_category) & (drinks_df['Dairy'] == selected_dairy)]
    sweetener_options = filtered_df['Sweetener'].unique()
    return [{'label': s, 'value': s} for s in sweetener_options]

@app.callback(Output('flavor-changer', 'figure'), 
              [Input('f_nutrition', 'value'), Input('f_category', 'value'), Input('f_dairy', 'value'), 
               Input('f_sweetener', 'value'), Input('f_size', 'value')])
def update_graph(nutrition_category, drink_type, dairy, sweetener, sizes):
    # Filter the drinks_df based on selected values
    filtered_df = drinks_df[
        (drinks_df['Category'] == drink_type) &
        (drinks_df['Dairy'] == dairy) &
        (drinks_df['Sweetener'] == sweetener) &
        (drinks_df['Size'].isin(sizes))
    ]

    colors = {'Small': '#EA4598', 'Medium': '#874710', 'Large': '#F58425'}

    fig = px.bar(filtered_df, x='Flavor', y=nutrition_category, labels={'Flavor': 'Flavor', 'value': nutrition_category}, 
                 barmode='group', color='Size', color_discrete_map=colors)
    return fig

# Define callback functions to update drink1 dropdown options dynamically
@app.callback(Output('d1_flavor', 'options'), Input('d1_category', 'value'))
def update_flavor_options(selected_category):
    filtered_df = drinks_df[drinks_df['Category'] == selected_category]
    flavor_options = filtered_df['Flavor'].unique()
    return [{'label': flavor, 'value': flavor} for flavor in flavor_options]

@app.callback(Output('d1_dairy', 'options'), [Input('d1_category', 'value'), Input('d1_flavor', 'value')])
def update_dairy_options(selected_category, selected_flavor):
    filtered_df = drinks_df[(drinks_df['Category'] == selected_category) & (drinks_df['Flavor'] == selected_flavor)]
    dairy_options = filtered_df['Dairy'].unique()
    return [{'label': d, 'value': d} for d in dairy_options]

@app.callback(Output('d1_sweetener', 'options'), [Input('d1_category', 'value'), Input('d1_flavor', 'value'), Input('d1_dairy', 'value')])
def update_sweetener_options(selected_category, selected_flavor, selected_dairy):
    filtered_df = drinks_df[(drinks_df['Category'] == selected_category) & (drinks_df['Flavor'] == selected_flavor) & (drinks_df['Dairy'] == selected_dairy)]
    sweetener_options = filtered_df['Sweetener'].unique()
    return [{'label': s, 'value': s} for s in sweetener_options]

#drink 2
@app.callback(Output('d2_flavor', 'options'), Input('d2_category', 'value'))
def update_flavor_options(selected_category):
    filtered_df = drinks_df[drinks_df['Category'] == selected_category]
    flavor_options = filtered_df['Flavor'].unique()
    return [{'label': flavor, 'value': flavor} for flavor in flavor_options]

@app.callback(Output('d2_dairy', 'options'), [Input('d2_category', 'value'), Input('d2_flavor', 'value')])
def update_dairy_options(selected_category, selected_flavor):
    filtered_df = drinks_df[(drinks_df['Category'] == selected_category) & (drinks_df['Flavor'] == selected_flavor)]
    dairy_options = filtered_df['Dairy'].unique()
    return [{'label': d, 'value': d} for d in dairy_options]

@app.callback(Output('d2_sweetener', 'options'), [Input('d2_category', 'value'), Input('d2_flavor', 'value'), Input('d2_dairy', 'value')])
def update_sweetener_options(selected_category, selected_flavor, selected_dairy):
    filtered_df = drinks_df[(drinks_df['Category'] == selected_category) & (drinks_df['Flavor'] == selected_flavor) & (drinks_df['Dairy'] == selected_dairy)]
    sweetener_options = filtered_df['Sweetener'].unique()
    return [{'label': s, 'value': s} for s in sweetener_options]

# Define callback to update drink comparison graphs
@app.callback(Output('drinks_cal-ww', 'figure'), 
              [Input('d1_category', 'value'), Input('d1_flavor', 'value'), Input('d1_dairy', 'value'), Input('d1_sweetener', 'value'), 
               Input('d2_category', 'value'), Input('d2_flavor', 'value'), Input('d2_dairy', 'value'), Input('d2_sweetener', 'value'),
               Input('drink1_size', 'value'), Input('drink2_size', 'value')])
def update_drinks_1(cat1, flavor1, dairy1, sweetener1, cat2, flavor2, dairy2, sweetener2, size1, size2):    
    # Filter drinks_df based on the conditions for each combination of category, flavor, dairy, and sweetener
    filtered_df1 = drinks_df[
        (drinks_df['Category'] == cat1) &
        (drinks_df['Flavor'] == flavor1) &
        (drinks_df['Dairy'] == dairy1) &
        (drinks_df['Sweetener'] == sweetener1) &
        (drinks_df['Size'] == size1)
    ]

    filtered_df2 = drinks_df[
        (drinks_df['Category'] == cat2) &
        (drinks_df['Flavor'] == flavor2) &
        (drinks_df['Dairy'] == dairy2) &
        (drinks_df['Sweetener'] == sweetener2) &
        (drinks_df['Size'] == size2)
    ]

    # Define custom colors for each combination of category, flavor, dairy, and sweetener
    colors = {
        '{}_{}_{}_{}_{}'.format(cat1, flavor1, dairy1, sweetener1, size1): '#822F29',
        '{}_{}_{}_{}_{}'.format(cat2, flavor2, dairy2, sweetener2, size2): '#CA3D7D'
    }

    fig = make_subplots(rows=1, cols=2, shared_yaxes=True, subplot_titles=('Calories', 'WW'), horizontal_spacing=0.09)

    fig.add_trace(go.Bar(x=filtered_df1['Category'],  y=filtered_df1['Calories'], name='calories1', 
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat1, flavor1, dairy1, sweetener1, size1)],
                        orientation='v'), row=1, col=1)

    fig.add_trace(go.Bar(x=filtered_df2['Category'], y=filtered_df2['Calories'],name='calories2', 
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat2, flavor2, dairy2, sweetener2, size2)],
                        orientation='v'), row=1, col=1)

    fig.add_trace(go.Bar(x=filtered_df1['Category'], y=filtered_df1['Weight Watcher Pnts'], name='ww1', 
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat1, flavor1, dairy1, sweetener1, size1)],
                        orientation='v'), row=1, col=2)

    fig.add_trace(go.Bar(x=filtered_df2['Category'], y=filtered_df2['Weight Watcher Pnts'], name='ww2', 
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat2, flavor2, dairy2, sweetener2, size2)],
                        orientation='v'), row=1, col=2)

    # Update layout
    fig.update_layout(showlegend=False, margin=dict(l=20, r=20), height=500, width=200, title_font=dict(size=16))
    fig.update_xaxes(showticklabels=False)    
    return fig

@app.callback(Output('drinks_grams', 'figure'),
              [Input('d1_category', 'value'), Input('d1_flavor', 'value'), Input('d1_dairy', 'value'), Input('d1_sweetener', 'value'), 
               Input('d2_category', 'value'), Input('d2_flavor', 'value'), Input('d2_dairy', 'value'), Input('d2_sweetener', 'value'),
               Input('drink1_size', 'value'), Input('drink2_size', 'value')])
def update_drinks_2(cat1, flavor1, dairy1, sweetener1, cat2, flavor2, dairy2, sweetener2, size1, size2):    
    filtered_df1 = drinks_df[
        (drinks_df['Category'] == cat1) &
        (drinks_df['Flavor'] == flavor1) &
        (drinks_df['Dairy'] == dairy1) &
        (drinks_df['Sweetener'] == sweetener1) &
        (drinks_df['Size'] == size1)
    ]

    filtered_df2 = drinks_df[
        (drinks_df['Category'] == cat2) &
        (drinks_df['Flavor'] == flavor2) &
        (drinks_df['Dairy'] == dairy2) &
        (drinks_df['Sweetener'] == sweetener2) &
        (drinks_df['Size'] == size2)
    ]

    # Define custom colors for each combination of category, flavor, dairy, and sweetener
    colors = {
        '{}_{}_{}_{}_{}'.format(cat1, flavor1, dairy1, sweetener1, size1): '#822F29',
        '{}_{}_{}_{}_{}'.format(cat2, flavor2, dairy2, sweetener2, size2): '#CA3D7D'
    }

    fig = make_subplots(rows=1, cols=6, shared_yaxes=True,
                        subplot_titles=('Sugars', 'Carbs', 'Protein', 'Fiber', 'Total Fat', 'Saturated Fats'),horizontal_spacing=0.01)

    fig.add_trace(go.Bar(x=filtered_df1['Category'], y=filtered_df1['Sugars (g)'],
                        name='Sugar1', orientation='v',
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat1, flavor1, dairy1, sweetener1, size1)]), row=1, col=1)

    fig.add_trace(go.Bar(x=filtered_df2['Category'], y=filtered_df2['Sugars (g)'],
                        name='Sugar2', orientation='v',
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat2, flavor2, dairy2, sweetener2, size2)]), row=1, col=1)
    
    fig.add_trace(go.Bar(x=filtered_df1['Category'], y=filtered_df1['Carbs (g)'],
                        name='Carbs1', orientation='v',
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat1, flavor1, dairy1, sweetener1, size1)]), row=1, col=2)

    fig.add_trace(go.Bar(x=filtered_df2['Category'], y=filtered_df2['Carbs (g)'],
                        name='Carbs2', orientation='v',
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat2, flavor2, dairy2, sweetener2, size2)]), row=1, col=2)

    fig.add_trace(go.Bar(x=filtered_df1['Category'], y=filtered_df1['Protein (g)'],
                        name='Protein1', orientation='v',
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat1, flavor1, dairy1, sweetener1, size1)]), row=1, col=3)

    fig.add_trace(go.Bar(x=filtered_df2['Category'], y=filtered_df2['Protein (g)'],
                        name='Protein2', orientation='v',
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat2, flavor2, dairy2, sweetener2, size2)]), row=1, col=3)
    
    fig.add_trace(go.Bar(x=filtered_df1['Category'], y=filtered_df1['Fiber (g)'],
                        name='Fiber1', orientation='v',
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat1, flavor1, dairy1, sweetener1, size1)]), row=1, col=4)

    fig.add_trace(go.Bar(x=filtered_df2['Category'], y=filtered_df2['Fiber (g)'],
                        name='Fiber2', orientation='v',
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat2, flavor2, dairy2, sweetener2, size2)]), row=1, col=4)

    fig.add_trace(go.Bar(x=filtered_df1['Category'], y=filtered_df1['Total Fat (g)'],
                        name='Total Fat1', orientation='v',
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat1, flavor1, dairy1, sweetener1, size1)]), row=1, col=5)

    fig.add_trace(go.Bar(x=filtered_df2['Category'], y=filtered_df2['Total Fat (g)'],
                        name='Total Fat2', orientation='v',
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat2, flavor2, dairy2, sweetener2, size2)]), row=1, col=5)
    
    fig.add_trace(go.Bar(x=filtered_df1['Category'], y=filtered_df1['Saturated Fat (g)'],
                        name='Saturated Fat1', orientation='v',
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat1, flavor1, dairy1, sweetener1, size1)]), row=1, col=6)

    fig.add_trace(go.Bar(x=filtered_df2['Category'], y=filtered_df2['Saturated Fat (g)'],
                        name='Saturated Fat2', orientation='v',
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat2, flavor2, dairy2, sweetener2, size2)]), row=1, col=6)

    # Update layout
    fig.update_layout(showlegend=False, margin=dict(l=20, r=20), height=500, width=900)
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(title_text='grams (g)', row=1, col=1)

    return fig
    
@app.callback(Output('drinks_mg', 'figure'),              
              [Input('d1_category', 'value'), Input('d1_flavor', 'value'), Input('d1_dairy', 'value'), Input('d1_sweetener', 'value'), 
               Input('d2_category', 'value'), Input('d2_flavor', 'value'), Input('d2_dairy', 'value'), Input('d2_sweetener', 'value'),
               Input('drink1_size', 'value'), Input('drink2_size', 'value')])
def update_drinks_3(cat1, flavor1, dairy1, sweetener1, cat2, flavor2, dairy2, sweetener2, size1, size2):    
    # Filter drinks_df based on the conditions for each combination of category, flavor, dairy, and sweetener
    filtered_df1 = drinks_df[
        (drinks_df['Category'] == cat1) &
        (drinks_df['Flavor'] == flavor1) &
        (drinks_df['Dairy'] == dairy1) &
        (drinks_df['Sweetener'] == sweetener1) &
        (drinks_df['Size'] == size1)
    ]

    filtered_df2 = drinks_df[
        (drinks_df['Category'] == cat2) &
        (drinks_df['Flavor'] == flavor2) &
        (drinks_df['Dairy'] == dairy2) &
        (drinks_df['Sweetener'] == sweetener2) &
        (drinks_df['Size'] == size2)
    ]

    # Define custom colors for each combination of category, flavor, dairy, and sweetener
    colors = {
        '{}_{}_{}_{}_{}'.format(cat1, flavor1, dairy1, sweetener1, size1): '#822F29',
        '{}_{}_{}_{}_{}'.format(cat2, flavor2, dairy2, sweetener2, size2): '#CA3D7D'
    }

    fig = make_subplots(rows=1, cols=2, shared_yaxes=True, subplot_titles=('Cholesterol', 'Sodium'), horizontal_spacing=0.02)

    fig.add_trace(go.Bar(x=filtered_df1['Category'],  y=filtered_df1['Cholesterol (mg)'], name='Cholesterol1', 
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat1, flavor1, dairy1, sweetener1, size1)],
                        orientation='v'), row=1, col=1)

    fig.add_trace(go.Bar(x=filtered_df2['Category'], y=filtered_df2['Cholesterol (mg)'],name='Cholesterol2', 
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat2, flavor2, dairy2, sweetener2, size2)],
                        orientation='v'), row=1, col=1)

    fig.add_trace(go.Bar(x=filtered_df1['Category'], y=filtered_df1['Sodium (mg)'], name='sodium1', 
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat1, flavor1, dairy1, sweetener1, size1)],
                        orientation='v'), row=1, col=2)

    fig.add_trace(go.Bar(x=filtered_df2['Category'], y=filtered_df2['Sodium (mg)'], name='sodium2', 
                        marker_color=colors['{}_{}_{}_{}_{}'.format(cat2, flavor2, dairy2, sweetener2, size2)],
                        orientation='v'), row=1, col=2)

    # Update layout
    fig.update_layout(showlegend=False, margin=dict(l=20, r=20), height=500, width=300)
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(title_text='milligrams (mg)', row=1, col=1)
    
    return fig
    


# Define callback to update the bakery item options based on selected categories
@app.callback(Output('item1', 'options'), Input('item1_cat', 'value'))
def update_item1_options(selected_category):
    filtered_df = bakery_df[bakery_df['Category'] == selected_category]
    item_options = [{'label': item, 'value': item} for item in filtered_df['Item'].unique()]
    return item_options

@app.callback(Output('item2', 'options'), Input('item2_cat', 'value'))
def update_item2_options(selected_category):
    filtered_df = bakery_df[bakery_df['Category'] == selected_category]
    item_options = [{'label': item, 'value': item} for item in filtered_df['Item'].unique()]
    return item_options

# Define callback to update bakery comparison graphs
@app.callback(Output('bakery_cal-ww', 'figure'), [Input('item1', 'value'), Input('item2', 'value')])
def update_bakery_1(item1, item2):
    # Filter dataframe based on selected items
    filtered_df = bakery_df[bakery_df['Item'].isin([item1, item2])]

    fig = make_subplots(rows=1, cols=2, shared_yaxes=True, subplot_titles=('Calories', 'WW'), horizontal_spacing=0.09)

    # Define custom colors for item1 and item2
    colors = {item1: '#DC5C34', item2: '#E59B47'}

    fig.add_trace(go.Bar(x=filtered_df['Item'], y=filtered_df['Calories'], name=item1,
                     marker_color=[colors.get(item, 'blue') for item in filtered_df['Item']], orientation='v'), row=1, col=1)

    fig.add_trace(go.Bar(x=filtered_df['Item'], y=filtered_df['Weight Watcher Pnts'], name=item2,
                        marker_color=[colors.get(item, 'blue') for item in filtered_df['Item']], orientation='v'), row=1, col=2)

    # Update layout
    fig.update_layout(showlegend=False, margin=dict(l=20, r=20), height=500, width=200, title_font=dict(size=10))
    fig.update_xaxes(showticklabels=False)
    
    return fig

@app.callback(Output('bakery_grams', 'figure'), [Input('item1', 'value'), Input('item2', 'value')])
def update_bakery_2(item1, item2):
    # Filter dataframe based on selected items
    filtered_df = bakery_df[bakery_df['Item'].isin([item1, item2])]
    #print(filtered_df)

    fig = make_subplots(rows=1, cols=6, shared_yaxes=True,
                        subplot_titles=('Sugars', 'Carbs', 'Protein', 'Fiber', 'Total Fat', 'Saturated Fats'),horizontal_spacing=0.01)

    # Define custom colors for item1 and item2
    colors = {item1: '#DC5C34', item2: '#E59B47'}

    fig.add_trace(go.Bar(x=filtered_df['Item'], y=filtered_df['Sugars (g)'], name='sugar', marker_color=[colors.get(item, 'blue') for item in filtered_df['Item']], orientation='v'), row=1, col=1)
    fig.add_trace(go.Bar(x=filtered_df['Item'], y=filtered_df['Carbs (g)'], name='carbs', marker_color=[colors.get(item, 'blue') for item in filtered_df['Item']], orientation='v'), row=1, col=2)
    fig.add_trace(go.Bar(x=filtered_df['Item'], y=filtered_df['Protein (g)'], name='protein', marker_color=[colors.get(item, 'blue') for item in filtered_df['Item']], orientation='v'), row=1, col=3)
    fig.add_trace(go.Bar(x=filtered_df['Item'], y=filtered_df['Fiber (g)'], name='fiber', marker_color=[colors.get(item, 'blue') for item in filtered_df['Item']], orientation='v'), row=1, col=4)
    fig.add_trace(go.Bar(x=filtered_df['Item'], y=filtered_df['Total Fat (g)'], name='total fat', marker_color=[colors.get(item, 'blue') for item in filtered_df['Item']], orientation='v'), row=1, col=5)
    fig.add_trace(go.Bar(x=filtered_df['Item'], y=filtered_df['Saturated Fat (g)'], name='saturated fat', marker_color=[colors.get(item, 'blue') for item in filtered_df['Item']], orientation='v'), row=1, col=6)

    # Update layout
    fig.update_layout(showlegend=False, margin=dict(l=20, r=20), height=500, width=900)
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(title_text='grams (g)', row=1, col=1)

    return fig
    
@app.callback(Output('bakery_mg', 'figure'), [Input('item1', 'value'), Input('item2', 'value')])
def update_bakery_3(item1, item2):
    # Filter dataframe based on selected items
    filtered_df = bakery_df[bakery_df['Item'].isin([item1, item2])]

    fig = make_subplots(rows=1, cols=2, subplot_titles=('Cholesterol', 'Sodium'), horizontal_spacing=0.25)

    # Define custom colors for item1 and item2
    colors = {item1: '#DC5C34', item2: '#E59B47'}

    fig.add_trace(go.Bar(x=filtered_df['Item'], y=filtered_df['Cholesterol (mg)'], name='cholesterol',
                     marker_color=[colors.get(item, 'blue') for item in filtered_df['Item']], orientation='v'), row=1, col=1)

    fig.add_trace(go.Bar(x=filtered_df['Item'], y=filtered_df['Sodium (mg)'], name='sodium',
                        marker_color=[colors.get(item, 'blue') for item in filtered_df['Item']], orientation='v'), row=1, col=2)

    # Update layout
    fig.update_layout(showlegend=False, margin=dict(l=20, r=20), height=500, width=300)
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(title_text='milligrams (mg)', row=1, col=1)
    
    return fig
    

if __name__ == '__main__':
    app.run_server(debug=True)
