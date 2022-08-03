#@220731 修正メモ　
# header_city_geoの各要素にArv_をつけて、ヘッダー名をユニークにする
# CPUのheaderとmergeして、出力ヘッダーに使う

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

filename = 'node_city_name.csv'

df_node_city_name = pd.read_csv(filename)
print(df_node_city_name)


#header_node_city_name = list(df_node_city_name.columns.values)
#print(header_node_city_name)


#l_node_city_name = df_node_city_name.values.tolist()
#print(l_node_city_name)


#
#        name_ens capital_jp       capital_en  iscapital        lat        lon
#0        Belgium      ブリュセル         Brussels          1  50.850300   4.351700
#1    Switzerland     チューリッヒ           Zurich          0  47.384200   8.531850
#2       Portugal       リスボン           Lisbon          1  38.722200  -9.139300
#3         Poland      ワルシャワ          Warsaw           1  52.229770  21.011780
#4    Netherlands    アムステルダム        Amsterdam          1  52.391500   4.903500


filename = 'city_geo_data.csv'

df_city_geo = pd.read_csv(filename)
print(df_city_geo)


header_city_geo = list(df_city_geo.columns.values)
#print(header_city_geo)


df_node_geo = pd.merge(df_node_city_name, df_city_geo, on='capital_en') 



#l_city_geo = df_city_geo.values.tolist()
#
##print('l_city_geo',l_city_geo)
#
#
#
#def search_city( l_city_geo, city_name ):
#
#    for l_city in l_city_geo :
#
#        print('l_city,city_name BF' , l_city , str(city_name))
#
#        result_in = str(city_name) in l_city 
#
#        if result_in :
#
#        #if str(l_city[2]) == str(city_name) :
#
#            print('l_city[2],city_name IN' , l_city[2] , city_name)
#
#            print('l_city' , l_city)
#
#            return l_city
#
#        else:
#
#            pass
#
#    print('error no city_name')





#l_node_geo = []
#
#for r in l_node_city_name:
#
#    city_name = r[1]
#
#    l_geo = search_city( l_city_geo , city_name )
#
#    l_node_geo_row = []
#    l_node_geo_row = l_geo
#
#    #l_node_geo_row.append( r[0] )
#    #l_node_geo_row.append( l_geo )
#
#    l_node_geo_row.insert(0,r[0])
#
#    l_node_geo.append(l_node_geo_row)
#
#
#df_node_geo = pd.DataFrame(l_node_geo)
#
#
#
#header_node_city_geo = header_city_geo.insert(0,header_node_city_name[0])
#print(header_node_city_geo)



filename = 'node_city_geo.csv'

df_node_geo.to_csv( filename , encoding="utf8", header=True , index=False)
#df_node_geo.to_csv( filename , encoding="shift_jis")

print('end of process')


#40,NOR,Norway,オスロ,Oslo,1,59.9138,10.7522,
#41,DEN,Denmark,コペンハーゲン,Kopenhagen,1,55.676,12.5683,
#42,HEL,Finland,ヘルシンキ,Helsinki,1,60.1698,24.9383,
#43,JNB,JNB,South Africa,ヨハネスブルグ,Johannesburg,0.0,-26.2044,28.0416

