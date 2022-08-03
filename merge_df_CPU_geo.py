
# read_test
# city_geo_data.csv 
#

# l_2d = [[0, 1, 2], [3, 4, 5]]
#
#df = pd.DataFrame(l_2d)
#print(df)
##    0  1  2
## 0  0  1  2
## 1  3  4  5

#l_2d = df.values.tolist()
#print(l_2d)
## [[0, 1, 2], [3, 4, 5]]

import pandas as pd

#
#   node_name          city_name
#0       root              Tokyo
#1        JPN              Tokyo
#2        YTO            Toronto
#3        NYC      New York City
#4        LAX        Los Angeles
#5        MEX        Mexico City
#6        SAO          Sao Paulo
#7        BUE       Buenos Aires
#8        KUL       Kuala Lumpur
#9        BKK            Bangkok
#10       SIN          Singapore
#11       SGN   Ho Chi Minh City
#

filename = 'common_plan_unit@220726.csv'

df_CPU = pd.read_csv(filename)

#print(df_CPU)

#l_CPU = df_CPU.values.tolist()
#
##print(l_node_city_name)


#
#        name_ens capital_jp       capital_en  iscapital        lat        lon
#0        Belgium      ブリュセル         Brussels          1  50.850300   4.351700
#1    Switzerland     チューリッヒ           Zurich          0  47.384200   8.531850
#2       Portugal       リスボン           Lisbon          1  38.722200  -9.139300
#3         Poland      ワルシャワ          Warsaw           1  52.229770  21.011780
#4    Netherlands    アムステルダム        Amsterdam          1  52.391500   4.903500


filename = 'node_city_geo.csv'

df_city_geo = pd.read_csv(filename)

#print(df_city_geo)
#
#l_city_geo = df_city_geo.values.tolist()
#
#print(l_city_geo)



#def search_node( l_city_geo, node_name ):
#
#    for l_city in l_city_geo :
#
#        print('l_city,city_name BF' , l_city , node_name)
#
#        result_in = node_name in l_city 
#
#        if result_in :
#
#            print('l_city IN' , l_city)
#
#            return l_city
#
#        else:
#
#            pass
#
#    print('error no city_name')
#
#
#
#
#
#l_CPU_geo = []
#
#for r in l_CPU:
#
#    node_name = r[5] 
#
##0 seq_no
##1 control_flag
##2 priority_no
##3 modal
##4 LT
##5 Dpt_entity #### node_name
##6 Dpt_week
##7 Dpt_step
##8 Arv_entity
##9 Arv_week
##10 Arv_step
#
#
#    l_geo = search_node(l_city_geo,node_name)
#
#    l_CPU_geo_row = []
#
#    l_CPU_geo_row = r + l_geo
#
#
#    #l_node_geo_row.append( r[0] )
#    #l_node_geo_row.append( l_geo )
#
#    l_node_geo_row.insert(0,r[0])
#
#
#    l_CPU_geo.append(l_CPU_geo_row)



df_CPU_geo = pd.merge(df_CPU, df_city_geo, left_on='Dpt_entity', right_on='node_name' ) 

#df_CPU_geo = pd.DataFrame(l_CPU_geo)



filename = 'CPU_geo_df.csv'

df_CPU_geo.to_csv( filename , encoding="utf8", header=True , index=False)
#df_CPU_geo.to_csv( filename , encoding="shift_jis")

print('end of process')

