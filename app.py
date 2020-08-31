import pandas as pd
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px




color_palette_blue = ['#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#50526F', '#1F1F25', '#50526F', '#6D73C1', '#636EFA', '#6D73C1', '#50526F', '#1F1F25']
color_palette_blue_2 = ['#636EFA','#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#1F1F25', '#636EFA']
color_palette_blue_3 = ['#1F1F25','#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA', '#636EFA']
color_palette_heatmap_pale_4_descending =  ['#90FB83', '#ECFB83', '#FBDC83', '#FB9083']
color_palette_heatmap_pale_10_descending = ['#90FB83', '#A6FB83','#B0FB83', '#CFFB83', '#ECFB83', '#FBF483', '#FBDC83', '#FBC683', '#FBA983', '#FB9083']
color_palette_heatmap_pale_10 = [ '#FB9083', '#FBA983', '#FBC683', '#FBDC83', '#FBF483', '#ECFB83', '#CFFB83','#B0FB83', '#A6FB83','#90FB83']
color_palette_heatmap_pale_6_descending =  ['#90FB83', '#CFFB83', '#ECFB83', '#FBDC83', '#FBA983', '#FB9083']
color_palette_heatmap_pale_6 =  ['#FB9083', '#FBA983', '#FBDC83', '#ECFB83', '#CFFB83', '#90FB83']
color_palette_heatmap_pale_5 =  ['#90FB83', '#CFFB83', '#FBDC83', '#FBA983', '#FB9083']
color_palette_heatmap_pale_5_descending =  ['#FB9083', '#FBA983', '#FBDC83', '#CFFB83', '#90FB83']


color_palette_heatmap_pale_3_descending =  ['#90FB83', '#ECFB83', '#FB9083'] 
color_palette_heatmap_pale_3 =  ['#FB9083', '#ECFB83', '#90FB83'] 
color_palette_heatmap_pale_2_descending =  ['#90FB83', '#FB9083']  
color_palette_heatmap_pale_2 =  ['#FB9083', '#90FB83'] 



df = pd.read_csv('https://raw.githubusercontent.com/codetomath/distressed_loans/master/Loans%20Breakdown.csv', sep = ';',encoding='ISO-8859-9')
coordinates = pd.read_csv('https://raw.githubusercontent.com/codetomath/distressed_loans/master/Enlem-Boylam.csv', sep = ';', encoding='ISO-8859-9')


coordinates = df.merge(coordinates,on='Şehir',how='left')
coordinates = coordinates[['Şehir','Lattitude','Longitude']]
coordinates.drop_duplicates(subset ="Şehir", keep = "first", inplace = True) 





external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server




sube_list = df.sort_values(by=['Şube'], ascending = True)
# integer column names converted to string column names in order to eliminate Key Error
df.columns = df.columns.astype(str)
df_3 = df[df['Bölge'] == 'Ege']
sube_list_3 = df_3.sort_values(by=['Şube'], ascending = True)
df_4 = df[df['Şube'] == 'Kadıköy']
df_5 = df[df['Kredi Türü'] == 'Kredi Kartı']
df_6 = df[df['Tahsilat Ofisi'] == 'Tahsilat Ofisi-1']







app.layout = html.Div([
        dcc.Tabs([
            
            

        dcc.Tab(label='Ana Sayfa', style={"color": "white","background": "#5D6D7E", 'textAlign': 'center', 'verticalAlign': 'middle','width':'100%', 'height' : 5, 'line-height' : 0 ,'margin-top':0 , 'margin-bottom':0 ,'margin-left' : 0,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '90%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'},selected_style={"color": "white","background": "#1F1F25", 'textAlign': 'center', 'verticalAlign': 'middle', 'width':'100%', 'height' : 5, 'line-height' : 0 , 'margin-top':0 , 'margin-left' : 0,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '90%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'},
                children=[  
                    
                    
                    html.Div([
    
    
    html.Div([dcc.Markdown('''EMPTY''', style={"color": "rgba(0,0,0,0)", 'textAlign': 'center', 'height' : 350})
              ]),
    html.Div([html.H1('''Sorunlu Kredilerin Yönetimi''', style={"color": "white", 'textAlign': 'center', 'font-size': '500%' })
              ]),
    html.Div([dcc.Markdown('''EMPTY''', style={"color": "rgba(0,0,0,0)", 'textAlign': 'center', 'height' : 100})
              ]),
    html.Div([
        html.H1('''Kullanıcı Adı :''', style={"color": "white", 'textAlign': 'right', 'font-size': '200%', 'margin-left':00}, className="six columns"),
        dcc.Input(id='Username_Input', value='', type='text', placeholder='',  style={'margin-left':'1%','margin-top':0, 'background': 'white', 'width': '15%' ,'font-style': 'italic', 'color' : '#99A3A4'}, className="two columns")
              ], className="row"),
    html.Div([
        html.H1('''Şifre :''', style={"color": "white", 'textAlign': 'right', 'font-size': '200%', 'margin-left':00}, className="six columns"),
        dcc.Input(id='Password_Input', value='', type='password', placeholder='',  style={'margin-left':'1%','margin-top':0, 'background': 'white', 'width': '15%' ,'font-style': 'italic', 'color' : '#99A3A4'}, className="two columns")
              ], className="row"),
    html.Div([
        html.H1('''EMPTY''', style={"color": "rgba(0,0,0,0)", 'textAlign': 'left', 'font-size': '200%', 'margin-left':00}, className="six columns"),
        dcc.Link('Giriş', href='/', refresh = True,loading_state = {'is_loading': True},style={"color": "white", 'font-size': '200%', 'textAlign': 'center', 'margin-left':'1%'})
              ], className="row"),            
    html.Div([dcc.Markdown('''EMPTY''', style={"color": "rgba(0,0,0,0)", 'textAlign': 'center', 'height' : 250})
              ]),
    html.Div(id = 'Test')
   
   
],style={"background-color": 'rgba(0,0,0,0)','background-image':'url(https://i.ibb.co/938TR8S/Background-02.jpg)', 'repeat': False})

            
            ]),
            
            
            
        dcc.Tab(label='İdari Takip', style={"color": "white","background": "#5D6D7E", 'textAlign': 'center', 'verticalAlign': 'middle','width':'100%', 'height' : 5, 'line-height' : 0 ,'margin-top':0 , 'margin-bottom':0 ,'margin-left' : 0,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '90%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'},selected_style={"color": "white","background": "#1F1F25", 'textAlign': 'center', 'verticalAlign': 'middle', 'width':'100%', 'height' : 5, 'line-height' : 0 , 'margin-top':0 , 'margin-left' : 0,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '90%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'},
                children=[

                                            
                        # ROW-1
    
                        html.Div([
                                    html.Div(
                                                [
                                                    html.H1('''Gecikmedeki Krediler''', style={"color": "white","background": "#5D6D7E", 'textAlign': 'left', 'width':'100%', 'height' : 45 ,'margin-top':10 , 'margin-left' : 30,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '250%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'})
                                                ], className = 'five columns'),
                                    
                                    
  

                                  
                                    
                                                html.Div([html.I('Bölge    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Bölge_Filtresi',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df['Bölge'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Bölge Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': '1%'}),                        
                                     
                                    
  




                                                html.Div([html.I('Kredi Türü    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Kredi Türü_Filtresi',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df['Kredi Türü'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Kredi Türü Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': '1%'}),                        
                                    
                                    
  

                                  
                                    
                                                html.Div([html.I('Segment    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Segment_Filtresi',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df['Segment'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Segment Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': '1%'}),                        
                                     
                                    
                                    
                                    
                                                html.Div([html.I('Şube    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Şube_Filtresi',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in sube_list['Şube'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Şube Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': '1%'}),                        
                                     
   
                                         
            
                        
                        ], className="row", style = {'background': '#5D6D7E'}),

                        
                        html.Div([ 

                                            html.Div([          
                                                                html.Div([html.H1('Aylık NPL Aktarımı', style={"color": "#5D6D7E","background": "rgba(0,0,0,0)", 'textAlign': 'center', 'width':'75%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '150%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '0%', 'margin-left': '25%'})]),  
                                                                html.Div([html.Div(id='card-output_01_apple')]),
                                                                html.Div([html.H1('Yıllık NPL Aktarımı', style={"color": "#5D6D7E","background": "rgba(0,0,0,0)", 'textAlign': 'center', 'width':'75%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '150%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '0%', 'margin-left': '25%'})]),
                                                                html.Div([html.Div(id='card-output_01_orange')])
                                                                
                                                ], className="four columns"),
                                            
                                            html.Div(id='graph-output_01_apple', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '20%', 'margin-right': '0%', 'margin-bottom': '0%'}, className="six columns"),

                        ], className="row", style = {'margin-top': '1%'}), 


                                            html.Div(id='graph-output_01_orange', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}, className="five columns"),
                                            
                                            html.Div(id='graph-output_01_banana', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '10%', 'margin-right': '0%', 'margin-bottom': '0%'}, className="six columns"),
                                            
                                            html.Div(id='graph-output_01_lemon', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}, className="five columns"),
                                                                
                                            html.Div(id='graph-output_01_cherry', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '10%', 'margin-right': '0%', 'margin-bottom': '0%'}, className="six columns"),

                                            
                                     
    

                        # ROW-5
                         html.Div([
                        html.Div(
                                    [
                                        html.Span('''Roll Rate Gelişimi''', style={"color": "#5D6D7E","background": "rgba(0,0,0,0)", 'width':'100%', 'height' : 10 ,'margin-top':0, 'margin-left':0 ,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '150%' , 'font-style': 'italic', 'border-bottom': '10px', 'textAlign': 'center'})

                                        
                                        
                                        ],className="ten columns"
                                )
                        ],className="row"), 
                            
                            

                        # ROW-6
                        html.Div([                            
                            
                        
                                            html.Div([                                                
                                                                html.Div(id='graph-output_01_apricot_1', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '10%', 'margin-right': '0%', 'margin-bottom': '0%'}),                                                
                                                ], className="two columns"),        
                                            
                                            html.Div([                                                
                                                                html.Div(id='graph-output_01_apricot_2', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '2%', 'margin-right': '0%', 'margin-bottom': '0%'}),                                                
                                                ], className="two columns"), 
                                            
                                            html.Div([                                                
                                                                html.Div(id='graph-output_01_apricot_3', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '2%', 'margin-right': '0%', 'margin-bottom': '0%'}),                                                
                                                ], className="two columns"), 
                                            
                                             html.Div([                                                
                                                                html.Div(id='graph-output_01_apricot_4', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '2%', 'margin-right': '0%', 'margin-bottom': '0%'}),                                                
                                                ], className="two columns"),       
                                            
                                             html.Div([                                                
                                                                html.Div(id='graph-output_01_apricot_5', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '2%', 'margin-right': '0%', 'margin-bottom': '0%'}),                                                
                                                ], className="two columns"),
                                        
                                             
                                             
                                    ], className="row", style = {'margin-top': 0}), 
    
                                            
                                            html.Div(id='graph-output_01_mango', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}, className="six columns"),
                                            
                                            html.Div(id='graph-output_01_coconut', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '5%', 'margin-right': '0%', 'margin-bottom': '0%'}, className="four columns"),

                                            
                                       
    
    
    ]),
                dcc.Tab(label='Yasal Takip', style={"color": "white","background": "#5D6D7E", 'textAlign': 'center', 'verticalAlign': 'middle','width':'100%', 'height' : 5, 'line-height' : 0 ,'margin-top':0 , 'margin-bottom':0 ,'margin-left' : 0,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '90%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'},selected_style={"color": "white","background": "#1F1F25", 'textAlign': 'center', 'verticalAlign': 'middle', 'width':'100%', 'height' : 5, 'line-height' : 0 ,'margin-top':0 , 'margin-left' : 0,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '90%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'},
                
                        children=[
                    
                        
                                       # ROW-1
    
                        html.Div([
                                    html.Div(
                                                [
                                                    html.H1('''Takipteki Krediler''', style={"color": "white","background": "#5D6D7E", 'textAlign': 'left', 'width':'130%', 'height' : 45 ,'margin-top':10 , 'margin-left' : 30,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '250%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'})
                                                ], className = 'five columns'),
                                    
                                    
  

                                  
                                    
                                                html.Div([html.I('Bölge    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Bölge_Filtresi_tab2',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df['Bölge'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Bölge Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': '1%'}),                        
                                     
                                    
  




                                                html.Div([html.I('Kredi Türü    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Kredi Türü_Filtresi_tab2',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df['Kredi Türü'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Kredi Türü Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': '1%'}),                        
                                    
                                    
 

                                  
                                    
                                                html.Div([html.I('Şube    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Şube_Filtresi_tab2',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in sube_list['Şube'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Şube Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': '1%'}),                        
                                     
                                     
                                  
                                    
                                                html.Div([html.I('Tahsilat Ofisi    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Tahsilat_Ofisi_Filtresi_tab2',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df['Tahsilat Ofisi'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Tahsilat Ofisi Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': '1%'}),                        
                                     
                                             
            
                        
                        ], className="row", style = {'background': '#5D6D7E'}),
     
                    
                    
                    
                        # ROW-2
                        html.Div([

                                            html.Div([          
                                                                html.Div([html.H1('Aylık NPL Tahsilatı', style={"color": "#5D6D7E","background": "rgba(0,0,0,0)", 'textAlign': 'center', 'width':'75%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '150%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '0%', 'margin-left': '25%'})]),  
                                                                html.Div([html.Div(id='card-output_02_apple')]),
                                                                html.Div([html.H1('Yıllık NPL Tahsilatı', style={"color": "#5D6D7E","background": "rgba(0,0,0,0)", 'textAlign': 'center', 'width':'75%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '150%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '0%', 'margin-left': '25%'})]),
                                                                html.Div([html.Div(id='card-output_02_orange')]),
                                                                html.Div([html.H1('12. Ay NPL Tahsilat %', style={"color": "#5D6D7E","background": "rgba(0,0,0,0)", 'textAlign': 'center', 'width':'75%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '150%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '0%', 'margin-left': '25%'})]),
                                                                html.Div([html.Div(id='card-output_02_banana')])                                                                
                                                ], className="four columns"),
                                            
                                                                html.Div(id='graph-output_02_apple', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '10%', 'margin-right': '0%', 'margin-bottom': '0%'},className="seven columns"),
                                         

                                                ], className="row", style = {'margin-top': '1%'}),

                                                                                  
                                          
                                            html.Div(id='graph-output_02_orange', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}, className="six columns"),

                                            
                                            html.Div(id='graph-output_02_banana', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}, className="six columns"),
                                                         
                                            
                                            html.Div(id='graph-output_02_lemon', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}, className="twelve columns"),
                    

                                            html.Div(id='graph-output_02_cherry', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}, className="six columns"),


                                            html.Div(id='graph-output_02_apricot', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '5%', 'margin-right': '0%', 'margin-bottom': '0%'}, className="four columns")        
                    
                    
                    
    ]),
                                                

                dcc.Tab(label='Tablo', style={"color": "white","background": "#5D6D7E", 'textAlign': 'center', 'verticalAlign': 'middle','width':'100%', 'height' : 5, 'line-height' : 0 ,'margin-top':0 , 'margin-bottom':0 ,'margin-left' : 0,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '90%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'},selected_style={"color": "white","background": "#1F1F25", 'textAlign': 'center', 'verticalAlign': 'middle', 'width':'100%', 'height' : 5, 'line-height' : 0 ,'margin-top':0 , 'margin-left' : 0,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '90%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'},
                children=[
                    
                                                                
                        # ROW-1
    
                        html.Div([
                                    html.Div(
                                                [
                                                    html.H1('''Sorunlu Krediler''', style={"color": "white","background": "#5D6D7E", 'textAlign': 'left', 'width':'100%', 'height' : 45 ,'margin-top':10 , 'margin-left' : 30,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '250%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'})
                                                ], className = 'five columns'),
                                    
                                    
  

                                  
                                    
                                                html.Div([html.I('Bölge    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Bölge_Filtresi_tab7',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df['Bölge'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Bölge Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': '1%'}),                        
                                     
                                    
  




                                                html.Div([html.I('Kredi Türü    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Kredi Türü_Filtresi_tab7',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df['Kredi Türü'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Kredi Türü Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left':'1%'}),                        
                                    
                                    
  

                                  
                                    
                                                html.Div([html.I('Segment    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Segment_Filtresi_tab7',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df['Segment'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Segment Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': '1%'}),                        
                                     
                                    
                                    
  

                                  
                                    
                                                html.Div([html.I('Şube    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Şube_Filtresi_tab7',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df['Şube'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Şube Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': '1%'}),                        
                                     
                                                    
                                             
            
                        
                        ], className="row", style = {'background': '#5D6D7E'}),
                        
                        
                        # ROW-2
                        html.Div([
                                    html.Span('''Gecikmedeki Kredilere İlişkin Detaylar''', style={"color": "#5D6D7E","background": "rgba(0,0,0,0)", 'width':'100%', 'height' : 10 ,'textAlign': 'center','margin-top':'2%','display': 'inline-block', 'font-family': "Calibri" , 'font-size': '150%' , 'font-style': 'italic', 'border-bottom': '10px'}),
                                    html.Div(id='table-output_07_apple',style={'margin-left': '2%','margin-right': '2%','margin-top': '1%'})
                                ]), 
                        
                    
                    ]),                         
                                
                                
                 
                                
                
                dcc.Tab(label='Bölge', style={"color": "white","background": "#5D6D7E", 'textAlign': 'center', 'verticalAlign': 'middle','width':'100%', 'height' : 5, 'line-height' : 0 ,'margin-top':0 , 'margin-bottom':0 ,'margin-left' : 0,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '90%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'},selected_style={"color": "white","background": "#1F1F25", 'textAlign': 'center', 'verticalAlign': 'middle', 'width':'100%', 'height' : 5, 'line-height' : 0 ,'margin-top':0 , 'margin-left' : 0,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '90%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'},
                children=[
                    
                    
                    
 
                    
                                         # ROW-1
    
                        html.Div([
                                    html.Div(
                                                [
                                                    html.H1('''Ege Bölgesi''', style={"color": "white","background": "#5D6D7E", 'textAlign': 'left', 'width':'100%', 'height' : 45 ,'margin-top':10 , 'margin-left' : 30,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '250%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'})
                                                ], className = 'four columns'),
                                    
                                    




                                                html.Div([html.I('Şube    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Şube_Filtresi_tab3',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in sube_list_3['Şube'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Şube Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': 130}),                        
                                     
             






                                                html.Div([html.I('Kredi Türü    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Kredi Türü_Filtresi_tab3',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df['Kredi Türü'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Kredi Türü Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': 50}),                        
                                    
                                    
  

                                  
                                    
                                                 html.Div([html.I('Segment    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Segment_Filtresi_tab3',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df_3['Segment'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Segment Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': 50}),                        
                                     
                                                     
                                    

                                    


                                  
                                    
                                                html.Div([html.I('Ay    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Ay_Filtresi_tab3',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df['Ay'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Ay Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': 50}),                        
                                     
                                             
            
                        
                        ], className="row", style = {'background': '#5D6D7E'}),


                        # ROW-2
                        html.Div([

                                            html.Div([          
                                                                html.Div([html.H1('Son 12 Ay NPL Aktarımı (M TL)', style={"color": "#5D6D7E","background": "rgba(0,0,0,0)", 'textAlign': 'center', 'width':'120%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '150%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '0%', 'margin-left': '0%'})]),  
                                                                html.Div([html.Div(id='card-output_03_apple')]),
                                                                html.Div([html.H1('Son 12 Ay NPL Tahsilatı (M TL)', style={"color": "#5D6D7E","background": "rgba(0,0,0,0)", 'textAlign': 'center', 'width':'120%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '150%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '0%', 'margin-left': '0%'})]),
                                                                html.Div([html.Div(id='card-output_03_orange')]),
                                                                html.Div(id='graph-output_03_apple', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}),

                                                ], className="three columns"),
                                            
                                            
                                            html.Div([                                               
                                            
                                                                html.Div(id='graph-output_03_orange', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}),
                                                                html.Div(id='graph-output_03_banana', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}),
                                                ], className="five columns"),                                            



                                            html.Div([                                               
                                            
                                                                html.Div(id='graph-output_03_lemon', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}),
                                                                html.Div(id='graph-output_03_cherry', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}),
                                                ], className="four columns"),  
                                            
                                            
                                    ], className="row", style = {'margin-top': 20}),                       


                        # ROW-3
                         html.Div([
                        html.Div(
                                    [
                                        html.Span('''Roll Rate Gelişimi''', style={"color": "#5D6D7E","background": "rgba(0,0,0,0)", 'width':'100%', 'height' : 10 ,'margin-top':0, 'margin-left':500 ,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '150%' , 'font-style': 'italic', 'border-bottom': '10px'})

                                        
                                        
                                        ],className="four columns"
                                )
                        ],className="row"),
                            
 


                           

                        # ROW-4
                        html.Div([                            
                            
                        
                                            html.Div([                                                
                                                                html.Div(id='graph-output_03_apricot_1', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '10%', 'margin-right': '0%', 'margin-bottom': '0%'}),                                                
                                                ], className="two columns"),        
                                            
                                            html.Div([                                                
                                                                html.Div(id='graph-output_03_apricot_2', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '-30%', 'margin-right': '0%', 'margin-bottom': '0%'}),                                                
                                                ], className="two columns"), 
                                            
                                            html.Div([                                                
                                                                html.Div(id='graph-output_03_apricot_3', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '-60%', 'margin-right': '0%', 'margin-bottom': '0%'}),                                                
                                                ], className="two columns"), 
                                            
                                             html.Div([                                                
                                                                html.Div(id='graph-output_03_apricot_4', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '-90%', 'margin-right': '0%', 'margin-bottom': '0%'}),                                                
                                                ], className="two columns"),       
                                            
                                             html.Div([                                                
                                                                html.Div(id='graph-output_03_apricot_5', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '-120%', 'margin-right': '0%', 'margin-bottom': '0%'}),                                                
                                                ], className="two columns"),
                                             
                                            html.Div([                                               
                                            
                                                                html.Div(id='graph-output_03_mango', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '-130%', 'margin-right': '0%', 'margin-bottom': '0%'}),
                                                                html.Div(id='graph-output_03_coconut', style={'display': 'inline-block', 'margin-top': '10%', 'margin-left': '-130%', 'margin-right': '0%', 'margin-bottom': '0%'})
                                                ], className="two columns"),                                               
                                             
                                             
                                             
                                             
                                    ], className="row", style = {'margin-top': 0}),    
                    
             
                    
                    
    ]),
                dcc.Tab(label='Şube', style={"color": "white","background": "#5D6D7E", 'textAlign': 'center', 'verticalAlign': 'middle','width':'100%', 'height' : 5, 'line-height' : 0 ,'margin-top':0 , 'margin-bottom':0 ,'margin-left' : 0,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '90%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'},selected_style={"color": "white","background": "#1F1F25", 'textAlign': 'center', 'verticalAlign': 'middle', 'width':'100%', 'height' : 5, 'line-height' : 0 ,'margin-top':0 , 'margin-left' : 0,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '90%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'},
                children=[
        
 
                    
                    
                    
 
                    
                                         # ROW-1
    
                        html.Div([
                                    html.Div(
                                                [
                                                    html.H1('''Kadıköy Şubesi''', style={"color": "white","background": "#5D6D7E", 'textAlign': 'left', 'width':'100%', 'height' : 45 ,'margin-top':10 , 'margin-left' : 30,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '250%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'})
                                                ], className = 'six columns'),
                                    
                                    



                                                html.Div([html.I('Kredi Türü    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Kredi Türü_Filtresi_tab4',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df['Kredi Türü'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Kredi Türü Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': 90}),                        
                                    
                                    
  

                                  
                                    
                                                 html.Div([html.I('Segment    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Segment_Filtresi_tab4',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df_3['Segment'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Segment Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': 50}),                        
                                     
                                                     
                                    

                                    


                                  
                                    
                                                html.Div([html.I('Ay    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Ay_Filtresi_tab4',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df['Ay'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Ay Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': 50}),                        
                                     
                                             
            
                        
                        ], className="row", style = {'background': '#5D6D7E'}),


                        # ROW-2
                        html.Div([

                                            html.Div([          
                                                                html.Div([html.H1('Son 12 Ay NPL Aktarımı (M TL)', style={"color": "#5D6D7E","background": "rgba(0,0,0,0)", 'textAlign': 'center', 'width':'120%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '150%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '0%', 'margin-left': '0%'})]),  
                                                                html.Div([html.Div(id='card-output_04_apple')]),
                                                                html.Div([html.H1('Son 12 Ay NPL Tahsilatı (M TL)', style={"color": "#5D6D7E","background": "rgba(0,0,0,0)", 'textAlign': 'center', 'width':'120%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '150%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '0%', 'margin-left': '0%'})]),
                                                                html.Div([html.Div(id='card-output_04_orange')]),
                                                                html.Div(id='graph-output_04_apple', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}),

                                                ], className="three columns"),
                                            
                                            
                                            html.Div([                                               
                                            
                                                                html.Div(id='graph-output_04_orange', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}),
                                                                html.Div(id='graph-output_04_banana', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}),
                                                ], className="five columns"),                                            



                                            html.Div([                                               
                                            
                                                                html.Div(id='graph-output_04_lemon', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}),
                                                                html.Div(id='graph-output_04_cherry', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}),
                                                ], className="four columns"),  
                                            
                                            
                                    ], className="row", style = {'margin-top': 20}),                       


                        # ROW-3
                         html.Div([
                        html.Div(
                                    [
                                        html.Span('''Roll Rate Gelişimi''', style={"color": "#5D6D7E","background": "rgba(0,0,0,0)", 'width':'100%', 'height' : 10 ,'margin-top':0, 'margin-left':500 ,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '150%' , 'font-style': 'italic', 'border-bottom': '10px'})

                                        
                                        
                                        ],className="four columns"
                                )
                        ],className="row"),
                            
                            

                        # ROW-4
                        html.Div([                            
                            
                        
                                            html.Div([                                                
                                                                html.Div(id='graph-output_04_apricot_1', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '10%', 'margin-right': '0%', 'margin-bottom': '0%'}),                                                
                                                ], className="two columns"),        
                                            
                                            html.Div([                                                
                                                                html.Div(id='graph-output_04_apricot_2', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '-30%', 'margin-right': '0%', 'margin-bottom': '0%'}),                                                
                                                ], className="two columns"), 
                                            
                                            html.Div([                                                
                                                                html.Div(id='graph-output_04_apricot_3', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '-60%', 'margin-right': '0%', 'margin-bottom': '0%'}),                                                
                                                ], className="two columns"), 
                                            
                                             html.Div([                                                
                                                                html.Div(id='graph-output_04_apricot_4', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '-90%', 'margin-right': '0%', 'margin-bottom': '0%'}),                                                
                                                ], className="two columns"),       
                                            
                                             html.Div([                                                
                                                                html.Div(id='graph-output_04_apricot_5', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '-120%', 'margin-right': '0%', 'margin-bottom': '0%'}),                                                
                                                ], className="two columns"),
                                             
                                            html.Div([                                               
                                            
                                                                html.Div(id='graph-output_04_mango', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '-130%', 'margin-right': '0%', 'margin-bottom': '0%'}),
                                                                html.Div(id='graph-output_04_coconut', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '-130%', 'margin-right': '0%', 'margin-bottom': '0%'}),
                                                ], className="two columns"),                                               
                                             
                                             
                                             
                                             
                                    ], className="row", style = {'margin-top': 0}),                        
                    
                    
                    
                    
                    
                    
                    
                    
    ]),

                dcc.Tab(label='Tahsilat Ofisi', style={"color": "white","background": "#5D6D7E", 'textAlign': 'center', 'verticalAlign': 'middle','width':'100%', 'height' : 5, 'line-height' : 0 ,'margin-top':0 , 'margin-bottom':0 ,'margin-left' : 0,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '90%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'},selected_style={"color": "white","background": "#1F1F25", 'textAlign': 'center', 'verticalAlign': 'middle', 'width':'100%', 'height' : 5, 'line-height' : 0 ,'margin-top':0 , 'margin-left' : 0,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '90%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'},
                children=[
                    
                    
                    
                    
                    
                       # ROW-1
    
                        html.Div([
                                    html.Div(
                                                [
                                                    html.H1('''Tahsilat Ofisi-1''', style={"color": "white","background": "#5D6D7E", 'textAlign': 'left', 'width':'130%', 'height' : 45 ,'margin-top':10 , 'margin-left' : 30,'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '250%' ,'padding-left':'0%', 'justify-content': 'center', 'font-style': 'italic'})
                                                ], className = 'four columns'),
                                    
                                    
  

                                  
                                    
                                                html.Div([html.I('Bölge    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Bölge_Filtresi_tab6',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df['Bölge'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Bölge Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': 100}),                        
                                     
                                    
  




                                                html.Div([html.I('Kredi Türü    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Kredi Türü_Filtresi_tab6',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df['Kredi Türü'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Kredi Türü Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': 50}),                        
                                    
                                    
  

                                  
                                    
                                                html.Div([html.I('Segment    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Segment_Filtresi_tab6',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in df['Segment'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Segment Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': 50}),                        
                                     
                                    
                                    
  

                                  
                                    
                                                html.Div([html.I('Şube    :',style={"background": "rgba(0,0,0,0)", 'color':'white', 'font-family': "Calibri", 'font-size': '100%'}),
                                                          dcc.Dropdown(id = 'Şube_Filtresi_tab6',
                                                             options=[{'label': 'Tümü', 'value': 'All'}] + [{'label': i, 'value': i} for i in sube_list['Şube'].unique()], 
                                                             value= 'All',
                                                             multi=False,
                                                             placeholder='Şube Seçiniz',
                                                             style={'width': '100%','margin-top':0, 'background': 'white)', 'color': '#5D6D7E', 'font-family': "Calibri", 'font-size': '90%'}
                                                             )
                                            ], className="two columns", style={'font-family': "Calibri" , 'font-size': '100%' ,'justify-content': 'center', 'font-style': 'italic', 'background': '#5D6D7E', 'color': 'white', 'margin-left': 50}),                        
                                     
                                     
                                   
                                             
            
                        
                        ], className="row", style = {'background': '#5D6D7E'}),
     
                    
                    
                    
                        # ROW-2
                        html.Div([

                                            html.Div([          
                                                                html.Div([html.H1('Aylık NPL Tahsilatı (M TL)', style={"color": "#5D6D7E","background": "rgba(0,0,0,0)", 'textAlign': 'center', 'width':'120%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '150%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '0%', 'margin-left': '0%'})]),  
                                                                html.Div([html.Div(id='card-output_06_apple')]),
                                                                html.Div([html.H1('Son 12 Ay NPL Tahsilatı (M TL)', style={"color": "#5D6D7E","background": "rgba(0,0,0,0)", 'textAlign': 'center', 'width':'120%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '150%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '0%', 'margin-left': '0%'})]),
                                                                html.Div([html.Div(id='card-output_06_orange')]),
                                                                html.Div([html.H1('12. Ay NPL Tahsilat %', style={"color": "#5D6D7E","background": "rgba(0,0,0,0)", 'textAlign': 'center', 'width':'120%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '150%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '0%', 'margin-left': '0%'})]),
                                                                html.Div([html.Div(id='card-output_06_banana')])                                                                
                                                ], className="three columns"),
                                            
                                            
                                            html.Div([                                               
                                            
                                                                html.Div(id='graph-output_06_apple', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}),
                                                ], className="five columns"),                                            



                                            html.Div([                                               
                                            
                                                                html.Div(id='graph-output_06_orange', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}),
                                                ], className="four columns"),  
                                            
                                            
                                    ], className="row", style = {'margin-top': 20}),                       
                    
                    
                    

                        # ROW-3
                        html.Div([



                                            html.Div([                                               
                                            
                                                                html.Div(id='graph-output_06_banana', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}),
                                                ], className="six columns"),  
                                            
                                            
                                            html.Div([                                               
                                            
                                                                html.Div(id='graph-output_06_lemon', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '40%', 'margin-right': '0%', 'margin-bottom': '0%'}),
                                                ], className="two columns"),                                            

                                            
                                            
                                    ], className="row", style = {'margin-top': 20}),    




                        # ROW-4
                        html.Div([



                                            html.Div([                                               
                                            
                                                                html.Div(id='graph-output_06_cherry', style={'display': 'inline-block', 'margin-top': '0%', 'margin-left': '0%', 'margin-right': '0%', 'margin-bottom': '0%'}),
                                                ], className="twelve columns"),  
                                            

                                            
                                            
                                    ], className="row", style = {'margin-top': 20}),  
                    
                    
       
                    
                    
                    ])

        
        ])
    
                    ],style={"background-color": 'rgba(0,0,0,0)','background-image':'url(https://i.ibb.co/MVY0nMr/Background-01.jpg)', 'repeat': False})




#tab-1 callback begins here
@app.callback([Output('card-output_01_apple', 'children'),Output('card-output_01_orange', 'children'),Output('graph-output_01_apple', 'children'),Output('graph-output_01_orange', 'children'),Output('graph-output_01_banana', 'children'),Output('graph-output_01_lemon', 'children'),Output('graph-output_01_cherry', 'children'),Output('graph-output_01_apricot_1', 'children'),Output('graph-output_01_apricot_2', 'children'),Output('graph-output_01_apricot_3', 'children'),Output('graph-output_01_apricot_4', 'children'),Output('graph-output_01_apricot_5', 'children'),Output('graph-output_01_mango', 'children'),Output('graph-output_01_coconut', 'children')],
              [Input('Bölge_Filtresi', 'value'),
              Input('Kredi Türü_Filtresi', 'value'),
              Input('Segment_Filtresi', 'value'),
              Input('Şube_Filtresi', 'value'),
               ]) 


def update_value(input_1, input_2, input_3, input_4):  
    
    df_2 = df


    # BÖLGE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Bölge'] == input_1]  

   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  


    # ŞUBE FİLTRESİ    
    if input_4 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_4] 


    last_month_NPL = df_2[df_2['Ay_2'] == max(df_2['Ay_2'])]
    last_month_NPL = round(sum(last_month_NPL['NPL']),1)



    df_2 = df
    
    # BÖLGE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Bölge'] == input_1]  

   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  


    # ŞUBE FİLTRESİ    
    if input_4 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_4] 


    total_NPL = round(sum(df_2['NPL']),1)
    



    df_2 = df
    
    # BÖLGE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Bölge'] == input_1]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  


    # ŞUBE FİLTRESİ    
    if input_4 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_4] 


    
    df_2_kredi_türü = df_2.groupby(['Kredi Türü'])['NPL'].sum(),df_2.groupby(['Kredi Türü'])['NPL'].count()
    df_2_kredi_türü= pd.DataFrame(list( df_2_kredi_türü))
    df_2_kredi_türü.reset_index(drop=True, inplace=True)
    df_2_kredi_türü=df_2_kredi_türü.T
    df_2_kredi_türü.reset_index(drop=False, inplace=True)
    df_2_kredi_türü=df_2_kredi_türü.rename(columns = {0:'NPL', 1:'NPL_2'})
    df_2_kredi_türü=df_2_kredi_türü[['Kredi Türü','NPL']]
    df_2_kredi_türü['NPL'] = df_2_kredi_türü['NPL'].round(1)
    df_2_kredi_türü = df_2_kredi_türü.sort_values(by=['NPL'],  ascending=[False])
    

    df_2 = df
    
    # BÖLGE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Bölge'] == input_1]  

   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  


    # ŞUBE FİLTRESİ    
    if input_4 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_4] 


    df_2_ay_NPL = df_2.groupby(['Ay'])['NPL'].sum(),df_2.groupby(['Ay'])['NPL'].count()
    df_2_ay_NPL= pd.DataFrame(list( df_2_ay_NPL))
    df_2_ay_NPL.reset_index(drop=True, inplace=True)
    df_2_ay_NPL=df_2_ay_NPL.T
    df_2_ay_NPL.reset_index(drop=False, inplace=True)
    df_2_ay_NPL=df_2_ay_NPL.rename(columns = {0:'NPL', 1:'NPL_2'})
    df_2_ay_NPL=df_2_ay_NPL[['Ay','NPL']]
    df_2_ay_NPL['NPL'] = df_2_ay_NPL['NPL'].round(1)

    

    df_2 = df
    
    # BÖLGE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Bölge'] == input_1]  

   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  


    # ŞUBE FİLTRESİ    
    if input_4 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_4] 
        

    df_2['Total Loans'] = df_2['Gecikmesiz'] + df_2['Bucket-1'] + df_2['Bucket-2'] + df_2['Bucket-3']
    df_2_ay_PL = df_2.groupby(['Ay'])['Total Loans'].sum(),df_2.groupby(['Ay'])['Total Loans'].count()
    df_2_ay_PL= pd.DataFrame(list( df_2_ay_PL))
    df_2_ay_PL.reset_index(drop=True, inplace=True)
    df_2_ay_PL=df_2_ay_PL.T
    df_2_ay_PL.reset_index(drop=False, inplace=True)
    df_2_ay_PL=df_2_ay_PL.rename(columns = {0:'Total Loans', 1:'Total Loans_2'})
    df_2_ay_PL=df_2_ay_PL[['Ay','Total Loans']]
    df_2_ay_PL['Total Loans'] = df_2_ay_PL['Total Loans'].round(0)

 
    df_2 = df
    

    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  



    
    df_2['Total Loans'] = df_2['Gecikmesiz'] + df_2['Bucket-1'] + df_2['Bucket-2'] + df_2['Bucket-3']
    df_2_bölge_nplpct = df_2.groupby(['Bölge'])['Total Loans'].sum(),df_2.groupby(['Bölge'])['NPL'].sum()
    df_2_bölge_nplpct = pd.DataFrame(list( df_2_bölge_nplpct))
    df_2_bölge_nplpct.reset_index(drop=True, inplace=True)
    df_2_bölge_nplpct = df_2_bölge_nplpct.T
    df_2_bölge_nplpct.reset_index(drop=False, inplace=True)
    df_2_bölge_nplpct = df_2_bölge_nplpct.rename(columns = {0:'Total Loans', 1:'NPL'})
    df_2_bölge_nplpct['NPL Aktarım %'] = df_2_bölge_nplpct['NPL'] / df_2_bölge_nplpct ['Total Loans']
    df_2_bölge_nplpct = df_2_bölge_nplpct[['Bölge','NPL Aktarım %']]
    df_2_bölge_nplpct = df_2_bölge_nplpct.sort_values(by=['NPL Aktarım %'],  ascending=[False])
    df_2_bölge_nplpct['NPL Aktarım %']= ((df_2_bölge_nplpct['NPL Aktarım %'] * 100).round(1)).astype(str) + '%'


    df_2 = df
    
    # BÖLGE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Bölge'] == input_1]  

   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  






    df_2['Total Loans'] = df_2['Gecikmesiz'] + df_2['Bucket-1'] + df_2['Bucket-2'] + df_2['Bucket-3']
    df_2_sube_nplpct = df_2.groupby(['Şube'])['Total Loans'].sum(),df_2.groupby(['Şube'])['NPL'].sum()
    df_2_sube_nplpct = pd.DataFrame(list( df_2_sube_nplpct))
    df_2_sube_nplpct.reset_index(drop=True, inplace=True)
    df_2_sube_nplpct = df_2_sube_nplpct.T
    df_2_sube_nplpct.reset_index(drop=False, inplace=True)
    df_2_sube_nplpct = df_2_sube_nplpct.rename(columns = {0:'Total Loans', 1:'NPL'})
    df_2_sube_nplpct['NPL Aktarım %'] = df_2_sube_nplpct['NPL'] / df_2_sube_nplpct ['Total Loans']
    df_2_sube_nplpct = df_2_sube_nplpct[['Şube','NPL Aktarım %']]
    df_2_sube_nplpct = df_2_sube_nplpct.sort_values(by=['NPL Aktarım %'],  ascending=[False])
    df_2_sube_nplpct['NPL Aktarım %']= ((df_2_sube_nplpct['NPL Aktarım %'] * 100).round(1)).astype(str) + '%'    
    df_2_sube_nplpct = df_2_sube_nplpct.head(5)



    df_2 = df
    
    # BÖLGE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Bölge'] == input_1]  

   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  


    # ŞUBE FİLTRESİ    
    if input_4 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_4] 


    df_2_roll_rate_1 = df_2.groupby(['Ay'])['Gecikmesiz'].sum(),df_2.groupby(['Ay'])['Bucket-1'].sum()
    df_2_roll_rate_1 = pd.DataFrame(list( df_2_roll_rate_1))
    df_2_roll_rate_1.reset_index(drop=True, inplace=True)
    df_2_roll_rate_1 = df_2_roll_rate_1.T
    df_2_roll_rate_1.reset_index(drop=False, inplace=True)
    df_2_roll_rate_1 = df_2_roll_rate_1.rename(columns = {0:'Previous', 1:'Next'})
    df_2_roll_rate_1['Roll Rate %'] = df_2_roll_rate_1['Next'] / df_2_roll_rate_1['Previous']
    df_2_roll_rate_1 = df_2_roll_rate_1[['Ay','Roll Rate %']]
    df_2_roll_rate_1 = df_2_roll_rate_1.sort_values(by=['Ay'],  ascending=[True])
    df_2_roll_rate_1['Roll Rate %']= ((df_2_roll_rate_1['Roll Rate %'] * 100).round(1)).astype(str) + '%'    
    


    df_2 = df
    
    # BÖLGE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Bölge'] == input_1]  

   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  


    # ŞUBE FİLTRESİ    
    if input_4 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_4] 


    df_2_roll_rate_2 = df_2.groupby(['Ay'])['Bucket-1'].sum(),df_2.groupby(['Ay'])['Bucket-2'].sum()
    df_2_roll_rate_2 = pd.DataFrame(list( df_2_roll_rate_2))
    df_2_roll_rate_2.reset_index(drop=True, inplace=True)
    df_2_roll_rate_2 = df_2_roll_rate_2.T
    df_2_roll_rate_2.reset_index(drop=False, inplace=True)
    df_2_roll_rate_2 = df_2_roll_rate_2.rename(columns = {0:'Previous', 1:'Next'})
    df_2_roll_rate_2['Roll Rate %'] = df_2_roll_rate_2['Next'] / df_2_roll_rate_2['Previous']
    df_2_roll_rate_2 = df_2_roll_rate_2[['Ay','Roll Rate %']]
    df_2_roll_rate_2['Roll Rate %']= ((df_2_roll_rate_2['Roll Rate %'] * 100).round(1)).astype(str) + '%'    
    

    df_2 = df
    
    # BÖLGE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Bölge'] == input_1]  

   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  


    # ŞUBE FİLTRESİ    
    if input_4 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_4] 
        
        

    df_2_roll_rate_3 = df_2.groupby(['Ay'])['Bucket-2'].sum(),df_2.groupby(['Ay'])['Bucket-3'].sum()
    df_2_roll_rate_3 = pd.DataFrame(list( df_2_roll_rate_3))
    df_2_roll_rate_3.reset_index(drop=True, inplace=True)
    df_2_roll_rate_3 = df_2_roll_rate_3.T
    df_2_roll_rate_3.reset_index(drop=False, inplace=True)
    df_2_roll_rate_3 = df_2_roll_rate_3.rename(columns = {0:'Previous', 1:'Next'})
    df_2_roll_rate_3['Roll Rate %'] = df_2_roll_rate_3['Next'] / df_2_roll_rate_3['Previous']
    df_2_roll_rate_3 = df_2_roll_rate_3[['Ay','Roll Rate %']]
    df_2_roll_rate_3['Roll Rate %']= ((df_2_roll_rate_3['Roll Rate %'] * 100).round(1)).astype(str) + '%'      
    


    df_2 = df
    
    # BÖLGE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Bölge'] == input_1]  

   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  


    # ŞUBE FİLTRESİ    
    if input_4 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_4] 
        

    df_2_roll_rate_4 = df_2.groupby(['Ay'])['Bucket-3'].sum(),df_2.groupby(['Ay'])['NPL'].sum()
    df_2_roll_rate_4 = pd.DataFrame(list( df_2_roll_rate_4))
    df_2_roll_rate_4.reset_index(drop=True, inplace=True)
    df_2_roll_rate_4 = df_2_roll_rate_4.T
    df_2_roll_rate_4.reset_index(drop=False, inplace=True)
    df_2_roll_rate_4 = df_2_roll_rate_4.rename(columns = {0:'Previous', 1:'Next'})
    df_2_roll_rate_4['Roll Rate %'] = df_2_roll_rate_4['Next'] / df_2_roll_rate_4['Previous']
    df_2_roll_rate_4 = df_2_roll_rate_4[['Ay','Roll Rate %']]
    df_2_roll_rate_4['Roll Rate %']= ((df_2_roll_rate_4['Roll Rate %'] * 100).round(1)).astype(str) + '%'    
    


    df_2 = df
    
    # BÖLGE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Bölge'] == input_1]  

   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  


    # ŞUBE FİLTRESİ    
    if input_4 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_4] 
        

    df_2_roll_rate_5 = df_2.groupby(['Ay'])['Gecikmesiz'].sum(),df_2.groupby(['Ay'])['NPL'].sum()
    df_2_roll_rate_5 = pd.DataFrame(list( df_2_roll_rate_5))
    df_2_roll_rate_5.reset_index(drop=True, inplace=True)
    df_2_roll_rate_5 = df_2_roll_rate_5.T
    df_2_roll_rate_5.reset_index(drop=False, inplace=True)
    df_2_roll_rate_5 = df_2_roll_rate_5.rename(columns = {0:'Previous', 1:'Next'})
    df_2_roll_rate_5['Roll Rate %'] = df_2_roll_rate_5['Next'] / df_2_roll_rate_5['Previous']
    df_2_roll_rate_5 = df_2_roll_rate_5[['Ay','Roll Rate %']]
    df_2_roll_rate_5['Roll Rate %']= ((df_2_roll_rate_5['Roll Rate %'] * 100).round(2)).astype(str) + '%'    



    df_2 = df
    
    # BÖLGE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Bölge'] == input_1]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  


    # ŞUBE FİLTRESİ    
    if input_4 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_4] 


    df_2['Total Loans'] = df_2['Gecikmesiz'] + df_2['Bucket-1'] + df_2['Bucket-2'] + df_2['Bucket-3']
    df_2_kredituru_nplpct = df_2.groupby(['Kredi Türü'])['Total Loans'].sum(),df_2.groupby(['Kredi Türü'])['NPL'].sum()
    df_2_kredituru_nplpct = pd.DataFrame(list( df_2_kredituru_nplpct))
    df_2_kredituru_nplpct.reset_index(drop=True, inplace=True)
    df_2_kredituru_nplpct = df_2_kredituru_nplpct.T
    df_2_kredituru_nplpct.reset_index(drop=False, inplace=True)
    df_2_kredituru_nplpct = df_2_kredituru_nplpct.rename(columns = {0:'Total Loans', 1:'NPL'})
    df_2_kredituru_nplpct['NPL Aktarım %'] = df_2_kredituru_nplpct['NPL'] / df_2_kredituru_nplpct ['Total Loans']
    df_2_kredituru_nplpct = df_2_kredituru_nplpct[['Kredi Türü','NPL Aktarım %']]
    df_2_kredituru_nplpct = df_2_kredituru_nplpct.sort_values(by=['NPL Aktarım %'],  ascending=[False])
    df_2_kredituru_nplpct['NPL Aktarım %']= ((df_2_kredituru_nplpct['NPL Aktarım %'] * 100).round(2)).astype(str) + '%'    

    

    df_2 = df
    
    # BÖLGE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Bölge'] == input_1]  

   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  


    # ŞUBE FİLTRESİ    
    if input_4 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_4] 
 

    df_2['Total Loans'] = df_2['Gecikmesiz'] + df_2['Bucket-1'] + df_2['Bucket-2'] + df_2['Bucket-3']
    df_2_segment_nplpct = df_2.groupby(['Segment'])['Total Loans'].sum(),df_2.groupby(['Segment'])['NPL'].sum()
    df_2_segment_nplpct = pd.DataFrame(list( df_2_segment_nplpct))
    df_2_segment_nplpct.reset_index(drop=True, inplace=True)
    df_2_segment_nplpct = df_2_segment_nplpct.T
    df_2_segment_nplpct.reset_index(drop=False, inplace=True)
    df_2_segment_nplpct = df_2_segment_nplpct.rename(columns = {0:'Total Loans', 1:'NPL'})
    df_2_segment_nplpct['NPL Aktarım %'] = df_2_segment_nplpct['NPL'] / df_2_segment_nplpct['Total Loans']
    df_2_segment_nplpct = df_2_segment_nplpct[['Segment','NPL Aktarım %']]
    df_2_segment_nplpct = df_2_segment_nplpct.sort_values(by=['NPL Aktarım %'],  ascending=[False])
    df_2_segment_nplpct['NPL Aktarım %']= ((df_2_segment_nplpct['NPL Aktarım %'] * 100).round(1)).astype(str) + '%'    
      
    
    
    
    
    #card-output_01_apple
    return html.H1(last_month_NPL, style={"color": "white","background": color_palette_blue[3], 'textAlign': 'center', 'width':'75%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '250%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '-20%', 'margin-left': '25%'}
    
    

    #card-output_01_orange          
          ),html.H1(total_NPL, style={"color": "white","background": color_palette_blue[1], 'textAlign': 'center', 'width':'75%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '250%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '-20%', 'margin-left': '25%'}                              
   

                    
    #graph-output_01_apple          

   ),dcc.Graph(                    
                
                    
                        figure={
                                    'data': [
                                                {'x': (df_2_bölge_nplpct['Bölge'].values.tolist()), 'y': (df_2_bölge_nplpct['NPL Aktarım %'].values.tolist()), 'type': 'bar', 'name': df_2_bölge_nplpct['Bölge'].values.tolist(), 'marker' : {'color': color_palette_heatmap_pale_10},'text' : df_2_bölge_nplpct['NPL Aktarım %'],'textposition':'outside', 'textfont':{'color':'auto'},'hoverinfo' : 'x+text','cliponaxis': False}
                                            ],
                                    'layout':   {
                                                    'height' : 225,
                                                    #'width' : 600,
                                                    'title': ' Bölge Bazında Aylık NPL Dönüşüm Oranı', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': df_2_bölge_nplpct['Bölge'], 'ticktext': df_2_bölge_nplpct['Bölge']},
                                                    'margin' : {'l': 0,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                    
                                                }
                                }
 
              
    #graph-output_01_orange
    ),dcc.Graph(



                        figure={
                                    'data': [
                                                {'x': (df_2_ay_NPL['Ay'].values.tolist()), 'y': (df_2_ay_NPL['NPL'].values.tolist()), 'type': 'bar', 'name': df_2_ay_NPL['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_ay_NPL['NPL'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'x+text'}
                                            ],
                                    'layout':   {
                                                    'height' : 225,
                                                    #'width' : 600,
                                                    'title': ' Aylık NPL Aktarımları (M TL)', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': df_2_ay_NPL['Ay'], 'ticktext': df_2_ay_NPL['Ay']},
                                                    'margin' : {'l': 40,'r': 00,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }
              
    #graph-output_01_banana
    ),dcc.Graph(

                        figure={
                                    'data': [
                                                {'x': (df_2_sube_nplpct['Şube'].values.tolist()), 'y': (df_2_sube_nplpct['NPL Aktarım %'].values.tolist()), 'type': 'bar', 'name': df_2_sube_nplpct['Şube'].values.tolist(), 'marker' : {'color': color_palette_heatmap_pale_10[0]},'text' : df_2_sube_nplpct['NPL Aktarım %'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'x+text'}
                                            ],
                                    'layout':   {
                                                    'height' : 225,
                                                    #'width' : 600,
                                                    'title': ' Şube Bazında Aylık NPL Dönüşüm Oranı (İlk 5 Şube)', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': df_2_sube_nplpct['Şube'], 'ticktext': df_2_sube_nplpct['Şube']},
                                                    'margin' : {'l': 0,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                } 
 
              
    #graph-output_01_lemon
    ),dcc.Graph(


                        figure={
                                    'data': [
                                                {'x': (df_2_ay_PL['Ay'].values.tolist()), 'y': (df_2_ay_PL['Total Loans'].values.tolist()), 'type': 'bar', 'name': df_2_ay_PL['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_ay_PL['Total Loans'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'x+text'}
                                            ],
                                    'layout':   {
                                                    'height' : 225,
                                                    #'width' : 600,
                                                    'title': ' Kredi Plasmanının Gelişimi (M TL)', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': df_2_ay_PL['Ay'], 'ticktext': df_2_ay_PL['Ay']},
                                                    'margin' : {'l': 40,'r': 00,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                } 
              
    #graph-output_01_cherry
    ),dcc.Graph(


 
        figure = px.area(
                            df_2_kredi_türü, 
                            x="Kredi Türü", 
                            y="NPL",  
                            title=" Kredi Türü Bazında NPL Aktarımları (M TL)", 
                            height = 225,
                            #width = 475,
                            text = 'NPL'
                            ).update_layout(
                                    title = {'pad':{'l':100}},
                                    paper_bgcolor = 'rgba(0,0,0,0)',
                                    plot_bgcolor = 'rgba(0,0,0,0)',
                                    margin={"r":40,"t":40,"l":0,"b":70},
                                    yaxis = {'title': None,'showgrid' : False, 'showline' : False, 'showticklabels' : False},
                                    xaxis = {'title': None,'showgrid' : False}
                                    ).update_traces(
                                                    #hovertemplate = df_2_kredi_türü["Kredi Türü"]+ ' : ' + df_2_kredi_türü["NPL"],
                                                    textposition ='top center',
                                                    cliponaxis = False,
                                                    line_color = color_palette_blue[0]
                                                    )  
                                        
    #graph-output_01_apricot_1
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'y': (df_2_roll_rate_1['Ay'].values.tolist()), 'x': (df_2_roll_rate_1['Roll Rate %'].values.tolist()), 'type': 'bar', 'name': df_2_roll_rate_1['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_roll_rate_1['Roll Rate %'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'text', 'hoverlabel':{'font':{'size':12}} ,'orientation': 'h'}
                                            ],
                                    'layout':   {
                                                    'height' : 495,
                                                    'width' : 250,
                                                    'title': ' Bucket-1', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'yaxis': {'showgrid' : False, 'showline' : True, 'showticklabels' : True, 'tickvals': df_2_roll_rate_1['Ay'], 'ticktext': df_2_roll_rate_1['Ay']},
                                                    'margin' : {'l': 50,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_01_apricot_2
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'y': (df_2_roll_rate_2['Ay'].values.tolist()), 'x': (df_2_roll_rate_2['Roll Rate %'].values.tolist()), 'type': 'bar', 'name': df_2_roll_rate_2['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_roll_rate_2['Roll Rate %'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'text', 'hoverlabel':{'font':{'size':12}} ,'orientation': 'h'}
                                            ],
                                    'layout':   {
                                                    'height' : 495,
                                                    'width' : 250,
                                                    'title': ' Bucket-2', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'yaxis': {'showgrid' : False, 'showline' : True, 'showticklabels' : False, 'tickvals': df_2_roll_rate_2['Ay'], 'ticktext': df_2_roll_rate_2['Ay']},
                                                    'margin' : {'l': 50,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_01_apricot_3
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'y': (df_2_roll_rate_3['Ay'].values.tolist()), 'x': (df_2_roll_rate_3['Roll Rate %'].values.tolist()), 'type': 'bar', 'name': df_2_roll_rate_3['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_roll_rate_3['Roll Rate %'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'text', 'hoverlabel':{'font':{'size':12}} ,'orientation': 'h'}
                                            ],
                                    'layout':   {
                                                    'height' : 495,
                                                    'width' : 250,
                                                    'title': ' Bucket-3', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'yaxis': {'showgrid' : False, 'showline' : True, 'showticklabels' : False, 'tickvals': df_2_roll_rate_3['Ay'], 'ticktext': df_2_roll_rate_3['Ay']},
                                                    'margin' : {'l': 50,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_01_apricot_4
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'y': (df_2_roll_rate_4['Ay'].values.tolist()), 'x': (df_2_roll_rate_4['Roll Rate %'].values.tolist()), 'type': 'bar', 'name': df_2_roll_rate_4['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_roll_rate_4['Roll Rate %'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'text', 'hoverlabel':{'font':{'size':12}} ,'orientation': 'h'}
                                            ],
                                    'layout':   {
                                                    'height' : 495,
                                                    'width' : 250,
                                                    'title': ' NPL', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'yaxis': {'showgrid' : False, 'showline' : True, 'showticklabels' : False, 'tickvals': df_2_roll_rate_4['Ay'], 'ticktext': df_2_roll_rate_4['Ay']},
                                                    'margin' : {'l': 50,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_01_apricot_5
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'y': (df_2_roll_rate_5['Ay'].values.tolist()), 'x': (df_2_roll_rate_5['Roll Rate %'].values.tolist()), 'type': 'bar', 'name': df_2_roll_rate_5['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_roll_rate_5['Roll Rate %'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'text', 'hoverlabel':{'font':{'size':12}} ,'orientation': 'h'}
                                            ],
                                    'layout':   {
                                                    'height' : 495,
                                                    'width' : 250,
                                                    'title': ' Aylık NPL Dönüşüm %', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'yaxis': {'showgrid' : False, 'showline' : True, 'showticklabels' : False, 'tickvals': df_2_roll_rate_5['Ay'], 'ticktext': df_2_roll_rate_5['Ay']},
                                                    'margin' : {'l': 50,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_01_mango
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'x': (df_2_kredituru_nplpct['Kredi Türü'].values.tolist()), 'y': (df_2_kredituru_nplpct['NPL Aktarım %'].values.tolist()), 'type': 'bar', 'name': df_2_kredituru_nplpct['Kredi Türü'].values.tolist(), 'marker' : {'color': color_palette_heatmap_pale_6},'text' : df_2_kredituru_nplpct['NPL Aktarım %'],'textposition':'outside', 'textfont':{'color':'auto'},'hoverinfo' : 'x+text','cliponaxis': False}
                                            ],
                                    'layout':   {
                                                    'height' : 275,
                                                    #'width' : 600,
                                                    'title': ' Kredi Türü Bazında Aylık NPL Dönüşüm Oranı', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': df_2_kredituru_nplpct['Kredi Türü'], 'ticktext': df_2_kredituru_nplpct['Kredi Türü']},
                                                    'margin' : {'l': 40,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_01_coconut
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'x': (df_2_segment_nplpct['Segment'].values.tolist()), 'y': (df_2_segment_nplpct['NPL Aktarım %'].values.tolist()), 'type': 'bar', 'name': df_2_segment_nplpct['Segment'].values.tolist(), 'marker' : {'color': color_palette_heatmap_pale_3},'text' : df_2_segment_nplpct['NPL Aktarım %'],'textposition':'outside', 'textfont':{'color':'auto'},'hoverinfo' : 'x+text','cliponaxis': False}
                                            ],
                                    'layout':   {
                                                    'height' : 275,
                                                    #'width' : 600,
                                                    'title': ' Segment Bazında Aylık NPL Dönüşüm Oranı', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': df_2_segment_nplpct['Segment'], 'ticktext': df_2_segment_nplpct['Segment']},
                                                    'margin' : {'l': 10,'r': 40,'t': 70,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    
    )
    




#tab-2 callback begins here
@app.callback([Output('card-output_02_apple', 'children'),Output('card-output_02_orange', 'children'),Output('card-output_02_banana', 'children'),Output('graph-output_02_apple', 'children'),Output('graph-output_02_orange', 'children'),Output('graph-output_02_banana', 'children'),Output('graph-output_02_lemon', 'children'),Output('graph-output_02_cherry', 'children'),Output('graph-output_02_apricot', 'children')],
              [Input('Bölge_Filtresi_tab2', 'value'),
              Input('Kredi Türü_Filtresi_tab2', 'value'),
              Input('Şube_Filtresi_tab2', 'value'),
              Input('Tahsilat_Ofisi_Filtresi_tab2', 'value')
               ]) 


def update_value_2(input_1, input_2, input_3, input_4):
    
        df_2 = df


        # BÖLGE FİLTRESİ    
        if input_1 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Bölge'] == input_1]  
    
       
        
        # KREDİ TÜRÜ FİLTRESİ    
        if input_2 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Kredi Türü'] == input_2]  
    

    
    
        # ŞUBE FİLTRESİ    
        if input_3 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Şube'] == input_3] 
    
    
    
        # TAHSİLAT OFİSİ FİLTRESİ    
        if input_4 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Tahsilat Ofisi'] == input_4]
    
    
    
        last_month_recovery = df_2[df_2['Ay_2'] == max(df_2['Ay_2'])]
        last_month_recovery = round(sum(last_month_recovery['Tahsilat-12']),1)

    
    
        df_2 = df
        
        # BÖLGE FİLTRESİ    
        if input_1 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Bölge'] == input_1]  
    
       
        
        # KREDİ TÜRÜ FİLTRESİ    
        if input_2 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Kredi Türü'] == input_2]  
    
       

        # ŞUBE FİLTRESİ    
        if input_3 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Şube'] == input_3] 



        # TAHSİLAT OFİSİ FİLTRESİ    
        if input_4 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Tahsilat Ofisi'] == input_4]
            
            
            
    
    
        total_recovery = round(sum(df_2['Tahsilat-12']),1)                                                                           

        total_recovery_pct = sum(df_2['Tahsilat-12'])/sum(df_2['NPL'])
        total_recovery_pct = str(round(total_recovery_pct * 100,1))+'%'
        

        df_2 = df


        # BÖLGE FİLTRESİ    
        if input_1 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Bölge'] == input_1]  
    
       
        
        # KREDİ TÜRÜ FİLTRESİ    
        if input_2 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Kredi Türü'] == input_2]  
    
       
    
        # ŞUBE FİLTRESİ    
        if input_3 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Şube'] == input_3] 



        # TAHSİLAT OFİSİ FİLTRESİ    
        if input_4 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Tahsilat Ofisi'] == input_4]



        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2['Tahsilat-1']),sum(df_2['Tahsilat-2']),sum(df_2['Tahsilat-3']),sum(df_2['Tahsilat-4']),sum(df_2['Tahsilat-5']),sum(df_2['Tahsilat-6']),sum(df_2['Tahsilat-7']),sum(df_2['Tahsilat-8']),sum(df_2['Tahsilat-9']),sum(df_2['Tahsilat-10']),sum(df_2['Tahsilat-11']),sum(df_2['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'    
        recovery_vintage_all = recovery_vintage




        df_2 = df

        
        # KREDİ TÜRÜ FİLTRESİ    
        if input_2 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Kredi Türü'] == input_2]  
    
       
 

        # TAHSİLAT OFİSİ FİLTRESİ    
        if input_4 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Tahsilat Ofisi'] == input_4]    

    
    
    
        bolge_recovery_pct = df_2.groupby(['Bölge'])['NPL'].sum(),df_2.groupby(['Bölge'])['Tahsilat-12'].sum()
        bolge_recovery_pct = pd.DataFrame(list( bolge_recovery_pct))
        bolge_recovery_pct.reset_index(drop=True, inplace=True)
        bolge_recovery_pct = bolge_recovery_pct.T
        bolge_recovery_pct.reset_index(drop=False, inplace=True)
        bolge_recovery_pct = bolge_recovery_pct.rename(columns = {0:'NPL', 1:'Recovery'})
        bolge_recovery_pct['12. Ay NPL Tahsilat %'] = bolge_recovery_pct['Recovery'] / bolge_recovery_pct['NPL']
        bolge_recovery_pct = bolge_recovery_pct[['Bölge','12. Ay NPL Tahsilat %']]
        bolge_recovery_pct = bolge_recovery_pct.sort_values(by=['12. Ay NPL Tahsilat %'],  ascending=[False])
        bolge_recovery_pct['12. Ay NPL Tahsilat %']= ((bolge_recovery_pct['12. Ay NPL Tahsilat %'] * 100).round(1)).astype(str) + '%'    
        






        df_2 = df


        # BÖLGE FİLTRESİ    
        if input_1 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Bölge'] == input_1]  
    
       
        
        # KREDİ TÜRÜ FİLTRESİ    
        if input_2 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Kredi Türü'] == input_2]  
    

    
        # ŞUBE FİLTRESİ    
        if input_3 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Şube'] == input_3] 



        # TAHSİLAT OFİSİ FİLTRESİ    
        if input_4 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Tahsilat Ofisi'] == input_4]
        
        
        
        
        df_2_bireysel_kitle = df_2[df_2['Segment'] == 'Bireysel Kitle']
        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2_bireysel_kitle['Tahsilat-1']),sum(df_2_bireysel_kitle['Tahsilat-2']),sum(df_2_bireysel_kitle['Tahsilat-3']),sum(df_2_bireysel_kitle['Tahsilat-4']),sum(df_2_bireysel_kitle['Tahsilat-5']),sum(df_2_bireysel_kitle['Tahsilat-6']),sum(df_2_bireysel_kitle['Tahsilat-7']),sum(df_2_bireysel_kitle['Tahsilat-8']),sum(df_2_bireysel_kitle['Tahsilat-9']),sum(df_2_bireysel_kitle['Tahsilat-10']),sum(df_2_bireysel_kitle['Tahsilat-11']),sum(df_2_bireysel_kitle['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2_bireysel_kitle['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'
        recovery_vintage['Segment'] = 'Bireysel Kitle'  
        df_2_bireysel_kitle = recovery_vintage
        df_2_bireysel_kitle = df_2_bireysel_kitle[(df_2_bireysel_kitle['Ay'] == 3) | (df_2_bireysel_kitle['Ay'] == 6) | (df_2_bireysel_kitle['Ay'] == 9) | (df_2_bireysel_kitle['Ay'] == 12)]
        
        
        
        
        df_2_bireysel_portfoy = df_2[df_2['Segment'] == 'Bireysel Portföy']
        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2_bireysel_portfoy['Tahsilat-1']),sum(df_2_bireysel_portfoy['Tahsilat-2']),sum(df_2_bireysel_portfoy['Tahsilat-3']),sum(df_2_bireysel_portfoy['Tahsilat-4']),sum(df_2_bireysel_portfoy['Tahsilat-5']),sum(df_2_bireysel_portfoy['Tahsilat-6']),sum(df_2_bireysel_portfoy['Tahsilat-7']),sum(df_2_bireysel_portfoy['Tahsilat-8']),sum(df_2_bireysel_portfoy['Tahsilat-9']),sum(df_2_bireysel_portfoy['Tahsilat-10']),sum(df_2_bireysel_portfoy['Tahsilat-11']),sum(df_2_bireysel_portfoy['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2_bireysel_portfoy['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'
        recovery_vintage['Segment'] = 'Bireysel Portföy'  
        df_2_bireysel_portfoy = recovery_vintage
        df_2_bireysel_portfoy = df_2_bireysel_portfoy[(df_2_bireysel_portfoy['Ay'] == 3) | (df_2_bireysel_portfoy['Ay'] == 6) | (df_2_bireysel_portfoy['Ay'] == 9) | (df_2_bireysel_portfoy['Ay'] == 12)]
        
        
        
        df_2_ozel_birikim = df_2[df_2['Segment'] == 'Özel Birikim']
        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2_ozel_birikim['Tahsilat-1']),sum(df_2_ozel_birikim['Tahsilat-2']),sum(df_2_ozel_birikim['Tahsilat-3']),sum(df_2_ozel_birikim['Tahsilat-4']),sum(df_2_ozel_birikim['Tahsilat-5']),sum(df_2_ozel_birikim['Tahsilat-6']),sum(df_2_ozel_birikim['Tahsilat-7']),sum(df_2_ozel_birikim['Tahsilat-8']),sum(df_2_ozel_birikim['Tahsilat-9']),sum(df_2_ozel_birikim['Tahsilat-10']),sum(df_2_ozel_birikim['Tahsilat-11']),sum(df_2_ozel_birikim['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2_ozel_birikim['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'
        recovery_vintage['Segment'] = 'Özel Birikim'  
        df_2_ozel_birikim = recovery_vintage
        df_2_ozel_birikim = df_2_ozel_birikim[(df_2_ozel_birikim['Ay'] == 3) | (df_2_ozel_birikim['Ay'] == 6) | (df_2_ozel_birikim['Ay'] == 9) | (df_2_ozel_birikim['Ay'] == 12)]
        
        
        
        df_2_segment_recovery = df_2_bireysel_kitle.append([df_2_bireysel_portfoy,df_2_ozel_birikim])
        df_2_segment_recovery_3_ay_tahsilat = df_2_segment_recovery[df_2_segment_recovery['Ay']==3]
        df_2_segment_recovery_6_ay_tahsilat = df_2_segment_recovery[df_2_segment_recovery['Ay']==6]
        df_2_segment_recovery_9_ay_tahsilat = df_2_segment_recovery[df_2_segment_recovery['Ay']==9]
        df_2_segment_recovery_12_ay_tahsilat = df_2_segment_recovery[df_2_segment_recovery['Ay']==12]










        df_2 = df
        
        # BÖLGE FİLTRESİ    
        if input_1 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Bölge'] == input_1]  
    
       
        
        # KREDİ TÜRÜ FİLTRESİ    
        if input_2 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Kredi Türü'] == input_2]  
    

        # ŞUBE FİLTRESİ    
        if input_3 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Şube'] == input_3] 




        ofis_recovery_pct = df_2.groupby(['Tahsilat Ofisi'])['NPL'].sum(),df_2.groupby(['Tahsilat Ofisi'])['Tahsilat-12'].sum()
        ofis_recovery_pct = pd.DataFrame(list( ofis_recovery_pct))
        ofis_recovery_pct.reset_index(drop=True, inplace=True)
        ofis_recovery_pct = ofis_recovery_pct.T
        ofis_recovery_pct.reset_index(drop=False, inplace=True)
        ofis_recovery_pct = ofis_recovery_pct.rename(columns = {0:'NPL', 1:'Recovery'})
        ofis_recovery_pct['12. Ay NPL Tahsilat %'] = ofis_recovery_pct['Recovery'] / ofis_recovery_pct['NPL']
        ofis_recovery_pct = ofis_recovery_pct[['Tahsilat Ofisi','12. Ay NPL Tahsilat %']]
        ofis_recovery_pct = ofis_recovery_pct.sort_values(by=['12. Ay NPL Tahsilat %'],  ascending=[False])
        ofis_recovery_pct['12. Ay NPL Tahsilat %']= ((ofis_recovery_pct['12. Ay NPL Tahsilat %'] * 100).round(1)).astype(str) + '%'        
  
        
        


        df_2 = df
        
        # BÖLGE FİLTRESİ    
        if input_1 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Bölge'] == input_1]  
    
       
        
        # KREDİ TÜRÜ FİLTRESİ    
        if input_2 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Kredi Türü'] == input_2]  
    


        # TAHSİLAT OFİSİ FİLTRESİ    
        if input_4 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Tahsilat Ofisi'] == input_4]




        sube_recovery_pct = df_2.groupby(['Şube'])['NPL'].sum(),df_2.groupby(['Şube'])['Tahsilat-12'].sum()
        sube_recovery_pct = pd.DataFrame(list( sube_recovery_pct))
        sube_recovery_pct.reset_index(drop=True, inplace=True)
        sube_recovery_pct = sube_recovery_pct.T
        sube_recovery_pct.reset_index(drop=False, inplace=True)
        sube_recovery_pct = sube_recovery_pct.rename(columns = {0:'NPL', 1:'Recovery'})
        sube_recovery_pct['12. Ay NPL Tahsilat %'] = sube_recovery_pct['Recovery'] / sube_recovery_pct['NPL']
        sube_recovery_pct = sube_recovery_pct[['Şube','12. Ay NPL Tahsilat %']]
        sube_recovery_pct = sube_recovery_pct.sort_values(by=['12. Ay NPL Tahsilat %'],  ascending=[False])
        sube_recovery_pct['12. Ay NPL Tahsilat %']= ((sube_recovery_pct['12. Ay NPL Tahsilat %'] * 100).round(1)).astype(str) + '%'        
        sube_recovery_pct = sube_recovery_pct.head(5)
        sube_recovery_pct  
        
        
        


        df_2 = df


        # BÖLGE FİLTRESİ    
        if input_1 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Bölge'] == input_1]  
    
       
    
        # ŞUBE FİLTRESİ    
        if input_3 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Şube'] == input_3] 



        # TAHSİLAT OFİSİ FİLTRESİ    
        if input_4 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Tahsilat Ofisi'] == input_4]        
        
        
        

        
        
        df_2_yapılandırma = df_2[df_2['Kredi Türü'] == 'Yapılandırma']
        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2_yapılandırma['Tahsilat-1']),sum(df_2_yapılandırma['Tahsilat-2']),sum(df_2_yapılandırma['Tahsilat-3']),sum(df_2_yapılandırma['Tahsilat-4']),sum(df_2_yapılandırma['Tahsilat-5']),sum(df_2_yapılandırma['Tahsilat-6']),sum(df_2_yapılandırma['Tahsilat-7']),sum(df_2_yapılandırma['Tahsilat-8']),sum(df_2_yapılandırma['Tahsilat-9']),sum(df_2_yapılandırma['Tahsilat-10']),sum(df_2_yapılandırma['Tahsilat-11']),sum(df_2_yapılandırma['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2_yapılandırma['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'
        recovery_vintage['Kredi Türü'] = 'Yapılandırma'  
        df_2_yapılandırma = recovery_vintage
        df_2_yapılandırma = df_2_yapılandırma[(df_2_yapılandırma['Ay'] == 3) | (df_2_yapılandırma['Ay'] == 6) | (df_2_yapılandırma['Ay'] == 9) | (df_2_yapılandırma['Ay'] == 12)]
                    
        
        
        
        df_2_kmh = df_2[df_2['Kredi Türü'] == 'KMH']
        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2_kmh['Tahsilat-1']),sum(df_2_kmh['Tahsilat-2']),sum(df_2_kmh['Tahsilat-3']),sum(df_2_kmh['Tahsilat-4']),sum(df_2_kmh['Tahsilat-5']),sum(df_2_kmh['Tahsilat-6']),sum(df_2_kmh['Tahsilat-7']),sum(df_2_kmh['Tahsilat-8']),sum(df_2_kmh['Tahsilat-9']),sum(df_2_kmh['Tahsilat-10']),sum(df_2_kmh['Tahsilat-11']),sum(df_2_kmh['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2_kmh['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'
        recovery_vintage['Kredi Türü'] = 'KMH'  
        df_2_kmh = recovery_vintage
        df_2_kmh = df_2_kmh[(df_2_kmh['Ay'] == 3) | (df_2_kmh['Ay'] == 6) | (df_2_kmh['Ay'] == 9) | (df_2_kmh['Ay'] == 12)]
        
        
        
        
        df_2_kredi_kartı = df_2[df_2['Kredi Türü'] == 'Kredi Kartı']
        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2_kredi_kartı['Tahsilat-1']),sum(df_2_kredi_kartı['Tahsilat-2']),sum(df_2_kredi_kartı['Tahsilat-3']),sum(df_2_kredi_kartı['Tahsilat-4']),sum(df_2_kredi_kartı['Tahsilat-5']),sum(df_2_kredi_kartı['Tahsilat-6']),sum(df_2_kredi_kartı['Tahsilat-7']),sum(df_2_kredi_kartı['Tahsilat-8']),sum(df_2_kredi_kartı['Tahsilat-9']),sum(df_2_kredi_kartı['Tahsilat-10']),sum(df_2_kredi_kartı['Tahsilat-11']),sum(df_2_kredi_kartı['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2_kredi_kartı['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'
        recovery_vintage['Kredi Türü'] = 'Kredi Kartı'  
        df_2_kredi_kartı = recovery_vintage
        df_2_kredi_kartı = df_2_kredi_kartı[(df_2_kredi_kartı['Ay'] == 3) | (df_2_kredi_kartı['Ay'] == 6) | (df_2_kredi_kartı['Ay'] == 9) | (df_2_kredi_kartı['Ay'] == 12)]
        
        
        
        df_2_kredi_ihtiyac = df_2[df_2['Kredi Türü'] == 'İhtiyaç']
        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2_kredi_ihtiyac['Tahsilat-1']),sum(df_2_kredi_ihtiyac['Tahsilat-2']),sum(df_2_kredi_ihtiyac['Tahsilat-3']),sum(df_2_kredi_ihtiyac['Tahsilat-4']),sum(df_2_kredi_ihtiyac['Tahsilat-5']),sum(df_2_kredi_ihtiyac['Tahsilat-6']),sum(df_2_kredi_ihtiyac['Tahsilat-7']),sum(df_2_kredi_ihtiyac['Tahsilat-8']),sum(df_2_kredi_ihtiyac['Tahsilat-9']),sum(df_2_kredi_ihtiyac['Tahsilat-10']),sum(df_2_kredi_ihtiyac['Tahsilat-11']),sum(df_2_kredi_ihtiyac['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2_kredi_ihtiyac['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'
        recovery_vintage['Kredi Türü'] = 'İhtiyaç'  
        df_2_kredi_ihtiyac = recovery_vintage
        df_2_kredi_ihtiyac = df_2_kredi_ihtiyac[(df_2_kredi_ihtiyac['Ay'] == 3) | (df_2_kredi_ihtiyac['Ay'] == 6) | (df_2_kredi_ihtiyac['Ay'] == 9) | (df_2_kredi_ihtiyac['Ay'] == 12)]
        
        
        
        
        
        df_2_kredi_tasit = df_2[df_2['Kredi Türü'] == 'Taşıt']
        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2_kredi_tasit['Tahsilat-1']),sum(df_2_kredi_tasit['Tahsilat-2']),sum(df_2_kredi_tasit['Tahsilat-3']),sum(df_2_kredi_tasit['Tahsilat-4']),sum(df_2_kredi_tasit['Tahsilat-5']),sum(df_2_kredi_tasit['Tahsilat-6']),sum(df_2_kredi_tasit['Tahsilat-7']),sum(df_2_kredi_tasit['Tahsilat-8']),sum(df_2_kredi_tasit['Tahsilat-9']),sum(df_2_kredi_tasit['Tahsilat-10']),sum(df_2_kredi_tasit['Tahsilat-11']),sum(df_2_kredi_tasit['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2_kredi_tasit['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'
        recovery_vintage['Kredi Türü'] = 'Taşıt'  
        df_2_kredi_tasit = recovery_vintage
        df_2_kredi_tasit = df_2_kredi_tasit[(df_2_kredi_tasit['Ay'] == 3) | (df_2_kredi_tasit['Ay'] == 6) | (df_2_kredi_tasit['Ay'] == 9) | (df_2_kredi_tasit['Ay'] == 12)]
        
        
        
        
        df_2_kredi_konut = df_2[df_2['Kredi Türü'] == 'Konut']
        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2_kredi_konut['Tahsilat-1']),sum(df_2_kredi_konut['Tahsilat-2']),sum(df_2_kredi_konut['Tahsilat-3']),sum(df_2_kredi_konut['Tahsilat-4']),sum(df_2_kredi_konut['Tahsilat-5']),sum(df_2_kredi_konut['Tahsilat-6']),sum(df_2_kredi_konut['Tahsilat-7']),sum(df_2_kredi_konut['Tahsilat-8']),sum(df_2_kredi_konut['Tahsilat-9']),sum(df_2_kredi_konut['Tahsilat-10']),sum(df_2_kredi_konut['Tahsilat-11']),sum(df_2_kredi_konut['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2_kredi_konut['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'
        recovery_vintage['Kredi Türü'] = 'Konut'  
        df_2_kredi_konut = recovery_vintage
        df_2_kredi_konut = df_2_kredi_konut[(df_2_kredi_konut['Ay'] == 3) | (df_2_kredi_konut['Ay'] == 6) | (df_2_kredi_konut['Ay'] == 9) | (df_2_kredi_konut['Ay'] == 12)]
        
        
        
        
        
        df_2_kredi_turu_recovery = df_2_yapılandırma.append([df_2_kmh,df_2_kredi_kartı,df_2_kredi_ihtiyac,df_2_kredi_tasit,df_2_kredi_konut])

        
        df_2_kredi_turu_recovery_3_ay_tahsilat = df_2_kredi_turu_recovery[df_2_kredi_turu_recovery['Ay']==3]
        df_2_kredi_turu_recovery_6_ay_tahsilat = df_2_kredi_turu_recovery[df_2_kredi_turu_recovery['Ay']==6]
        df_2_kredi_turu_recovery_9_ay_tahsilat = df_2_kredi_turu_recovery[df_2_kredi_turu_recovery['Ay']==9]
        df_2_kredi_turu_recovery_12_ay_tahsilat = df_2_kredi_turu_recovery[df_2_kredi_turu_recovery['Ay']==12]
            
                
                
                
        
        
        
        
        
        
        
        

        #card-output_02_apple
        return html.H1(last_month_recovery, style={"color": "white","background": color_palette_blue[3], 'textAlign': 'center', 'width':'75%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '250%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '-20%', 'margin-left': '25%'}
        
        
    
        #card-output_02_orange          
              ),html.H1(total_recovery, style={"color": "white","background": color_palette_blue[1], 'textAlign': 'center', 'width':'75%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '250%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '-20%', 'margin-left': '25%'}                              
       


        #card-output_02_banana          
              ),html.H1(total_recovery_pct, style={"color": "white","background": color_palette_blue[0], 'textAlign': 'center', 'width':'75%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '250%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '-20%', 'margin-left': '25%'}                              
       


            ),dcc.Graph(

                
               
                        figure={
                                    'data': [
                                                {'x': (bolge_recovery_pct['Bölge'].values.tolist()), 'y': (bolge_recovery_pct['12. Ay NPL Tahsilat %'].values.tolist()), 'type': 'bar', 'name': bolge_recovery_pct['Bölge'].values.tolist(), 'marker' : {'color': color_palette_heatmap_pale_10_descending},'text' : bolge_recovery_pct['12. Ay NPL Tahsilat %'],'textposition':'outside', 'textfont':{'color':'auto'},'hoverinfo' : 'x+text', 'cliponaxis': False}
                                            ],
                                    'layout':   {
                                                    'height' : 325,
                                                    #'width' : 700,
                                                    'title': ' Bölge Bazında 12. Ay NPL Tahsilat Oranı (%)', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': bolge_recovery_pct['Bölge'], 'ticktext': bolge_recovery_pct['Bölge']},
                                                    'margin' : {'l': 10,'r': 60,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }                
                
                




            #graph-output_02_apple
            ),dcc.Graph(


                        figure={
                                    'data': [
                                                {'x': (df_2_segment_recovery_3_ay_tahsilat['Segment'].values.tolist()), 'y': (df_2_segment_recovery_3_ay_tahsilat['Tahsilat%'].values.tolist()), 'type': 'bar', 'name': '3. Ay', 'marker' : {'color': color_palette_blue[0]},'text' : df_2_segment_recovery_3_ay_tahsilat['Tahsilat%%'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'name+text'},
                                                {'x': (df_2_segment_recovery_6_ay_tahsilat['Segment'].values.tolist()), 'y': (df_2_segment_recovery_6_ay_tahsilat['Tahsilat%'].values.tolist()), 'type': 'bar', 'name': '6. Ay', 'marker' : {'color': color_palette_blue[1]},'text' : df_2_segment_recovery_6_ay_tahsilat['Tahsilat%%'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'name+text'},
                                                {'x': (df_2_segment_recovery_9_ay_tahsilat['Segment'].values.tolist()), 'y': (df_2_segment_recovery_9_ay_tahsilat['Tahsilat%'].values.tolist()), 'type': 'bar', 'name': '9. Ay', 'marker' : {'color': color_palette_blue[2]},'text' : df_2_segment_recovery_9_ay_tahsilat['Tahsilat%%'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'name+text'},
                                                {'x': (df_2_segment_recovery_12_ay_tahsilat['Segment'].values.tolist()), 'y': (df_2_segment_recovery_12_ay_tahsilat['Tahsilat%'].values.tolist()), 'type': 'bar', 'name': '12. Ay', 'marker' : {'color': color_palette_blue[3]},'text' : df_2_segment_recovery_12_ay_tahsilat['Tahsilat%%'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'name+text'},
                                            ],
                                    'layout':   {
                                                    'height' : 275,
                                                    #'width' : 1100,
                                                    'title': ' Segment Bazında İlk 3-6-9-12 Ay NPL Tahsilat %', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': df_2_segment_recovery_3_ay_tahsilat['Segment'], 'ticktext': df_2_segment_recovery_3_ay_tahsilat['Segment']},
                                                    'margin' : {'l': 40,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }
                        
            #graph-output_02_orange              
            ),dcc.Graph(
                        

                        figure = px.area(
                            recovery_vintage_all, 
                            x="Ay", 
                            y="Tahsilat%",  
                            title=" NPL Tahsilat Vintage Eğrisi", 
                            height = 275,
                            #width = 600,
                            text = 'Tahsilat%%'
                            ).update_layout(
                                    title = {'pad':{'l':185}},
                                    paper_bgcolor = 'rgba(0,0,0,0)',
                                    plot_bgcolor = 'rgba(0,0,0,0)',
                                    margin={"r":40,"t":40,"l":90,"b":40},
                                    yaxis = {'title': None,'showgrid' : False, 'showline' : True, 'showticklabels' : False,'tickformat': ',.0%', 'linecolor': '#E5E8E8'},
                                    xaxis = {'title': 'Takipte Geçen Süre (Ay)','showgrid' : False, 'showline' : False, 'linecolor': '#99A3A4'}
                                    ).update_traces(
                                                    hovertemplate = '%{x}. Ay: %{text}',
                                                    textposition ='top center',
                                                    cliponaxis = False,
                                                    line_color = color_palette_blue[0]
                                                    )                        

            #graph-output_02_banana
            ),dcc.Graph(
                

                        figure={
                                    'data': [
                                                {'x': (df_2_kredi_turu_recovery_3_ay_tahsilat['Kredi Türü'].values.tolist()), 'y': (df_2_kredi_turu_recovery_3_ay_tahsilat['Tahsilat%'].values.tolist()), 'type': 'bar', 'name': '3. Ay', 'marker' : {'color': color_palette_blue[0]},'text' : df_2_kredi_turu_recovery_3_ay_tahsilat['Tahsilat%%'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'name+text'},
                                                {'x': (df_2_kredi_turu_recovery_6_ay_tahsilat['Kredi Türü'].values.tolist()), 'y': (df_2_kredi_turu_recovery_6_ay_tahsilat['Tahsilat%'].values.tolist()), 'type': 'bar', 'name': '6. Ay', 'marker' : {'color': color_palette_blue[1]},'text' : df_2_kredi_turu_recovery_6_ay_tahsilat['Tahsilat%%'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'name+text'},
                                                {'x': (df_2_kredi_turu_recovery_9_ay_tahsilat['Kredi Türü'].values.tolist()), 'y': (df_2_kredi_turu_recovery_9_ay_tahsilat['Tahsilat%'].values.tolist()), 'type': 'bar', 'name': '9. Ay', 'marker' : {'color': color_palette_blue[2]},'text' : df_2_kredi_turu_recovery_9_ay_tahsilat['Tahsilat%%'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'name+text'},
                                                {'x': (df_2_kredi_turu_recovery_12_ay_tahsilat['Kredi Türü'].values.tolist()), 'y': (df_2_kredi_turu_recovery_12_ay_tahsilat['Tahsilat%'].values.tolist()), 'type': 'bar', 'name': '12. Ay', 'marker' : {'color': color_palette_blue[3]},'text' : df_2_kredi_turu_recovery_12_ay_tahsilat['Tahsilat%%'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'name+text'},
                                            ],
                                    'layout':   {
                                                    'height' : 275,
                                                    #'width' : 1850,
                                                    'title': ' Kredi Türü Bazında İlk 3-6-9-12 Ay NPL Tahsilat %', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': df_2_kredi_turu_recovery_3_ay_tahsilat['Kredi Türü'], 'ticktext': df_2_kredi_turu_recovery_3_ay_tahsilat['Kredi Türü']},
                                                    'margin' : {'l': 40,'r': 0,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }
            #graph-output_02_lemon    
            ),dcc.Graph(
                
                        figure={
                                    'data': [
                                                {'x': (sube_recovery_pct['Şube'].values.tolist()), 'y': (sube_recovery_pct['12. Ay NPL Tahsilat %'].values.tolist()), 'type': 'bar', 'name': sube_recovery_pct['Şube'].values.tolist(), 'marker' : {'color': color_palette_heatmap_pale_10[9]},'text' : sube_recovery_pct['12. Ay NPL Tahsilat %'],'textposition':'outside', 'textfont':{'color':'auto'},'hoverinfo' : 'x+text', 'cliponaxis': False}
                                            ],
                                    'layout':   {
                                                    'height' : 275,
                                                    #'width' : 365,
                                                    'title': {'text':' Şube Bazında 12. Ay NPL Tahsilat Oranı (İlk 5 Şube)','pad':{'l':200}, 'font':{'size':15} },
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': sube_recovery_pct['Şube'], 'ticktext': sube_recovery_pct['Şube']},
                                                    'margin' : {'l': 40,'r': 40,'t': 60,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

    
            #graph-output_02_cherry    
            ),dcc.Graph(
                        
                        figure={
                                    'data': [
                                                {'x': (ofis_recovery_pct['Tahsilat Ofisi'].values.tolist()), 'y': (ofis_recovery_pct['12. Ay NPL Tahsilat %'].values.tolist()), 'type': 'bar', 'name': ofis_recovery_pct['Tahsilat Ofisi'].values.tolist(), 'marker' : {'color': color_palette_heatmap_pale_2_descending},'text' : ofis_recovery_pct['12. Ay NPL Tahsilat %'],'textposition':'outside', 'textfont':{'color':'auto'},'hoverinfo' : 'x+text', 'cliponaxis': False}
                                            ],
                                    'layout':   {
                                                    'height' : 275,
                                                    #'width' : 375,
                                                    'title': {'text':' Tahsilat Ofisi Bazında' '12. Ay NPL Tahsilat Oranı (%)','pad':{'l':0}, 'font':{'size':15} },
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': ofis_recovery_pct['Tahsilat Ofisi'], 'ticktext': ofis_recovery_pct['Tahsilat Ofisi']},
                                                    'margin' : {'l': 100,'r': 100,'t': 60,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }
                    


            )
          


                
                                      
                                                
                                                
#table-1 callback begins here
@app.callback(Output('table-output_07_apple', 'children'),
              [Input('Bölge_Filtresi_tab7', 'value'),
              Input('Kredi Türü_Filtresi_tab7', 'value'),
              Input('Segment_Filtresi_tab7', 'value'),
              Input('Şube_Filtresi_tab7', 'value')
               ])


def update_value_table_1(input_1, input_2, input_3, input_4):  
    
    df_2 = df


    # BÖLGE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Bölge'] == input_1]  

   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  



    # ŞUBE FİLTRESİ    
    if input_4 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_4] 



    


    df_table = df_2.groupby(['Şube'])['Bölge'].agg(pd.Series.mode), df_2.groupby(['Şube'])['Gecikmesiz'].sum(), df_2.groupby(['Şube'])['Bucket-1'].sum(), df_2.groupby(['Şube'])['Bucket-2'].sum(), df_2.groupby(['Şube'])['Bucket-3'].sum(), df_2.groupby(['Şube'])['NPL'].sum()
    df_table = pd.DataFrame(list( df_table))
    df_table.reset_index(drop=True, inplace=True)
    df_table = df_table.T
    df_table.reset_index(drop=False, inplace=True)
    df_table = df_table.rename(columns = {0:'Bölge', 1:'Gecikmesiz (M TL)', 2:'Bucket-1 (M TL)', 3:'Bucket-2 (M TL)', 4:'Bucket-3 (M TL)', 5:'NPL (M TL)'})
    df_table['NPL Aktarım %'] = df_table['NPL (M TL)'] / (df_table['Gecikmesiz (M TL)']+df_table['Bucket-1 (M TL)']+df_table['Bucket-2 (M TL)']+df_table['Bucket-3 (M TL)'])
    df_table = df_table.sort_values(by=['NPL Aktarım %'],  ascending=[False])
    df_table['Tier'] = pd.qcut(df_table['NPL Aktarım %'], 10, labels=False)+1
    df_table = df_table.sort_values(by=['NPL Aktarım %'], ascending = False)
    df_table['NPL Aktarım %'] = pd.Series(["{0:.2f}%".format(val * 100) for val in df_table['NPL Aktarım %']], index = df_table.index)  
    df_table['Gecikmesiz (M TL)'] = df_table['Gecikmesiz (M TL)'].astype(int)
    df_table['Bucket-1 (M TL)'] = df_table['Bucket-1 (M TL)'].astype(int)
    df_table['Bucket-2 (M TL)'] = df_table['Bucket-2 (M TL)'].astype(int)
    df_table['Bucket-3 (M TL)'] = df_table['Bucket-3 (M TL)'].astype(int)
    df_table['NPL (M TL)'] = df_table['NPL (M TL)'].astype(int)
    df_table = df_table[['Şube', 'Bölge', 'Gecikmesiz (M TL)', 'Bucket-1 (M TL)', 'Bucket-2 (M TL)', 'Bucket-3 (M TL)', 'NPL (M TL)', 'Tier', 'NPL Aktarım %']]
    
    
    
    return dash_table.DataTable(
                columns = [{"name": i, "id": i} for i in df_table],
                #hidden_columns = ['Tier'],
                #fixed_rows = {'headers': True},
                data=df_table.to_dict('records'),
                style_cell={'textAlign': 'center','fontFamily': 'Calibri', 'color': '#99A3A4', 'font-style': 'italic', 'fontSize': 15,'height': '10px'},
                style_header={'backgroundColor': '#5D6D7E', 'color': 'white','fontWeight': 'bold'},
                style_data_conditional=[{'if': {'row_index': 'odd'},'backgroundColor': 'rgba(0, 0, 0, 0)'},{'if': {'column_id': 'NPL Aktarım %', 'filter_query': '{Tier} eq 1'},'backgroundColor': color_palette_heatmap_pale_10_descending[0], 'color': 'white'},{'if': {'column_id': 'NPL Aktarım %', 'filter_query': '{Tier} eq 2'},'backgroundColor': color_palette_heatmap_pale_10_descending[1], 'color': 'white'},{'if': {'column_id': 'NPL Aktarım %', 'filter_query': '{Tier} eq 3'},'backgroundColor': color_palette_heatmap_pale_10_descending[2], 'color': 'white'},{'if': {'column_id': 'NPL Aktarım %', 'filter_query': '{Tier} eq 4'},'backgroundColor': color_palette_heatmap_pale_10_descending[3], 'color': 'white'},{'if': {'column_id': 'NPL Aktarım %', 'filter_query': '{Tier} eq 5'},'backgroundColor': color_palette_heatmap_pale_10_descending[4], 'color': 'white'},{'if': {'column_id': 'NPL Aktarım %', 'filter_query': '{Tier} eq 6'},'backgroundColor': color_palette_heatmap_pale_10_descending[5], 'color': 'white'},{'if': {'column_id': 'NPL Aktarım %', 'filter_query': '{Tier} eq 7'},'backgroundColor': color_palette_heatmap_pale_10_descending[6], 'color': 'white'},{'if': {'column_id': 'NPL Aktarım %', 'filter_query': '{Tier} eq 8'},'backgroundColor': color_palette_heatmap_pale_10_descending[7], 'color': 'white'},{'if': {'column_id': 'NPL Aktarım %', 'filter_query': '{Tier} eq 9'},'backgroundColor': color_palette_heatmap_pale_10_descending[8], 'color': 'white'},{'if': {'column_id': 'NPL Aktarım %', 'filter_query': '{Tier} eq 10'},'backgroundColor': color_palette_heatmap_pale_10_descending[9], 'color': 'white'}],
                style_table={'height' : 785,'maxHeight': 785,'overflowY': 'scroll','width': '100%','minWidth': '100%'},
                sort_action="native",
                sort_mode='native',
                #page_size=300
            )                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                
                
                
 #tab-3 callback begins here               
@app.callback([Output('card-output_03_apple', 'children'),Output('card-output_03_orange', 'children'),Output('graph-output_03_apple', 'children'),Output('graph-output_03_orange', 'children'),Output('graph-output_03_banana', 'children'),Output('graph-output_03_lemon', 'children'),Output('graph-output_03_cherry', 'children'),Output('graph-output_03_apricot_1', 'children'),Output('graph-output_03_apricot_2', 'children'),Output('graph-output_03_apricot_3', 'children'),Output('graph-output_03_apricot_4', 'children'),Output('graph-output_03_apricot_5', 'children'),Output('graph-output_03_mango', 'children'),Output('graph-output_03_coconut', 'children')],
              [Input('Şube_Filtresi_tab3', 'value'),
              Input('Kredi Türü_Filtresi_tab3', 'value'),
              Input('Segment_Filtresi_tab3', 'value'),
              Input('Ay_Filtresi_tab3', 'value')
               ]) 


def update_value_3(input_1, input_2, input_3, input_4):  
    



    df_2 = df_3
    
    
    
    # ŞUBE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_1]   
    
   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  



    # AY FİLTRESİ    
    if input_4 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Ay'] == input_4]  




    total_NPL = round(sum(df_2['NPL']),1)
    


    total_recovery = round(sum(df_2['Tahsilat-12']),1)                                                                           

    total_recovery_pct = sum(df_2['Tahsilat-12'])/sum(df_2['NPL'])
    total_recovery_pct = str(round(total_recovery_pct * 100,1))+'%'




    df_2 = df_3
    
    # ŞUBE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_1]   

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  



    # AY FİLTRESİ    
    if input_4 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Ay'] == input_4]  

    
    df_2_kredi_türü = df_2.groupby(['Kredi Türü'])['NPL'].sum(),df_2.groupby(['Kredi Türü'])['NPL'].count()
    df_2_kredi_türü= pd.DataFrame(list( df_2_kredi_türü))
    df_2_kredi_türü.reset_index(drop=True, inplace=True)
    df_2_kredi_türü=df_2_kredi_türü.T
    df_2_kredi_türü.reset_index(drop=False, inplace=True)
    df_2_kredi_türü=df_2_kredi_türü.rename(columns = {0:'NPL', 1:'NPL_2'})
    df_2_kredi_türü=df_2_kredi_türü[['Kredi Türü','NPL']]
    df_2_kredi_türü['NPL'] = df_2_kredi_türü['NPL'].round(1)
    df_2_kredi_türü = df_2_kredi_türü.sort_values(by=['NPL'],  ascending=[False])
    



    df_2 = df_3
    
    # ŞUBE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_1]   
    
   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  


 


    df_2_ay_NPL = df_2.groupby(['Ay'])['NPL'].sum(),df_2.groupby(['Ay'])['NPL'].count()
    df_2_ay_NPL= pd.DataFrame(list( df_2_ay_NPL))
    df_2_ay_NPL.reset_index(drop=True, inplace=True)
    df_2_ay_NPL=df_2_ay_NPL.T
    df_2_ay_NPL.reset_index(drop=False, inplace=True)
    df_2_ay_NPL=df_2_ay_NPL.rename(columns = {0:'NPL', 1:'NPL_2'})
    df_2_ay_NPL=df_2_ay_NPL[['Ay','NPL']]
    df_2_ay_NPL['NPL'] = df_2_ay_NPL['NPL'].round(1)

    

    df_2 = df_3
    
    # ŞUBE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_1]   
    
   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  


    df_2['Total Loans'] = df_2['Gecikmesiz'] + df_2['Bucket-1'] + df_2['Bucket-2'] + df_2['Bucket-3']
    df_2_ay_PL = df_2.groupby(['Ay'])['Total Loans'].sum(),df_2.groupby(['Ay'])['Total Loans'].count()
    df_2_ay_PL= pd.DataFrame(list( df_2_ay_PL))
    df_2_ay_PL.reset_index(drop=True, inplace=True)
    df_2_ay_PL=df_2_ay_PL.T
    df_2_ay_PL.reset_index(drop=False, inplace=True)
    df_2_ay_PL=df_2_ay_PL.rename(columns = {0:'Total Loans', 1:'Total Loans_2'})
    df_2_ay_PL=df_2_ay_PL[['Ay','Total Loans']]
    df_2_ay_PL['Total Loans'] = df_2_ay_PL['Total Loans'].round(0)

 

    df_2 = df_3
    

    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  



    # AY FİLTRESİ    
    if input_4 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Ay'] == input_4]  

    
    df_2['Total Loans'] = df_2['Gecikmesiz'] + df_2['Bucket-1'] + df_2['Bucket-2'] + df_2['Bucket-3']
    df_2_sube_nplpct = df_2.groupby(['Şube'])['Total Loans'].sum(),df_2.groupby(['Şube'])['NPL'].sum()
    df_2_sube_nplpct = pd.DataFrame(list( df_2_sube_nplpct))
    df_2_sube_nplpct.reset_index(drop=True, inplace=True)
    df_2_sube_nplpct = df_2_sube_nplpct.T
    df_2_sube_nplpct.reset_index(drop=False, inplace=True)
    df_2_sube_nplpct = df_2_sube_nplpct.rename(columns = {0:'Total Loans', 1:'NPL'})
    df_2_sube_nplpct['NPL Aktarım %'] = df_2_sube_nplpct['NPL'] / df_2_sube_nplpct ['Total Loans']
    df_2_sube_nplpct = df_2_sube_nplpct[['Şube','NPL Aktarım %']]
    df_2_sube_nplpct = df_2_sube_nplpct.sort_values(by=['NPL Aktarım %'],  ascending=[False])
    df_2_sube_nplpct['NPL Aktarım %']= ((df_2_sube_nplpct['NPL Aktarım %'] * 100).round(1)).astype(str) + '%'    
    df_2_sube_nplpct = df_2_sube_nplpct.head(5)




    sube_recovery_pct = df_2.groupby(['Şube'])['NPL'].sum(),df_2.groupby(['Şube'])['Tahsilat-12'].sum()
    sube_recovery_pct = pd.DataFrame(list( sube_recovery_pct))
    sube_recovery_pct.reset_index(drop=True, inplace=True)
    sube_recovery_pct = sube_recovery_pct.T
    sube_recovery_pct.reset_index(drop=False, inplace=True)
    sube_recovery_pct = sube_recovery_pct.rename(columns = {0:'NPL', 1:'Recovery'})
    sube_recovery_pct['12. Ay NPL Tahsilat %'] = sube_recovery_pct['Recovery'] / sube_recovery_pct['NPL']
    sube_recovery_pct = sube_recovery_pct[['Şube','12. Ay NPL Tahsilat %']]
    sube_recovery_pct = sube_recovery_pct.sort_values(by=['12. Ay NPL Tahsilat %'],  ascending=[False])
    sube_recovery_pct['12. Ay NPL Tahsilat %']= ((sube_recovery_pct['12. Ay NPL Tahsilat %'] * 100).round(1)).astype(str) + '%'        
    sube_recovery_pct = sube_recovery_pct.head(5)
    
     





    df_2 = df_3
    
    # ŞUBE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_1]   
    
   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  



    df_2_roll_rate_1 = df_2.groupby(['Ay'])['Gecikmesiz'].sum(),df_2.groupby(['Ay'])['Bucket-1'].sum()
    df_2_roll_rate_1 = pd.DataFrame(list( df_2_roll_rate_1))
    df_2_roll_rate_1.reset_index(drop=True, inplace=True)
    df_2_roll_rate_1 = df_2_roll_rate_1.T
    df_2_roll_rate_1.reset_index(drop=False, inplace=True)
    df_2_roll_rate_1 = df_2_roll_rate_1.rename(columns = {0:'Previous', 1:'Next'})
    df_2_roll_rate_1['Roll Rate %'] = df_2_roll_rate_1['Next'] / df_2_roll_rate_1['Previous']
    df_2_roll_rate_1 = df_2_roll_rate_1[['Ay','Roll Rate %']]
    df_2_roll_rate_1 = df_2_roll_rate_1.sort_values(by=['Ay'],  ascending=[True])
    df_2_roll_rate_1['Roll Rate %']= ((df_2_roll_rate_1['Roll Rate %'] * 100).round(1)).astype(str) + '%'    
    





    df_2 = df_3
    
    # ŞUBE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_1]   
    
   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  


    df_2_roll_rate_2 = df_2.groupby(['Ay'])['Bucket-1'].sum(),df_2.groupby(['Ay'])['Bucket-2'].sum()
    df_2_roll_rate_2 = pd.DataFrame(list( df_2_roll_rate_2))
    df_2_roll_rate_2.reset_index(drop=True, inplace=True)
    df_2_roll_rate_2 = df_2_roll_rate_2.T
    df_2_roll_rate_2.reset_index(drop=False, inplace=True)
    df_2_roll_rate_2 = df_2_roll_rate_2.rename(columns = {0:'Previous', 1:'Next'})
    df_2_roll_rate_2['Roll Rate %'] = df_2_roll_rate_2['Next'] / df_2_roll_rate_2['Previous']
    df_2_roll_rate_2 = df_2_roll_rate_2[['Ay','Roll Rate %']]
    df_2_roll_rate_2['Roll Rate %']= ((df_2_roll_rate_2['Roll Rate %'] * 100).round(1)).astype(str) + '%'    
    






    df_2 = df_3
    
    # ŞUBE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_1]   
    
   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  



    df_2_roll_rate_3 = df_2.groupby(['Ay'])['Bucket-2'].sum(),df_2.groupby(['Ay'])['Bucket-3'].sum()
    df_2_roll_rate_3 = pd.DataFrame(list( df_2_roll_rate_3))
    df_2_roll_rate_3.reset_index(drop=True, inplace=True)
    df_2_roll_rate_3 = df_2_roll_rate_3.T
    df_2_roll_rate_3.reset_index(drop=False, inplace=True)
    df_2_roll_rate_3 = df_2_roll_rate_3.rename(columns = {0:'Previous', 1:'Next'})
    df_2_roll_rate_3['Roll Rate %'] = df_2_roll_rate_3['Next'] / df_2_roll_rate_3['Previous']
    df_2_roll_rate_3 = df_2_roll_rate_3[['Ay','Roll Rate %']]
    df_2_roll_rate_3['Roll Rate %']= ((df_2_roll_rate_3['Roll Rate %'] * 100).round(1)).astype(str) + '%'      
    






    df_2 = df_3
    
    # ŞUBE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_1]   
    
   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  



    df_2_roll_rate_4 = df_2.groupby(['Ay'])['Bucket-3'].sum(),df_2.groupby(['Ay'])['NPL'].sum()
    df_2_roll_rate_4 = pd.DataFrame(list( df_2_roll_rate_4))
    df_2_roll_rate_4.reset_index(drop=True, inplace=True)
    df_2_roll_rate_4 = df_2_roll_rate_4.T
    df_2_roll_rate_4.reset_index(drop=False, inplace=True)
    df_2_roll_rate_4 = df_2_roll_rate_4.rename(columns = {0:'Previous', 1:'Next'})
    df_2_roll_rate_4['Roll Rate %'] = df_2_roll_rate_4['Next'] / df_2_roll_rate_4['Previous']
    df_2_roll_rate_4 = df_2_roll_rate_4[['Ay','Roll Rate %']]
    df_2_roll_rate_4['Roll Rate %']= ((df_2_roll_rate_4['Roll Rate %'] * 100).round(1)).astype(str) + '%'    
    




    df_2 = df_3
    
    # ŞUBE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_1]   
    
   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  



    df_2_roll_rate_5 = df_2.groupby(['Ay'])['Gecikmesiz'].sum(),df_2.groupby(['Ay'])['NPL'].sum()
    df_2_roll_rate_5 = pd.DataFrame(list( df_2_roll_rate_5))
    df_2_roll_rate_5.reset_index(drop=True, inplace=True)
    df_2_roll_rate_5 = df_2_roll_rate_5.T
    df_2_roll_rate_5.reset_index(drop=False, inplace=True)
    df_2_roll_rate_5 = df_2_roll_rate_5.rename(columns = {0:'Previous', 1:'Next'})
    df_2_roll_rate_5['Roll Rate %'] = df_2_roll_rate_5['Next'] / df_2_roll_rate_5['Previous']
    df_2_roll_rate_5 = df_2_roll_rate_5[['Ay','Roll Rate %']]
    df_2_roll_rate_5['Roll Rate %']= ((df_2_roll_rate_5['Roll Rate %'] * 100).round(2)).astype(str) + '%'    





    df_2 = df_3
    
    # ŞUBE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_1]   
    
   
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_2]  

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  



    # AY FİLTRESİ    
    if input_4 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Ay'] == input_4]  
        


    recovery_vintage_ay = list(range(0,13))
    recovery_vintage_tahsilat = [0,sum(df_2['Tahsilat-1']),sum(df_2['Tahsilat-2']),sum(df_2['Tahsilat-3']),sum(df_2['Tahsilat-4']),sum(df_2['Tahsilat-5']),sum(df_2['Tahsilat-6']),sum(df_2['Tahsilat-7']),sum(df_2['Tahsilat-8']),sum(df_2['Tahsilat-9']),sum(df_2['Tahsilat-10']),sum(df_2['Tahsilat-11']),sum(df_2['Tahsilat-12'])]
    recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
    recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
    recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
    recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2['NPL'])
    recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'    
    recovery_vintage_all = recovery_vintage
    
    
    
    
    
    
    df_2 = df_3
    
    # ŞUBE FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Şube'] == input_1]   

   
    
    # SEGMENT FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_3]  



    # AY FİLTRESİ    
    if input_4 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Ay'] == input_4]  
    
    
    
    kredi_turu_recovery = df_2.groupby(['Kredi Türü'])['Tahsilat-12'].sum(),df_2.groupby(['Kredi Türü'])['Tahsilat-12'].sum()
    kredi_turu_recovery = pd.DataFrame(list( kredi_turu_recovery))
    kredi_turu_recovery.reset_index(drop=True, inplace=True)
    kredi_turu_recovery = kredi_turu_recovery.T
    kredi_turu_recovery.reset_index(drop=False, inplace=True)
    kredi_turu_recovery = kredi_turu_recovery.rename(columns = {0:'Recovery', 1:'Delete'})
    kredi_turu_recovery = kredi_turu_recovery[['Kredi Türü','Recovery']]
    kredi_turu_recovery = kredi_turu_recovery.sort_values(by=['Recovery'],  ascending=[False])
    kredi_turu_recovery['Recovery']= (kredi_turu_recovery['Recovery'].round(1))        
    
    
    #card-output_03_apple
    return html.H1(total_NPL, style={"color": "white","background": color_palette_blue[3], 'textAlign': 'center', 'width':'75%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '250%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '-20%', 'margin-left': '22%'}
    
    

    #card-output_03_orange          
          ),html.H1(total_recovery, style={"color": "white","background": color_palette_blue[1], 'textAlign': 'center', 'width':'75%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '250%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '-20%', 'margin-left': '22%'}                              
   

                    
    #graph-output_03_apple          

   ),dcc.Graph(                    
        figure = px.area(
                            df_2_kredi_türü, 
                            x="Kredi Türü", 
                            y="NPL",  
                            title=" Kredi Türü Bazında NPL Aktarımları (M TL)", 
                            height = 175,
                            width = 475,
                            text = 'NPL'
                            ).update_layout(
                                    title = {'pad':{'l':65}},
                                    paper_bgcolor = 'rgba(0,0,0,0)',
                                    plot_bgcolor = 'rgba(0,0,0,0)',
                                    margin={"r":40,"t":40,"l":90,"b":70},
                                    yaxis = {'title': None,'showgrid' : False, 'showline' : False, 'showticklabels' : False},
                                    xaxis = {'title': None,'showgrid' : False}
                                    ).update_traces(
                                                    #hovertemplate = df_2_kredi_türü["Kredi Türü"]+ ' : ' + df_2_kredi_türü["NPL"],
                                                    textposition ='top center',
                                                    cliponaxis = False,
                                                    line_color = color_palette_blue[0]
                                                    )                    

 
              
    #graph-output_03_orange
    ),dcc.Graph(
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

 
              
    #graph-output_03_banana
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'x': (df_2_ay_PL['Ay'].values.tolist()), 'y': (df_2_ay_PL['Total Loans'].values.tolist()), 'type': 'bar', 'name': df_2_ay_PL['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_ay_PL['Total Loans'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'x+text'}
                                            ],
                                    'layout':   {
                                                    'height' : 175,
                                                    'width' : 800,
                                                    'title': ' Kredi Plasmanının Gelişimi (M TL)', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': df_2_ay_PL['Ay'], 'ticktext': df_2_ay_PL['Ay']},
                                                    'margin' : {'l': 40,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_03_lemon
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'x': (df_2_sube_nplpct['Şube'].values.tolist()), 'y': (df_2_sube_nplpct['NPL Aktarım %'].values.tolist()), 'type': 'bar', 'name': df_2_sube_nplpct['Şube'].values.tolist(), 'marker' : {'color': color_palette_heatmap_pale_10},'text' : df_2_sube_nplpct['NPL Aktarım %'],'textposition':'outside', 'textfont':{'color':'auto'},'hoverinfo' : 'x+text', 'cliponaxis': False}
                                            ],
                                    'layout':   {
                                                    'height' : 175,
                                                    'width' : 575,
                                                    'title': ' Şube Bazında Aylık NPL Dönüşüm Oranı (İlk 5 Şube)', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': df_2_sube_nplpct['Şube'], 'ticktext': df_2_sube_nplpct['Şube']},
                                                    'margin' : {'l': 10,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_03_cherry
            ),dcc.Graph(
                
                        figure={
                                    'data': [
                                                {'x': (sube_recovery_pct['Şube'].values.tolist()), 'y': (sube_recovery_pct['12. Ay NPL Tahsilat %'].values.tolist()), 'type': 'bar', 'name': sube_recovery_pct['Şube'].values.tolist(), 'marker' : {'color': color_palette_heatmap_pale_10_descending},'text' : sube_recovery_pct['12. Ay NPL Tahsilat %'],'textposition':'outside', 'textfont':{'color':'auto'},'hoverinfo' : 'x+text', 'cliponaxis': False}
                                            ],
                                    'layout':   {
                                                    'height' : 195,
                                                    'width' : 575,
                                                    'title': {'text':' Şube Bazında 12. Ay NPL Tahsilat Oranı (İlk 5 Şube)'},
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': sube_recovery_pct['Şube'], 'ticktext': sube_recovery_pct['Şube']},
                                                    'margin' : {'l': 10,'r': 40,'t': 60,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

    
    #graph-output_03_apricot_1
            ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'y': (df_2_roll_rate_1['Ay'].values.tolist()), 'x': (df_2_roll_rate_1['Roll Rate %'].values.tolist()), 'type': 'bar', 'name': df_2_roll_rate_1['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_roll_rate_1['Roll Rate %'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'text', 'hoverlabel':{'font':{'size':12}} ,'orientation': 'h'}
                                            ],
                                    'layout':   {
                                                    'height' : 495,
                                                    'width' : 250,
                                                    'title': ' Bucket-1', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'yaxis': {'showgrid' : False, 'showline' : True, 'showticklabels' : True, 'tickvals': df_2_roll_rate_1['Ay'], 'ticktext': df_2_roll_rate_1['Ay']},
                                                    'margin' : {'l': 50,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_03_apricot_2
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'y': (df_2_roll_rate_2['Ay'].values.tolist()), 'x': (df_2_roll_rate_2['Roll Rate %'].values.tolist()), 'type': 'bar', 'name': df_2_roll_rate_2['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_roll_rate_2['Roll Rate %'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'text', 'hoverlabel':{'font':{'size':12}} ,'orientation': 'h'}
                                            ],
                                    'layout':   {
                                                    'height' : 495,
                                                    'width' : 250,
                                                    'title': ' Bucket-2', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'yaxis': {'showgrid' : False, 'showline' : True, 'showticklabels' : False, 'tickvals': df_2_roll_rate_2['Ay'], 'ticktext': df_2_roll_rate_2['Ay']},
                                                    'margin' : {'l': 50,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_03_apricot_3
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'y': (df_2_roll_rate_3['Ay'].values.tolist()), 'x': (df_2_roll_rate_3['Roll Rate %'].values.tolist()), 'type': 'bar', 'name': df_2_roll_rate_3['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_roll_rate_3['Roll Rate %'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'text', 'hoverlabel':{'font':{'size':12}} ,'orientation': 'h'}
                                            ],
                                    'layout':   {
                                                    'height' : 495,
                                                    'width' : 250,
                                                    'title': ' Bucket-3', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'yaxis': {'showgrid' : False, 'showline' : True, 'showticklabels' : False, 'tickvals': df_2_roll_rate_3['Ay'], 'ticktext': df_2_roll_rate_3['Ay']},
                                                    'margin' : {'l': 50,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_03_apricot_4
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'y': (df_2_roll_rate_4['Ay'].values.tolist()), 'x': (df_2_roll_rate_4['Roll Rate %'].values.tolist()), 'type': 'bar', 'name': df_2_roll_rate_4['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_roll_rate_4['Roll Rate %'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'text', 'hoverlabel':{'font':{'size':12}} ,'orientation': 'h'}
                                            ],
                                    'layout':   {
                                                    'height' : 495,
                                                    'width' : 250,
                                                    'title': ' NPL', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'yaxis': {'showgrid' : False, 'showline' : True, 'showticklabels' : False, 'tickvals': df_2_roll_rate_4['Ay'], 'ticktext': df_2_roll_rate_4['Ay']},
                                                    'margin' : {'l': 50,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_03_apricot_5
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'y': (df_2_roll_rate_5['Ay'].values.tolist()), 'x': (df_2_roll_rate_5['Roll Rate %'].values.tolist()), 'type': 'bar', 'name': df_2_roll_rate_5['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_roll_rate_5['Roll Rate %'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'text', 'hoverlabel':{'font':{'size':12}} ,'orientation': 'h'}
                                            ],
                                    'layout':   {
                                                    'height' : 495,
                                                    'width' : 250,
                                                    'title': ' Aylık NPL Dönüşüm %', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'yaxis': {'showgrid' : False, 'showline' : True, 'showticklabels' : False, 'tickvals': df_2_roll_rate_5['Ay'], 'ticktext': df_2_roll_rate_5['Ay']},
                                                    'margin' : {'l': 50,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_03_mango
    ),dcc.Graph(
                                figure = px.area(
                            recovery_vintage_all, 
                            x="Ay", 
                            y="Tahsilat%",  
                            title=" NPL Tahsilat Vintage Eğrisi", 
                            height = 250,
                            width = 575,
                            text = 'Tahsilat%%'
                            ).update_layout(
                                    title = {'pad':{'l':185}},
                                    paper_bgcolor = 'rgba(0,0,0,0)',
                                    plot_bgcolor = 'rgba(0,0,0,0)',
                                    margin={"r":40,"t":40,"l":20,"b":40},
                                    yaxis = {'title': None,'showgrid' : False, 'showline' : True, 'showticklabels' : False,'tickformat': ',.0%', 'linecolor': '#E5E8E8'},
                                    xaxis = {'title': 'Takipte Geçen Süre (Ay)','showgrid' : False, 'showline' : False, 'linecolor': '#99A3A4'}
                                    ).update_traces(
                                                    hovertemplate = '%{x}. Ay: %{text}',
                                                    textposition ='top center',
                                                    cliponaxis = False,
                                                    line_color = color_palette_blue[0]
                                                    )    

 
     #graph-output_03_coconut          
   ),dcc.Graph(                    
        figure = px.area(
                            kredi_turu_recovery, 
                            x="Kredi Türü", 
                            y="Recovery",  
                            title=" Kredi Türü Bazında NPL Tahsilatı (M TL)", 
                            height = 150,
                            width = 575,
                            text = 'Recovery'
                            ).update_layout(
                                    title = {'pad':{'l':65}},
                                    paper_bgcolor = 'rgba(0,0,0,0)',
                                    plot_bgcolor = 'rgba(0,0,0,0)',
                                    margin={"r":40,"t":40,"l":20,"b":40},
                                    yaxis = {'title': None,'showgrid' : False, 'showline' : False, 'showticklabels' : False},
                                    xaxis = {'title': None,'showgrid' : False}
                                    ).update_traces(
                                                    #hovertemplate = df_2_kredi_türü["Kredi Türü"]+ ' : ' + df_2_kredi_türü["NPL"],
                                                    textposition ='top center',
                                                    cliponaxis = False,
                                                    line_color = color_palette_blue[0]
                                                    )                    

 

    )          
                      




                
 #tab-4 callback begins here               
@app.callback([Output('card-output_04_apple', 'children'),Output('card-output_04_orange', 'children'),Output('graph-output_04_apple', 'children'),Output('graph-output_04_orange', 'children'),Output('graph-output_04_banana', 'children'),Output('graph-output_04_lemon', 'children'),Output('graph-output_04_cherry', 'children'),Output('graph-output_04_apricot_1', 'children'),Output('graph-output_04_apricot_2', 'children'),Output('graph-output_04_apricot_3', 'children'),Output('graph-output_04_apricot_4', 'children'),Output('graph-output_04_apricot_5', 'children'),Output('graph-output_04_mango', 'children'),Output('graph-output_04_coconut', 'children')],
              [Input('Kredi Türü_Filtresi_tab4', 'value'),
              Input('Segment_Filtresi_tab4', 'value'),
              Input('Ay_Filtresi_tab4', 'value')
               ])


def update_value_4(input_1, input_2, input_3):  
    



    df_2 = df_4
    
    
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_1]  

   
    
    # SEGMENT FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_2]  



    # AY FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Ay'] == input_3]  




    total_NPL = round(sum(df_2['NPL']),1)
    


    total_recovery = round(sum(df_2['Tahsilat-12']),1)                                                                           

    total_recovery_pct = sum(df_2['Tahsilat-12'])/sum(df_2['NPL'])
    total_recovery_pct = str(round(total_recovery_pct * 100,1))+'%'




    df_2 = df_4
    

    
    # SEGMENT FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_2]  



    # AY FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Ay'] == input_3]  
        
        
        

    
    df_2_kredi_türü = df_2.groupby(['Kredi Türü'])['NPL'].sum(),df_2.groupby(['Kredi Türü'])['NPL'].count()
    df_2_kredi_türü= pd.DataFrame(list( df_2_kredi_türü))
    df_2_kredi_türü.reset_index(drop=True, inplace=True)
    df_2_kredi_türü=df_2_kredi_türü.T
    df_2_kredi_türü.reset_index(drop=False, inplace=True)
    df_2_kredi_türü=df_2_kredi_türü.rename(columns = {0:'NPL', 1:'NPL_2'})
    df_2_kredi_türü=df_2_kredi_türü[['Kredi Türü','NPL']]
    df_2_kredi_türü['NPL'] = df_2_kredi_türü['NPL'].round(1)
    df_2_kredi_türü = df_2_kredi_türü.sort_values(by=['NPL'],  ascending=[False])
    



    df_2 = df_4
    
    
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_1]  

   
    
    # SEGMENT FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_2]  



 


    df_2_ay_NPL = df_2.groupby(['Ay'])['NPL'].sum(),df_2.groupby(['Ay'])['NPL'].count()
    df_2_ay_NPL= pd.DataFrame(list( df_2_ay_NPL))
    df_2_ay_NPL.reset_index(drop=True, inplace=True)
    df_2_ay_NPL=df_2_ay_NPL.T
    df_2_ay_NPL.reset_index(drop=False, inplace=True)
    df_2_ay_NPL=df_2_ay_NPL.rename(columns = {0:'NPL', 1:'NPL_2'})
    df_2_ay_NPL=df_2_ay_NPL[['Ay','NPL']]
    df_2_ay_NPL['NPL'] = df_2_ay_NPL['NPL'].round(1)

    

    df_2 = df_4
    
    
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_1]  

   
    
    # SEGMENT FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_2]  




    df_2['Total Loans'] = df_2['Gecikmesiz'] + df_2['Bucket-1'] + df_2['Bucket-2'] + df_2['Bucket-3']
    df_2_ay_PL = df_2.groupby(['Ay'])['Total Loans'].sum(),df_2.groupby(['Ay'])['Total Loans'].count()
    df_2_ay_PL= pd.DataFrame(list( df_2_ay_PL))
    df_2_ay_PL.reset_index(drop=True, inplace=True)
    df_2_ay_PL=df_2_ay_PL.T
    df_2_ay_PL.reset_index(drop=False, inplace=True)
    df_2_ay_PL=df_2_ay_PL.rename(columns = {0:'Total Loans', 1:'Total Loans_2'})
    df_2_ay_PL=df_2_ay_PL[['Ay','Total Loans']]
    df_2_ay_PL['Total Loans'] = df_2_ay_PL['Total Loans'].round(0)

 

    

    
    df_2 = df_4
    
    
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_1]  

   
    
    # SEGMENT FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_2]  



    # AY FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Ay'] == input_3]  



    recovery_vintage_ay = list(range(0,13))
    recovery_vintage_tahsilat = [0,sum(df_2['Tahsilat-1']),sum(df_2['Tahsilat-2']),sum(df_2['Tahsilat-3']),sum(df_2['Tahsilat-4']),sum(df_2['Tahsilat-5']),sum(df_2['Tahsilat-6']),sum(df_2['Tahsilat-7']),sum(df_2['Tahsilat-8']),sum(df_2['Tahsilat-9']),sum(df_2['Tahsilat-10']),sum(df_2['Tahsilat-11']),sum(df_2['Tahsilat-12'])]
    recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
    recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
    recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
    recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2['NPL'])
    recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'    
    recovery_vintage_all = recovery_vintage


     





    df_2 = df_4
    
    
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_1]  

   
    
    # SEGMENT FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_2]  







    df_2_roll_rate_1 = df_2.groupby(['Ay'])['Gecikmesiz'].sum(),df_2.groupby(['Ay'])['Bucket-1'].sum()
    df_2_roll_rate_1 = pd.DataFrame(list( df_2_roll_rate_1))
    df_2_roll_rate_1.reset_index(drop=True, inplace=True)
    df_2_roll_rate_1 = df_2_roll_rate_1.T
    df_2_roll_rate_1.reset_index(drop=False, inplace=True)
    df_2_roll_rate_1 = df_2_roll_rate_1.rename(columns = {0:'Previous', 1:'Next'})
    df_2_roll_rate_1['Roll Rate %'] = df_2_roll_rate_1['Next'] / df_2_roll_rate_1['Previous']
    df_2_roll_rate_1 = df_2_roll_rate_1[['Ay','Roll Rate %']]
    df_2_roll_rate_1 = df_2_roll_rate_1.sort_values(by=['Ay'],  ascending=[True])
    df_2_roll_rate_1['Roll Rate %']= ((df_2_roll_rate_1['Roll Rate %'] * 100).round(1)).astype(str) + '%'    
    





    df_2 = df_4
    
    
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_1]  

   
    
    # SEGMENT FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_2]  





    df_2_roll_rate_2 = df_2.groupby(['Ay'])['Bucket-1'].sum(),df_2.groupby(['Ay'])['Bucket-2'].sum()
    df_2_roll_rate_2 = pd.DataFrame(list( df_2_roll_rate_2))
    df_2_roll_rate_2.reset_index(drop=True, inplace=True)
    df_2_roll_rate_2 = df_2_roll_rate_2.T
    df_2_roll_rate_2.reset_index(drop=False, inplace=True)
    df_2_roll_rate_2 = df_2_roll_rate_2.rename(columns = {0:'Previous', 1:'Next'})
    df_2_roll_rate_2['Roll Rate %'] = df_2_roll_rate_2['Next'] / df_2_roll_rate_2['Previous']
    df_2_roll_rate_2 = df_2_roll_rate_2[['Ay','Roll Rate %']]
    df_2_roll_rate_2['Roll Rate %']= ((df_2_roll_rate_2['Roll Rate %'] * 100).round(1)).astype(str) + '%'    
    




    df_2 = df_4
    
    
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_1]  

   
    
    # SEGMENT FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_2]  





    df_2_roll_rate_3 = df_2.groupby(['Ay'])['Bucket-2'].sum(),df_2.groupby(['Ay'])['Bucket-3'].sum()
    df_2_roll_rate_3 = pd.DataFrame(list( df_2_roll_rate_3))
    df_2_roll_rate_3.reset_index(drop=True, inplace=True)
    df_2_roll_rate_3 = df_2_roll_rate_3.T
    df_2_roll_rate_3.reset_index(drop=False, inplace=True)
    df_2_roll_rate_3 = df_2_roll_rate_3.rename(columns = {0:'Previous', 1:'Next'})
    df_2_roll_rate_3['Roll Rate %'] = df_2_roll_rate_3['Next'] / df_2_roll_rate_3['Previous']
    df_2_roll_rate_3 = df_2_roll_rate_3[['Ay','Roll Rate %']]
    df_2_roll_rate_3['Roll Rate %']= ((df_2_roll_rate_3['Roll Rate %'] * 100).round(1)).astype(str) + '%'      
    


    df_2 = df_4
    
    
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_1]  

   
    
    # SEGMENT FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_2]  





    df_2_roll_rate_4 = df_2.groupby(['Ay'])['Bucket-3'].sum(),df_2.groupby(['Ay'])['NPL'].sum()
    df_2_roll_rate_4 = pd.DataFrame(list( df_2_roll_rate_4))
    df_2_roll_rate_4.reset_index(drop=True, inplace=True)
    df_2_roll_rate_4 = df_2_roll_rate_4.T
    df_2_roll_rate_4.reset_index(drop=False, inplace=True)
    df_2_roll_rate_4 = df_2_roll_rate_4.rename(columns = {0:'Previous', 1:'Next'})
    df_2_roll_rate_4['Roll Rate %'] = df_2_roll_rate_4['Next'] / df_2_roll_rate_4['Previous']
    df_2_roll_rate_4 = df_2_roll_rate_4[['Ay','Roll Rate %']]
    df_2_roll_rate_4['Roll Rate %']= ((df_2_roll_rate_4['Roll Rate %'] * 100).round(1)).astype(str) + '%'    
    



    df_2 = df_4
    
    
    
    # KREDİ TÜRÜ FİLTRESİ    
    if input_1 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Kredi Türü'] == input_1]  

   
    
    # SEGMENT FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_2]  





    df_2_roll_rate_5 = df_2.groupby(['Ay'])['Gecikmesiz'].sum(),df_2.groupby(['Ay'])['NPL'].sum()
    df_2_roll_rate_5 = pd.DataFrame(list( df_2_roll_rate_5))
    df_2_roll_rate_5.reset_index(drop=True, inplace=True)
    df_2_roll_rate_5 = df_2_roll_rate_5.T
    df_2_roll_rate_5.reset_index(drop=False, inplace=True)
    df_2_roll_rate_5 = df_2_roll_rate_5.rename(columns = {0:'Previous', 1:'Next'})
    df_2_roll_rate_5['Roll Rate %'] = df_2_roll_rate_5['Next'] / df_2_roll_rate_5['Previous']
    df_2_roll_rate_5 = df_2_roll_rate_5[['Ay','Roll Rate %']]
    df_2_roll_rate_5['Roll Rate %']= ((df_2_roll_rate_5['Roll Rate %'] * 100).round(2)).astype(str) + '%'    




    df_2 = df_4
    
    
    
    # SEGMENT FİLTRESİ    
    if input_2 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Segment'] == input_2]  



    # AY FİLTRESİ    
    if input_3 == 'All':
        df_2 = df_2
    else :
        df_2 = df_2[df_2['Ay'] == input_3]  
        


    df_2['Total Loans'] = df_2['Gecikmesiz'] + df_2['Bucket-1'] + df_2['Bucket-2'] + df_2['Bucket-3']
    df_2_kredituru_nplpct = df_2.groupby(['Kredi Türü'])['Total Loans'].sum(),df_2.groupby(['Kredi Türü'])['NPL'].sum()
    df_2_kredituru_nplpct = pd.DataFrame(list( df_2_kredituru_nplpct))
    df_2_kredituru_nplpct.reset_index(drop=True, inplace=True)
    df_2_kredituru_nplpct = df_2_kredituru_nplpct.T
    df_2_kredituru_nplpct.reset_index(drop=False, inplace=True)
    df_2_kredituru_nplpct = df_2_kredituru_nplpct.rename(columns = {0:'Total Loans', 1:'NPL'})
    df_2_kredituru_nplpct['NPL Aktarım %'] = df_2_kredituru_nplpct['NPL'] / df_2_kredituru_nplpct ['Total Loans']
    df_2_kredituru_nplpct = df_2_kredituru_nplpct[['Kredi Türü','NPL Aktarım %']]
    df_2_kredituru_nplpct = df_2_kredituru_nplpct.sort_values(by=['NPL Aktarım %'],  ascending=[False])
    df_2_kredituru_nplpct['NPL Aktarım %']= ((df_2_kredituru_nplpct['NPL Aktarım %'] * 100).round(2)).astype(str) + '%'    

    


    kredi_turu_recovery_pct = df_2.groupby(['Kredi Türü'])['NPL'].sum(),df_2.groupby(['Kredi Türü'])['Tahsilat-12'].sum()
    kredi_turu_recovery_pct = pd.DataFrame(list( kredi_turu_recovery_pct))
    kredi_turu_recovery_pct.reset_index(drop=True, inplace=True)
    kredi_turu_recovery_pct = kredi_turu_recovery_pct.T
    kredi_turu_recovery_pct.reset_index(drop=False, inplace=True)
    kredi_turu_recovery_pct = kredi_turu_recovery_pct.rename(columns = {0:'NPL', 1:'Recovery'})
    kredi_turu_recovery_pct['12. Ay NPL Tahsilat %'] = kredi_turu_recovery_pct['Recovery'] / kredi_turu_recovery_pct['NPL']
    kredi_turu_recovery_pct = kredi_turu_recovery_pct[['Kredi Türü','12. Ay NPL Tahsilat %']]
    kredi_turu_recovery_pct = kredi_turu_recovery_pct.sort_values(by=['12. Ay NPL Tahsilat %'],  ascending=[False])
    kredi_turu_recovery_pct['12. Ay NPL Tahsilat %']= ((kredi_turu_recovery_pct['12. Ay NPL Tahsilat %'] * 100).round(1)).astype(str) + '%'         
    
    
    kredi_turu_recovery = df_2.groupby(['Kredi Türü'])['Tahsilat-12'].sum(),df_2.groupby(['Kredi Türü'])['Tahsilat-12'].sum()
    kredi_turu_recovery = pd.DataFrame(list( kredi_turu_recovery))
    kredi_turu_recovery.reset_index(drop=True, inplace=True)
    kredi_turu_recovery = kredi_turu_recovery.T
    kredi_turu_recovery.reset_index(drop=False, inplace=True)
    kredi_turu_recovery = kredi_turu_recovery.rename(columns = {0:'Recovery', 1:'Delete'})
    kredi_turu_recovery = kredi_turu_recovery[['Kredi Türü','Recovery']]
    kredi_turu_recovery = kredi_turu_recovery.sort_values(by=['Recovery'],  ascending=[False])
    kredi_turu_recovery['Recovery']= (kredi_turu_recovery['Recovery'].round(1))  
    
    
    #card-output_04_apple
    return html.H1(total_NPL, style={"color": "white","background": color_palette_blue[3], 'textAlign': 'center', 'width':'75%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '250%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '-20%', 'margin-left': '22%'}
    
    

    #card-output_43_orange          
          ),html.H1(total_recovery, style={"color": "white","background": color_palette_blue[1], 'textAlign': 'center', 'width':'75%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '250%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '-20%', 'margin-left': '22%'}                              
   

                    
    #graph-output_04_apple          

   ),dcc.Graph(                    
        figure = px.area(
                            df_2_kredi_türü, 
                            x="Kredi Türü", 
                            y="NPL",  
                            title=" Kredi Türü Bazında NPL Aktarımları (M TL)", 
                            height = 175,
                            width = 475,
                            text = 'NPL'
                            ).update_layout(
                                    title = {'pad':{'l':65}},
                                    paper_bgcolor = 'rgba(0,0,0,0)',
                                    plot_bgcolor = 'rgba(0,0,0,0)',
                                    margin={"r":40,"t":40,"l":90,"b":70},
                                    yaxis = {'title': None,'showgrid' : False, 'showline' : False, 'showticklabels' : False},
                                    xaxis = {'title': None,'showgrid' : False}
                                    ).update_traces(
                                                    #hovertemplate = df_2_kredi_türü["Kredi Türü"]+ ' : ' + df_2_kredi_türü["NPL"],
                                                    textposition ='top center',
                                                    cliponaxis = False,
                                                    line_color = color_palette_blue[0]
                                                    )                    

 
              
    #graph-output_04_orange
    ),dcc.Graph(
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

 
              
    #graph-output_04_banana
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'x': (df_2_ay_PL['Ay'].values.tolist()), 'y': (df_2_ay_PL['Total Loans'].values.tolist()), 'type': 'bar', 'name': df_2_ay_PL['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_ay_PL['Total Loans'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'x+text'}
                                            ],
                                    'layout':   {
                                                    'height' : 175,
                                                    'width' : 800,
                                                    'title': ' Kredi Plasmanının Gelişimi (M TL)', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': df_2_ay_PL['Ay'], 'ticktext': df_2_ay_PL['Ay']},
                                                    'margin' : {'l': 40,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_04_lemon
    ),dcc.Graph(

        
                                figure = px.area(
                            recovery_vintage_all, 
                            x="Ay", 
                            y="Tahsilat%",  
                            title=" NPL Tahsilat Vintage Eğrisi", 
                            height = 225,
                            width = 575,
                            text = 'Tahsilat%%'
                            ).update_layout(
                                    title = {'pad':{'l':185}},
                                    paper_bgcolor = 'rgba(0,0,0,0)',
                                    plot_bgcolor = 'rgba(0,0,0,0)',
                                    margin={"r":40,"t":40,"l":20,"b":40},
                                    yaxis = {'title': None,'showgrid' : False, 'showline' : True, 'showticklabels' : False,'tickformat': ',.0%', 'linecolor': '#E5E8E8'},
                                    xaxis = {'title': 'Takipte Geçen Süre (Ay)','showgrid' : False, 'showline' : False, 'linecolor': '#99A3A4'}
                                    ).update_traces(
                                                    hovertemplate = '%{x}. Ay: %{text}',
                                                    textposition ='top center',
                                                    cliponaxis = False,
                                                    line_color = color_palette_blue[0]
                                                    )    
    #graph-output_04_cherry
    ),dcc.Graph(                    
                        figure = px.area(
                            kredi_turu_recovery, 
                            x="Kredi Türü", 
                            y="Recovery",  
                            title=" Kredi Türü Bazında NPL Tahsilatı (M TL)", 
                            height = 125,
                            width = 575,
                            text = 'Recovery'
                            ).update_layout(
                                    title = {'pad':{'l':65}},
                                    paper_bgcolor = 'rgba(0,0,0,0)',
                                    plot_bgcolor = 'rgba(0,0,0,0)',
                                    margin={"r":40,"t":40,"l":20,"b":40},
                                    yaxis = {'title': None,'showgrid' : False, 'showline' : False, 'showticklabels' : False},
                                    xaxis = {'title': None,'showgrid' : False}
                                    ).update_traces(
                                                    #hovertemplate = df_2_kredi_türü["Kredi Türü"]+ ' : ' + df_2_kredi_türü["NPL"],
                                                    textposition ='top center',
                                                    cliponaxis = False,
                                                    line_color = color_palette_blue[0]
                                                    )                    

 

    
 
              
            #graph-output_04_apricot_1
            ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'y': (df_2_roll_rate_1['Ay'].values.tolist()), 'x': (df_2_roll_rate_1['Roll Rate %'].values.tolist()), 'type': 'bar', 'name': df_2_roll_rate_1['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_roll_rate_1['Roll Rate %'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'text', 'hoverlabel':{'font':{'size':12}} ,'orientation': 'h'}
                                            ],
                                    'layout':   {
                                                    'height' : 495,
                                                    'width' : 250,
                                                    'title': ' Bucket-1', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'yaxis': {'showgrid' : False, 'showline' : True, 'showticklabels' : True, 'tickvals': df_2_roll_rate_1['Ay'], 'ticktext': df_2_roll_rate_1['Ay']},
                                                    'margin' : {'l': 50,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_04_apricot_2
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'y': (df_2_roll_rate_2['Ay'].values.tolist()), 'x': (df_2_roll_rate_2['Roll Rate %'].values.tolist()), 'type': 'bar', 'name': df_2_roll_rate_2['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_roll_rate_2['Roll Rate %'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'text', 'hoverlabel':{'font':{'size':12}} ,'orientation': 'h'}
                                            ],
                                    'layout':   {
                                                    'height' : 495,
                                                    'width' : 250,
                                                    'title': ' Bucket-2', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'yaxis': {'showgrid' : False, 'showline' : True, 'showticklabels' : False, 'tickvals': df_2_roll_rate_2['Ay'], 'ticktext': df_2_roll_rate_2['Ay']},
                                                    'margin' : {'l': 50,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_04_apricot_3
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'y': (df_2_roll_rate_3['Ay'].values.tolist()), 'x': (df_2_roll_rate_3['Roll Rate %'].values.tolist()), 'type': 'bar', 'name': df_2_roll_rate_3['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_roll_rate_3['Roll Rate %'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'text', 'hoverlabel':{'font':{'size':12}} ,'orientation': 'h'}
                                            ],
                                    'layout':   {
                                                    'height' : 495,
                                                    'width' : 250,
                                                    'title': ' Bucket-3', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'yaxis': {'showgrid' : False, 'showline' : True, 'showticklabels' : False, 'tickvals': df_2_roll_rate_3['Ay'], 'ticktext': df_2_roll_rate_3['Ay']},
                                                    'margin' : {'l': 50,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_04_apricot_4
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'y': (df_2_roll_rate_4['Ay'].values.tolist()), 'x': (df_2_roll_rate_4['Roll Rate %'].values.tolist()), 'type': 'bar', 'name': df_2_roll_rate_4['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_roll_rate_4['Roll Rate %'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'text', 'hoverlabel':{'font':{'size':12}} ,'orientation': 'h'}
                                            ],
                                    'layout':   {
                                                    'height' : 495,
                                                    'width' : 250,
                                                    'title': ' NPL', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'yaxis': {'showgrid' : False, 'showline' : True, 'showticklabels' : False, 'tickvals': df_2_roll_rate_4['Ay'], 'ticktext': df_2_roll_rate_4['Ay']},
                                                    'margin' : {'l': 50,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_04_apricot_5
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'y': (df_2_roll_rate_5['Ay'].values.tolist()), 'x': (df_2_roll_rate_5['Roll Rate %'].values.tolist()), 'type': 'bar', 'name': df_2_roll_rate_5['Ay'].values.tolist(), 'marker' : {'color': color_palette_blue_2},'text' : df_2_roll_rate_5['Roll Rate %'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'text', 'hoverlabel':{'font':{'size':12}} ,'orientation': 'h'}
                                            ],
                                    'layout':   {
                                                    'height' : 495,
                                                    'width' : 250,
                                                    'title': ' Aylık NPL Dönüşüm %', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'yaxis': {'showgrid' : False, 'showline' : True, 'showticklabels' : False, 'tickvals': df_2_roll_rate_5['Ay'], 'ticktext': df_2_roll_rate_5['Ay']},
                                                    'margin' : {'l': 50,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_04_mango
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'x': (df_2_kredituru_nplpct['Kredi Türü'].values.tolist()), 'y': (df_2_kredituru_nplpct['NPL Aktarım %'].values.tolist()), 'type': 'bar', 'name': df_2_kredituru_nplpct['Kredi Türü'].values.tolist(), 'marker' : {'color': color_palette_heatmap_pale_6},'text' : df_2_kredituru_nplpct['NPL Aktarım %'],'textposition':'outside', 'textfont':{'color':'auto'},'hoverinfo' : 'x+text', 'cliponaxis': False}
                                            ],
                                    'layout':   {
                                                    'height' : 225,
                                                    'width' : 575,
                                                    'title': ' Kredi Türü Bazında Aylık NPL Dönüşüm Oranı', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': df_2_kredituru_nplpct['Kredi Türü'], 'ticktext': df_2_kredituru_nplpct['Kredi Türü']},
                                                    'margin' : {'l': 10,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              
    #graph-output_04_coconut
    ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'x': (kredi_turu_recovery_pct['Kredi Türü'].values.tolist()), 'y': (kredi_turu_recovery_pct['12. Ay NPL Tahsilat %'].values.tolist()), 'type': 'bar', 'name': kredi_turu_recovery_pct['Kredi Türü'].values.tolist(), 'marker' : {'color': color_palette_heatmap_pale_6_descending},'text' : kredi_turu_recovery_pct['12. Ay NPL Tahsilat %'],'textposition':'outside', 'textfont':{'color':'auto'},'hoverinfo' : 'x+text', 'cliponaxis': False}
                                            ],
                                    'layout':   {
                                                    'height' : 225,
                                                    'width' : 575,
                                                    'title': ' Kredi Türü Bazında 12. Ay NPL Tahsilat Oranı', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': kredi_turu_recovery_pct['Kredi Türü'], 'ticktext': kredi_turu_recovery_pct['Kredi Türü']},
                                                    'margin' : {'l': 10,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }

 
              

    )              







        
#tab-6 callback begins here
@app.callback([Output('card-output_06_apple', 'children'),Output('card-output_06_orange', 'children'),Output('card-output_06_banana', 'children'),Output('graph-output_06_apple', 'children'),Output('graph-output_06_orange', 'children'),Output('graph-output_06_banana', 'children'),Output('graph-output_06_lemon', 'children'),Output('graph-output_06_cherry', 'children')],
              [Input('Bölge_Filtresi_tab6', 'value'),
              Input('Kredi Türü_Filtresi_tab6', 'value'),
              Input('Segment_Filtresi_tab6', 'value'),
              Input('Şube_Filtresi_tab6', 'value')
               ]) 


def update_value_6(input_1, input_2, input_3, input_4):
    
        df_2 = df_6


        # BÖLGE FİLTRESİ    
        if input_1 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Bölge'] == input_1]  
    
       
        
        # KREDİ TÜRÜ FİLTRESİ    
        if input_2 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Kredi Türü'] == input_2]  
    
       
        
        # SEGMENT FİLTRESİ    
        if input_3 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Segment'] == input_3]  
    
    
    
        # ŞUBE FİLTRESİ    
        if input_4 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Şube'] == input_4] 
    

    
    
        last_month_recovery = df_2[df_2['Ay_2'] == max(df_2['Ay_2'])]
        last_month_recovery = round(sum(last_month_recovery['Tahsilat-12']),1)

    
    
        df_2 = df_6
        
        # BÖLGE FİLTRESİ    
        if input_1 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Bölge'] == input_1]  
    
       
        
        # KREDİ TÜRÜ FİLTRESİ    
        if input_2 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Kredi Türü'] == input_2]  
    
       
        
        # SEGMENT FİLTRESİ    
        if input_3 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Segment'] == input_3]  
    
    
    
        # ŞUBE FİLTRESİ    
        if input_4 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Şube'] == input_4] 


    
    
        total_recovery = round(sum(df_2['Tahsilat-12']),1)                                                                           

        total_recovery_pct = sum(df_2['Tahsilat-12'])/sum(df_2['NPL'])
        total_recovery_pct = str(round(total_recovery_pct * 100,1))+'%'
        

        df_2 = df_6


        # BÖLGE FİLTRESİ    
        if input_1 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Bölge'] == input_1]  
    
       
        
        # KREDİ TÜRÜ FİLTRESİ    
        if input_2 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Kredi Türü'] == input_2]  
    
       
        
        # SEGMENT FİLTRESİ    
        if input_3 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Segment'] == input_3]  
    
    
    
        # ŞUBE FİLTRESİ    
        if input_4 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Şube'] == input_4] 





        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2['Tahsilat-1']),sum(df_2['Tahsilat-2']),sum(df_2['Tahsilat-3']),sum(df_2['Tahsilat-4']),sum(df_2['Tahsilat-5']),sum(df_2['Tahsilat-6']),sum(df_2['Tahsilat-7']),sum(df_2['Tahsilat-8']),sum(df_2['Tahsilat-9']),sum(df_2['Tahsilat-10']),sum(df_2['Tahsilat-11']),sum(df_2['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'    
        recovery_vintage_all = recovery_vintage




        df_2 = df_6

        
        # KREDİ TÜRÜ FİLTRESİ    
        if input_2 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Kredi Türü'] == input_2]  
    
       
        
        # SEGMENT FİLTRESİ    
        if input_3 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Segment'] == input_3]  
    

    
        bolge_recovery_pct = df_2.groupby(['Bölge'])['NPL'].sum(),df_2.groupby(['Bölge'])['Tahsilat-12'].sum()
        bolge_recovery_pct = pd.DataFrame(list( bolge_recovery_pct))
        bolge_recovery_pct.reset_index(drop=True, inplace=True)
        bolge_recovery_pct = bolge_recovery_pct.T
        bolge_recovery_pct.reset_index(drop=False, inplace=True)
        bolge_recovery_pct = bolge_recovery_pct.rename(columns = {0:'NPL', 1:'Recovery'})
        bolge_recovery_pct['12. Ay NPL Tahsilat %'] = bolge_recovery_pct['Recovery'] / bolge_recovery_pct['NPL']
        bolge_recovery_pct = bolge_recovery_pct[['Bölge','12. Ay NPL Tahsilat %']]
        bolge_recovery_pct = bolge_recovery_pct.sort_values(by=['12. Ay NPL Tahsilat %'],  ascending=[False])
        bolge_recovery_pct['12. Ay NPL Tahsilat %']= ((bolge_recovery_pct['12. Ay NPL Tahsilat %'] * 100).round(1)).astype(str) + '%'    
        






        df_2 = df_6


        # BÖLGE FİLTRESİ    
        if input_1 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Bölge'] == input_1]  
    
       
        
        # KREDİ TÜRÜ FİLTRESİ    
        if input_2 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Kredi Türü'] == input_2]  
    

    
        # ŞUBE FİLTRESİ    
        if input_4 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Şube'] == input_4] 


        
        
        df_2_bireysel_kitle = df_2[df_2['Segment'] == 'Bireysel Kitle']
        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2_bireysel_kitle['Tahsilat-1']),sum(df_2_bireysel_kitle['Tahsilat-2']),sum(df_2_bireysel_kitle['Tahsilat-3']),sum(df_2_bireysel_kitle['Tahsilat-4']),sum(df_2_bireysel_kitle['Tahsilat-5']),sum(df_2_bireysel_kitle['Tahsilat-6']),sum(df_2_bireysel_kitle['Tahsilat-7']),sum(df_2_bireysel_kitle['Tahsilat-8']),sum(df_2_bireysel_kitle['Tahsilat-9']),sum(df_2_bireysel_kitle['Tahsilat-10']),sum(df_2_bireysel_kitle['Tahsilat-11']),sum(df_2_bireysel_kitle['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2_bireysel_kitle['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'
        recovery_vintage['Segment'] = 'Bireysel Kitle'  
        df_2_bireysel_kitle = recovery_vintage
        df_2_bireysel_kitle = df_2_bireysel_kitle[(df_2_bireysel_kitle['Ay'] == 3) | (df_2_bireysel_kitle['Ay'] == 6) | (df_2_bireysel_kitle['Ay'] == 9) | (df_2_bireysel_kitle['Ay'] == 12)]
        
        
        
        
        df_2_bireysel_portfoy = df_2[df_2['Segment'] == 'Bireysel Portföy']
        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2_bireysel_portfoy['Tahsilat-1']),sum(df_2_bireysel_portfoy['Tahsilat-2']),sum(df_2_bireysel_portfoy['Tahsilat-3']),sum(df_2_bireysel_portfoy['Tahsilat-4']),sum(df_2_bireysel_portfoy['Tahsilat-5']),sum(df_2_bireysel_portfoy['Tahsilat-6']),sum(df_2_bireysel_portfoy['Tahsilat-7']),sum(df_2_bireysel_portfoy['Tahsilat-8']),sum(df_2_bireysel_portfoy['Tahsilat-9']),sum(df_2_bireysel_portfoy['Tahsilat-10']),sum(df_2_bireysel_portfoy['Tahsilat-11']),sum(df_2_bireysel_portfoy['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2_bireysel_portfoy['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'
        recovery_vintage['Segment'] = 'Bireysel Portföy'  
        df_2_bireysel_portfoy = recovery_vintage
        df_2_bireysel_portfoy = df_2_bireysel_portfoy[(df_2_bireysel_portfoy['Ay'] == 3) | (df_2_bireysel_portfoy['Ay'] == 6) | (df_2_bireysel_portfoy['Ay'] == 9) | (df_2_bireysel_portfoy['Ay'] == 12)]
        
        
        
        df_2_ozel_birikim = df_2[df_2['Segment'] == 'Özel Birikim']
        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2_ozel_birikim['Tahsilat-1']),sum(df_2_ozel_birikim['Tahsilat-2']),sum(df_2_ozel_birikim['Tahsilat-3']),sum(df_2_ozel_birikim['Tahsilat-4']),sum(df_2_ozel_birikim['Tahsilat-5']),sum(df_2_ozel_birikim['Tahsilat-6']),sum(df_2_ozel_birikim['Tahsilat-7']),sum(df_2_ozel_birikim['Tahsilat-8']),sum(df_2_ozel_birikim['Tahsilat-9']),sum(df_2_ozel_birikim['Tahsilat-10']),sum(df_2_ozel_birikim['Tahsilat-11']),sum(df_2_ozel_birikim['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2_ozel_birikim['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'
        recovery_vintage['Segment'] = 'Özel Birikim'  
        df_2_ozel_birikim = recovery_vintage
        df_2_ozel_birikim = df_2_ozel_birikim[(df_2_ozel_birikim['Ay'] == 3) | (df_2_ozel_birikim['Ay'] == 6) | (df_2_ozel_birikim['Ay'] == 9) | (df_2_ozel_birikim['Ay'] == 12)]
        
        
        
        df_2_segment_recovery = df_2_bireysel_kitle.append([df_2_bireysel_portfoy,df_2_ozel_birikim])
        df_2_segment_recovery_3_ay_tahsilat = df_2_segment_recovery[df_2_segment_recovery['Ay']==3]
        df_2_segment_recovery_6_ay_tahsilat = df_2_segment_recovery[df_2_segment_recovery['Ay']==6]
        df_2_segment_recovery_9_ay_tahsilat = df_2_segment_recovery[df_2_segment_recovery['Ay']==9]
        df_2_segment_recovery_12_ay_tahsilat = df_2_segment_recovery[df_2_segment_recovery['Ay']==12]










        df_2 = df
        
        # BÖLGE FİLTRESİ    
        if input_1 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Bölge'] == input_1]  
    
       
        
        # KREDİ TÜRÜ FİLTRESİ    
        if input_2 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Kredi Türü'] == input_2]  
    
       
        
        # SEGMENT FİLTRESİ    
        if input_3 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Segment'] == input_3]  
    
    
    
        # ŞUBE FİLTRESİ    
        if input_4 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Şube'] == input_4] 




        ofis_recovery_pct = df_2.groupby(['Tahsilat Ofisi'])['NPL'].sum(),df_2.groupby(['Tahsilat Ofisi'])['Tahsilat-12'].sum()
        ofis_recovery_pct = pd.DataFrame(list( ofis_recovery_pct))
        ofis_recovery_pct.reset_index(drop=True, inplace=True)
        ofis_recovery_pct = ofis_recovery_pct.T
        ofis_recovery_pct.reset_index(drop=False, inplace=True)
        ofis_recovery_pct = ofis_recovery_pct.rename(columns = {0:'NPL', 1:'Recovery'})
        ofis_recovery_pct['12. Ay NPL Tahsilat %'] = ofis_recovery_pct['Recovery'] / ofis_recovery_pct['NPL']
        ofis_recovery_pct = ofis_recovery_pct[['Tahsilat Ofisi','12. Ay NPL Tahsilat %']]
        ofis_recovery_pct = ofis_recovery_pct.sort_values(by=['12. Ay NPL Tahsilat %'],  ascending=[False])
        ofis_recovery_pct['12. Ay NPL Tahsilat %']= ((ofis_recovery_pct['12. Ay NPL Tahsilat %'] * 100).round(1)).astype(str) + '%'        
  
        
        


        df_2 = df_6
        
        # BÖLGE FİLTRESİ    
        if input_1 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Bölge'] == input_1]  
    
       
        
        # KREDİ TÜRÜ FİLTRESİ    
        if input_2 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Kredi Türü'] == input_2]  
    
       
        
        # SEGMENT FİLTRESİ    
        if input_3 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Segment'] == input_3]  
    



        sube_recovery_pct = df_2.groupby(['Şube'])['NPL'].sum(),df_2.groupby(['Şube'])['Tahsilat-12'].sum()
        sube_recovery_pct = pd.DataFrame(list( sube_recovery_pct))
        sube_recovery_pct.reset_index(drop=True, inplace=True)
        sube_recovery_pct = sube_recovery_pct.T
        sube_recovery_pct.reset_index(drop=False, inplace=True)
        sube_recovery_pct = sube_recovery_pct.rename(columns = {0:'NPL', 1:'Recovery'})
        sube_recovery_pct['12. Ay NPL Tahsilat %'] = sube_recovery_pct['Recovery'] / sube_recovery_pct['NPL']
        sube_recovery_pct = sube_recovery_pct[['Şube','12. Ay NPL Tahsilat %']]
        sube_recovery_pct = sube_recovery_pct.sort_values(by=['12. Ay NPL Tahsilat %'],  ascending=[False])
        sube_recovery_pct['12. Ay NPL Tahsilat %']= ((sube_recovery_pct['12. Ay NPL Tahsilat %'] * 100).round(1)).astype(str) + '%'        
        sube_recovery_pct = sube_recovery_pct.head(5)
        sube_recovery_pct  
        
        
        


        df_2 = df_6


        # BÖLGE FİLTRESİ    
        if input_1 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Bölge'] == input_1]  
    
       
        
        # SEGMENT FİLTRESİ    
        if input_3 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Segment'] == input_3]  
    
    
    
        # ŞUBE FİLTRESİ    
        if input_4 == 'All':
            df_2 = df_2
        else :
            df_2 = df_2[df_2['Şube'] == input_4] 



        
        
        df_2_yapılandırma = df_2[df_2['Kredi Türü'] == 'Yapılandırma']
        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2_yapılandırma['Tahsilat-1']),sum(df_2_yapılandırma['Tahsilat-2']),sum(df_2_yapılandırma['Tahsilat-3']),sum(df_2_yapılandırma['Tahsilat-4']),sum(df_2_yapılandırma['Tahsilat-5']),sum(df_2_yapılandırma['Tahsilat-6']),sum(df_2_yapılandırma['Tahsilat-7']),sum(df_2_yapılandırma['Tahsilat-8']),sum(df_2_yapılandırma['Tahsilat-9']),sum(df_2_yapılandırma['Tahsilat-10']),sum(df_2_yapılandırma['Tahsilat-11']),sum(df_2_yapılandırma['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2_yapılandırma['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'
        recovery_vintage['Kredi Türü'] = 'Yapılandırma'  
        df_2_yapılandırma = recovery_vintage
        df_2_yapılandırma = df_2_yapılandırma[(df_2_yapılandırma['Ay'] == 3) | (df_2_yapılandırma['Ay'] == 6) | (df_2_yapılandırma['Ay'] == 9) | (df_2_yapılandırma['Ay'] == 12)]
                    
        
        
        
        df_2_kmh = df_2[df_2['Kredi Türü'] == 'KMH']
        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2_kmh['Tahsilat-1']),sum(df_2_kmh['Tahsilat-2']),sum(df_2_kmh['Tahsilat-3']),sum(df_2_kmh['Tahsilat-4']),sum(df_2_kmh['Tahsilat-5']),sum(df_2_kmh['Tahsilat-6']),sum(df_2_kmh['Tahsilat-7']),sum(df_2_kmh['Tahsilat-8']),sum(df_2_kmh['Tahsilat-9']),sum(df_2_kmh['Tahsilat-10']),sum(df_2_kmh['Tahsilat-11']),sum(df_2_kmh['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2_kmh['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'
        recovery_vintage['Kredi Türü'] = 'KMH'  
        df_2_kmh = recovery_vintage
        df_2_kmh = df_2_kmh[(df_2_kmh['Ay'] == 3) | (df_2_kmh['Ay'] == 6) | (df_2_kmh['Ay'] == 9) | (df_2_kmh['Ay'] == 12)]
        
        
        
        
        df_2_kredi_kartı = df_2[df_2['Kredi Türü'] == 'Kredi Kartı']
        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2_kredi_kartı['Tahsilat-1']),sum(df_2_kredi_kartı['Tahsilat-2']),sum(df_2_kredi_kartı['Tahsilat-3']),sum(df_2_kredi_kartı['Tahsilat-4']),sum(df_2_kredi_kartı['Tahsilat-5']),sum(df_2_kredi_kartı['Tahsilat-6']),sum(df_2_kredi_kartı['Tahsilat-7']),sum(df_2_kredi_kartı['Tahsilat-8']),sum(df_2_kredi_kartı['Tahsilat-9']),sum(df_2_kredi_kartı['Tahsilat-10']),sum(df_2_kredi_kartı['Tahsilat-11']),sum(df_2_kredi_kartı['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2_kredi_kartı['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'
        recovery_vintage['Kredi Türü'] = 'Kredi Kartı'  
        df_2_kredi_kartı = recovery_vintage
        df_2_kredi_kartı = df_2_kredi_kartı[(df_2_kredi_kartı['Ay'] == 3) | (df_2_kredi_kartı['Ay'] == 6) | (df_2_kredi_kartı['Ay'] == 9) | (df_2_kredi_kartı['Ay'] == 12)]
        
        
        
        df_2_kredi_ihtiyac = df_2[df_2['Kredi Türü'] == 'İhtiyaç']
        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2_kredi_ihtiyac['Tahsilat-1']),sum(df_2_kredi_ihtiyac['Tahsilat-2']),sum(df_2_kredi_ihtiyac['Tahsilat-3']),sum(df_2_kredi_ihtiyac['Tahsilat-4']),sum(df_2_kredi_ihtiyac['Tahsilat-5']),sum(df_2_kredi_ihtiyac['Tahsilat-6']),sum(df_2_kredi_ihtiyac['Tahsilat-7']),sum(df_2_kredi_ihtiyac['Tahsilat-8']),sum(df_2_kredi_ihtiyac['Tahsilat-9']),sum(df_2_kredi_ihtiyac['Tahsilat-10']),sum(df_2_kredi_ihtiyac['Tahsilat-11']),sum(df_2_kredi_ihtiyac['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2_kredi_ihtiyac['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'
        recovery_vintage['Kredi Türü'] = 'İhtiyaç'  
        df_2_kredi_ihtiyac = recovery_vintage
        df_2_kredi_ihtiyac = df_2_kredi_ihtiyac[(df_2_kredi_ihtiyac['Ay'] == 3) | (df_2_kredi_ihtiyac['Ay'] == 6) | (df_2_kredi_ihtiyac['Ay'] == 9) | (df_2_kredi_ihtiyac['Ay'] == 12)]
        
        
        
        
        
        df_2_kredi_tasit = df_2[df_2['Kredi Türü'] == 'Taşıt']
        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2_kredi_tasit['Tahsilat-1']),sum(df_2_kredi_tasit['Tahsilat-2']),sum(df_2_kredi_tasit['Tahsilat-3']),sum(df_2_kredi_tasit['Tahsilat-4']),sum(df_2_kredi_tasit['Tahsilat-5']),sum(df_2_kredi_tasit['Tahsilat-6']),sum(df_2_kredi_tasit['Tahsilat-7']),sum(df_2_kredi_tasit['Tahsilat-8']),sum(df_2_kredi_tasit['Tahsilat-9']),sum(df_2_kredi_tasit['Tahsilat-10']),sum(df_2_kredi_tasit['Tahsilat-11']),sum(df_2_kredi_tasit['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2_kredi_tasit['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'
        recovery_vintage['Kredi Türü'] = 'Taşıt'  
        df_2_kredi_tasit = recovery_vintage
        df_2_kredi_tasit = df_2_kredi_tasit[(df_2_kredi_tasit['Ay'] == 3) | (df_2_kredi_tasit['Ay'] == 6) | (df_2_kredi_tasit['Ay'] == 9) | (df_2_kredi_tasit['Ay'] == 12)]
        
        
        
        
        df_2_kredi_konut = df_2[df_2['Kredi Türü'] == 'Konut']
        recovery_vintage_ay = list(range(0,13))
        recovery_vintage_tahsilat = [0,sum(df_2_kredi_konut['Tahsilat-1']),sum(df_2_kredi_konut['Tahsilat-2']),sum(df_2_kredi_konut['Tahsilat-3']),sum(df_2_kredi_konut['Tahsilat-4']),sum(df_2_kredi_konut['Tahsilat-5']),sum(df_2_kredi_konut['Tahsilat-6']),sum(df_2_kredi_konut['Tahsilat-7']),sum(df_2_kredi_konut['Tahsilat-8']),sum(df_2_kredi_konut['Tahsilat-9']),sum(df_2_kredi_konut['Tahsilat-10']),sum(df_2_kredi_konut['Tahsilat-11']),sum(df_2_kredi_konut['Tahsilat-12'])]
        recovery_vintage_ay = pd.DataFrame(recovery_vintage_ay, columns = ['Ay'])
        recovery_vintage_tahsilat = pd.DataFrame(recovery_vintage_tahsilat, columns = ['Tahsilat'])
        recovery_vintage = pd.concat([recovery_vintage_ay, recovery_vintage_tahsilat], axis=1)
        recovery_vintage['Tahsilat%'] = recovery_vintage['Tahsilat'] / sum(df_2_kredi_konut['NPL'])
        recovery_vintage['Tahsilat%%']= ((recovery_vintage['Tahsilat%'] * 100).round(1)).astype(str) + '%'
        recovery_vintage['Kredi Türü'] = 'Konut'  
        df_2_kredi_konut = recovery_vintage
        df_2_kredi_konut = df_2_kredi_konut[(df_2_kredi_konut['Ay'] == 3) | (df_2_kredi_konut['Ay'] == 6) | (df_2_kredi_konut['Ay'] == 9) | (df_2_kredi_konut['Ay'] == 12)]
        
        
        
        
        
        df_2_kredi_turu_recovery = df_2_yapılandırma.append([df_2_kmh,df_2_kredi_kartı,df_2_kredi_ihtiyac,df_2_kredi_tasit,df_2_kredi_konut])

        
        df_2_kredi_turu_recovery_3_ay_tahsilat = df_2_kredi_turu_recovery[df_2_kredi_turu_recovery['Ay']==3]
        df_2_kredi_turu_recovery_6_ay_tahsilat = df_2_kredi_turu_recovery[df_2_kredi_turu_recovery['Ay']==6]
        df_2_kredi_turu_recovery_9_ay_tahsilat = df_2_kredi_turu_recovery[df_2_kredi_turu_recovery['Ay']==9]
        df_2_kredi_turu_recovery_12_ay_tahsilat = df_2_kredi_turu_recovery[df_2_kredi_turu_recovery['Ay']==12]
            
                
                
                
        
        
        
        
        
        
        
        

        #card-output_06_apple
        return html.H1(last_month_recovery, style={"color": "white","background": color_palette_blue[3], 'textAlign': 'center', 'width':'75%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '250%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '-20%', 'margin-left': '22%'}
        
        
    
        #card-output_06_orange          
              ),html.H1(total_recovery, style={"color": "white","background": color_palette_blue[1], 'textAlign': 'center', 'width':'75%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '250%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '-20%', 'margin-left': '22%'}                              
       


        #card-output_06_banana          
              ),html.H1(total_recovery_pct, style={"color": "white","background": color_palette_blue[0], 'textAlign': 'center', 'width':'75%', 'display': 'inline-block', 'font-family': "Calibri" , 'font-size': '250%' ,'justify-content': 'center', 'font-style': 'italic', 'margin-top': '-20%', 'margin-left': '22%'}                              
       

            #graph-output_06_apple            
            ),dcc.Graph(

                
                        figure = px.area(
                            recovery_vintage_all, 
                            x="Ay", 
                            y="Tahsilat%",  
                            title=" NPL Tahsilat Vintage Eğrisi", 
                            height = 300,
                            width = 800,
                            text = 'Tahsilat%%'
                            ).update_layout(
                                    title = {'pad':{'l':185}},
                                    paper_bgcolor = 'rgba(0,0,0,0)',
                                    plot_bgcolor = 'rgba(0,0,0,0)',
                                    margin={"r":40,"t":40,"l":90,"b":40},
                                    yaxis = {'title': None,'showgrid' : False, 'showline' : True, 'showticklabels' : False,'tickformat': ',.0%', 'linecolor': '#E5E8E8'},
                                    xaxis = {'title': 'Takipte Geçen Süre (Ay)','showgrid' : False, 'showline' : False, 'linecolor': '#99A3A4'}
                                    ).update_traces(
                                                    hovertemplate = '%{x}. Ay: %{text}',
                                                    textposition ='top center',
                                                    cliponaxis = False,
                                                    line_color = color_palette_blue[0]
                                                    )    
                
                
            



            #graph-output_06_orange
            ),dcc.Graph(
                        figure={
                                    'data': [
                                                {'x': (ofis_recovery_pct['Tahsilat Ofisi'].values.tolist()), 'y': (ofis_recovery_pct['12. Ay NPL Tahsilat %'].values.tolist()), 'type': 'bar', 'name': ofis_recovery_pct['Tahsilat Ofisi'].values.tolist(), 'marker' : {'color': color_palette_heatmap_pale_2_descending},'text' : ofis_recovery_pct['12. Ay NPL Tahsilat %'],'textposition':'outside', 'textfont':{'color':'auto'},'hoverinfo' : 'x+text', 'cliponaxis': False}
                                            ],
                                    'layout':   {
                                                    'height' : 315,
                                                    'width' : 550,
                                                    'title': {'text':' Tahsilat Ofisi Bazında' '12. Ay NPL Tahsilat Oranı (%)','pad':{'l':0}, 'font':{'size':15} },
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': ofis_recovery_pct['Tahsilat Ofisi'], 'ticktext': ofis_recovery_pct['Tahsilat Ofisi']},
                                                    'margin' : {'l': 150,'r': 100,'t': 60,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }
                
                
 

 
            #graph-output_06_banana              
            ),dcc.Graph(
                        
                        figure={
                                    'data': [
                                                {'x': (df_2_segment_recovery_3_ay_tahsilat['Segment'].values.tolist()), 'y': (df_2_segment_recovery_3_ay_tahsilat['Tahsilat%'].values.tolist()), 'type': 'bar', 'name': '3. Ay', 'marker' : {'color': color_palette_blue[0]},'text' : df_2_segment_recovery_3_ay_tahsilat['Tahsilat%%'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'name+text'},
                                                {'x': (df_2_segment_recovery_6_ay_tahsilat['Segment'].values.tolist()), 'y': (df_2_segment_recovery_6_ay_tahsilat['Tahsilat%'].values.tolist()), 'type': 'bar', 'name': '6. Ay', 'marker' : {'color': color_palette_blue[1]},'text' : df_2_segment_recovery_6_ay_tahsilat['Tahsilat%%'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'name+text'},
                                                {'x': (df_2_segment_recovery_9_ay_tahsilat['Segment'].values.tolist()), 'y': (df_2_segment_recovery_9_ay_tahsilat['Tahsilat%'].values.tolist()), 'type': 'bar', 'name': '9. Ay', 'marker' : {'color': color_palette_blue[2]},'text' : df_2_segment_recovery_9_ay_tahsilat['Tahsilat%%'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'name+text'},
                                                {'x': (df_2_segment_recovery_12_ay_tahsilat['Segment'].values.tolist()), 'y': (df_2_segment_recovery_12_ay_tahsilat['Tahsilat%'].values.tolist()), 'type': 'bar', 'name': '12. Ay', 'marker' : {'color': color_palette_blue[3]},'text' : df_2_segment_recovery_12_ay_tahsilat['Tahsilat%%'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'name+text'},
                                            ],
                                    'layout':   {
                                                    'height' : 250,
                                                    'width' : 1100,
                                                    'title': ' Segment Bazında İlk 3-6-9-12 Ay NPL Tahsilat %', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': df_2_segment_recovery_3_ay_tahsilat['Segment'], 'ticktext': df_2_segment_recovery_3_ay_tahsilat['Segment']},
                                                    'margin' : {'l': 40,'r': 40,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }
                    

            #graph-output_06_lemon
            ),dcc.Graph(
                
                        figure={
                                    'data': [
                                                {'x': (bolge_recovery_pct['Bölge'].values.tolist()), 'y': (bolge_recovery_pct['12. Ay NPL Tahsilat %'].values.tolist()), 'type': 'bar', 'name': bolge_recovery_pct['Bölge'].values.tolist(), 'marker' : {'color': color_palette_heatmap_pale_10_descending},'text' : bolge_recovery_pct['12. Ay NPL Tahsilat %'],'textposition':'outside', 'textfont':{'color':'auto'},'hoverinfo' : 'x+text', 'cliponaxis': False}
                                            ],
                                    'layout':   {
                                                    'height' : 250,
                                                    'width' : 750,
                                                    'title': ' Bölge Bazında 12. Ay NPL Tahsilat Oranı (%)', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': bolge_recovery_pct['Bölge'], 'ticktext': bolge_recovery_pct['Bölge']},
                                                    'margin' : {'l': 100,'r': 0,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }


    
            #graph-output_06_cherry    
            ),dcc.Graph(
                        
                        figure={
                                    'data': [
                                                {'x': (df_2_kredi_turu_recovery_3_ay_tahsilat['Kredi Türü'].values.tolist()), 'y': (df_2_kredi_turu_recovery_3_ay_tahsilat['Tahsilat%'].values.tolist()), 'type': 'bar', 'name': '3. Ay', 'marker' : {'color': color_palette_blue[0]},'text' : df_2_kredi_turu_recovery_3_ay_tahsilat['Tahsilat%%'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'name+text'},
                                                {'x': (df_2_kredi_turu_recovery_6_ay_tahsilat['Kredi Türü'].values.tolist()), 'y': (df_2_kredi_turu_recovery_6_ay_tahsilat['Tahsilat%'].values.tolist()), 'type': 'bar', 'name': '6. Ay', 'marker' : {'color': color_palette_blue[1]},'text' : df_2_kredi_turu_recovery_6_ay_tahsilat['Tahsilat%%'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'name+text'},
                                                {'x': (df_2_kredi_turu_recovery_9_ay_tahsilat['Kredi Türü'].values.tolist()), 'y': (df_2_kredi_turu_recovery_9_ay_tahsilat['Tahsilat%'].values.tolist()), 'type': 'bar', 'name': '9. Ay', 'marker' : {'color': color_palette_blue[2]},'text' : df_2_kredi_turu_recovery_9_ay_tahsilat['Tahsilat%%'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'name+text'},
                                                {'x': (df_2_kredi_turu_recovery_12_ay_tahsilat['Kredi Türü'].values.tolist()), 'y': (df_2_kredi_turu_recovery_12_ay_tahsilat['Tahsilat%'].values.tolist()), 'type': 'bar', 'name': '12. Ay', 'marker' : {'color': color_palette_blue[3]},'text' : df_2_kredi_turu_recovery_12_ay_tahsilat['Tahsilat%%'],'textposition':'auto', 'textfont':{'color':'white'},'hoverinfo' : 'name+text'},
                                            ],
                                    'layout':   {
                                                    'height' : 250,
                                                    'width' : 1850,
                                                    'title': ' Kredi Türü Bazında İlk 3-6-9-12 Ay NPL Tahsilat %', 
                                                    'plot_bgcolor': 'rgba(0,0,0,0)' ,
                                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                                    'font': {'color': '#5D6D7E'},
                                                    'yaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : False, 'range' : 'auto'},
                                                    'xaxis': {'showgrid' : False, 'showline' : False, 'showticklabels' : True, 'tickvals': df_2_kredi_turu_recovery_3_ay_tahsilat['Kredi Türü'], 'ticktext': df_2_kredi_turu_recovery_3_ay_tahsilat['Kredi Türü']},
                                                    'margin' : {'l': 80,'r': 0,'t': 40,'b': 70},
                                                    'legend' : {'x': 1,'y': 0.5,'orientation': 'v', 'itemclick': 'toggleothers'}
                                                }
                                }
                    


            )


               


                        
if __name__ == '__main__':
    app.run_server()
