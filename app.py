import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html





color_palette_blue_2 = ['#636EFA','#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#1F1F25', '#636EFA']



df = pd.read_csv('https://raw.githubusercontent.com/codetomath/distressed_loans/master/Loans%20Breakdown.csv', sep = ';',encoding='ISO-8859-9')
coordinates = pd.read_csv('https://raw.githubusercontent.com/codetomath/distressed_loans/master/Enlem-Boylam.csv', sep = ';', encoding='ISO-8859-9')


coordinates = df.merge(coordinates,on='Şehir',how='left')
coordinates = coordinates[['Şehir','Lattitude','Longitude']]
coordinates.drop_duplicates(subset ="Şehir", keep = "first", inplace = True) 





external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])





sube_list = df.sort_values(by=['Şube'], ascending = True)
# integer column names converted to string column names in order to eliminate Key Error
df.columns = df.columns.astype(str)
df_3 = df[df['Bölge'] == 'Ege']
sube_list_3 = df_3.sort_values(by=['Şube'], ascending = True)
df_4 = df[df['Şube'] == 'Kadıköy']
df_5 = df[df['Kredi Türü'] == 'Kredi Kartı']
df_6 = df[df['Tahsilat Ofisi'] == 'Tahsilat Ofisi-1']



df_2 = df_3

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
    

   
    
 #graph-output_03_orange 
dcc.Graph(
                        figure={
                                    'data': [
                                                {'x': (df_2_ay_NPL['Ay'].values.tolist()), 'y': (df_2_ay_NPL['NPL'].values.tolist()), 'type': 'bar', 'name': df_2_ay_NPL['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_ay_NPL['NPL'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'x+text'}
                                            ],
                                    'layout':   {
                                                    'height' : 175,
                                                    'width' : 800,
                                                    'title': ' Aylık NPL Aktarımları (M TL)', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': df_2_ay_NPL['Ay'], 'ticktext': df_2_ay_NPL['Ay']},
                                                    'margin' : {'l': 40,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

    )
    
    ])

                        
if __name__ == '__main__':
    app.run_server()
