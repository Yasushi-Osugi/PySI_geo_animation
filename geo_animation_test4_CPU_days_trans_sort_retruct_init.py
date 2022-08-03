
#
# geo and animation
#
# https://qiita.com/Ringa_hyj/items/68241f78d0e440680be3
#
# common_plan_unit@220726_map_data_test.csv
#

import plotly.express as px

import pandas as pd

#
#df = px.data.gapminder()
#
# capital_jp


#filename = 'geo_test_YTO.csv'

#filename = 'CPU_days_trans_geo_YTO.csv'

filename = 'CPU_days_trans_geo.csv'

# ***********************
#
#seq_no,control_flag,priority_no,modal,LT,Dpt_entity,Dpt_week,Dpt_step,Arv_entity,Arv_week,Arv_step,node_name,capital_en,name_ens,capital_jp,iscapital,lat,lon,node_name_Arv,capital_en_Arv,name_ens_Arv,capital_jp_Arv,iscapital_Arv,lat_Arv,lon_Arv,Dpt_day,lat_day,lon_day

#YTOLEAF202301009,F,1202301009,B,2,YTO,-1,0,YTOLEAF,1,0,YTO,Toronto,Canada,トロント,0,43.6534399,-79.3840901,YTO,Toronto,Canada,トロント,0,43.65794658648729,-79.3840901,-1.0,43.65434123729746,-79.3840901

#YTOLEAF202301009,F,1202301009,B,2,YTO,-1,0,YTOLEAF,1,0,YTO,Toronto,Canada,トロント,0,43.6534399,-79.3840901,YTO,Toronto,Canada,トロント,0,43.65794658648729,-79.3840901,-0.8,43.65434123729746,-79.3840901

#YTOLEAF202301009,F,1202301009,B,2,YTO,-1,0,YTOLEAF,1,0,YTO,Toronto,Canada,トロント,0,43.6534399,-79.3840901,YTO,Toronto,Canada,トロント,0,43.65794658648729,-79.3840901,-0.6,43.65434123729746,-79.3840901
#
# ***********************



df = pd.read_csv(filename)
print(df)


df_init_sort = df.sort_values(by=["Dpt_day" ])



americas = ["YTOLEAF","NYC_N","NYC_D","NYC_I","LAX_N","LAX_D","LAX_I","SFOLEAF","YTO","NYC","LAX"]

germany = ['HAM_D', 'HAM_D','HAM_I','HAM_N','MUCLEAF','FRALEAF','FRA','MUC','HAM']

df_retruct = df_init_sort[ df_init_sort[ "Arv_entity" ].isin( americas + germany ) ]






df_sort = df_retruct.sort_values(by=["Arv_entity", "Dpt_entity", "Dpt_day" ])

# GOTを一年分表示
#df_sort = df.sort_values(by=["Dpt_day", "Arv_entity","Dpt_entity", ])

#df_sort = df.sort_values(by=["Dpt_day", "Dpt_entity", "Arv_entity"])

#
# Dpt_day,lat_day,lon_day
#

#fig = px.scatter_geo(df,   

fig = px.scatter_geo(df_sort,   

lat = "lat_day",   lon = "lon_day",   color="Arv_entity",   hover_name="Arv_entity",   size="Arv_step",   animation_frame="Dpt_day",

#lat = "lat_day",   lon = "lon_day",   color="Arv_entity",   hover_name="capital_en",   size="Arv_step",   animation_frame="Dpt_day",

#lat = "lat_day",   lon = "lon_day",   color="Arv_entity",   hover_name="capital_jp_Arv",   size="Arv_step",   animation_frame="Dpt_day",

#lat = "lat_day",   lon = "lon_day",   color="name_ens_Arv",   hover_name="capital_jp_Arv",   size="Arv_step",   animation_frame="Dpt_day",



  projection="orthographic")

  #projection="equirectangular")
  #projection="natural earth")

# **********************************
#fig = px.scatter_geo(df, 
#
#  #locations="iso_alpha", 
#
#  lat = "lat_data",
#  lon = "lon_data",
#
#
#
#  color="name_ens",
#  #color="continent",
#
#  hover_name="capital_jp", 
#  #hover_name="country", 
#
#  size="Arv_step",
#  #size="pop",
#
#  animation_frame="Arv_week",
#  #animation_frame="year",
#
#  projection="orthographic")
#  #projection="equirectangular")
#  #projection="natural earth")
# **********************************


fig.show()

