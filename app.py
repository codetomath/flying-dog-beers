import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html





color_palette_blue_2 = ['#636EFA','#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#1F1F25', '#636EFA']


df= [
    ['2018-12',1.5],
    ['2019-01',2.5],
    ['2019-02',3.5],
    ['2019-03',4.5],
    ['2019-04',5.5]
    ]
df = pd.DataFrame(df, columns = ['Ay', 'NPL'])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df_2 = df

df_2_ay_NPL = df_2.groupby(['Ay'])['NPL'].sum(),df_2.groupby(['Ay'])['NPL'].count()
df_2_ay_NPL= pd.DataFrame(list( df_2_ay_NPL))
df_2_ay_NPL.reset_index(drop=True, inplace=True)
df_2_ay_NPL=df_2_ay_NPL.T
df_2_ay_NPL.reset_index(drop=False, inplace=True)
df_2_ay_NPL=df_2_ay_NPL.rename(columns = {0:'NPL', 1:'NPL_2'})
df_2_ay_NPL=df_2_ay_NPL[['Ay','NPL']]
df_2_ay_NPL['NPL'] = df_2_ay_NPL['NPL'].round(1)
df_2_ay_NPL

app.layout = html.Div([
    html.H1('Deneme')
    
    ])

                        
if __name__ == '__main__':
    app.run_server()
