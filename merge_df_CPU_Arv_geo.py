
#
#
#

import pandas as pd

import math


POLE_RADIUS = 6356752.314

lat_KM_degree = ( 360 * 1000 ) / ( 2 * math.pi * POLE_RADIUS )

print( lat_KM_degree )

# => 0.0090133729745762


#
# 緯度0-90を辞書のキーにして、1km移動分の経度を出す
#

# distance_KM_lat_lot_list

distance_KM_lat_lot_list = [[0, 111.19492664454764, 8.993216059188204e-06], [1, 111.1779906887568, 8.994586012977189e-06], [2, 111.12718798164178, 8.9986979618813e-06], [3, 111.04253400163961, 9.005558176340199e-06], [4, 110.92405454096395, 9.015177133023955e-06], [5, 110.77178569782954, 9.027569553928333e-06], [6, 110.58577386543698, 9.042754461499001e-06], [7, 110.36607571750545, 9.060755250187693e-06], [8, 110.11275819109838, 9.08159977488277e-06], [9, 109.8258984666609, 9.105320456846189e-06], [10, 109.50558394368862, 9.131954408044005e-06], [11, 109.15191221452018, 9.16154357456115e-06], [12, 108.76499103464425, 9.194134900277572e-06], [13, 108.34493828935294, 9.229780512028497e-06], [14, 107.89188195830181, 9.268537927501174e-06], [15, 107.40596007592136, 9.310470287618456e-06], [16, 106.88732068988205, 9.355646615012027e-06], [17, 106.33612181521883, 9.404142100816018e-06], [18, 105.75253138693961, 9.456038421823532e-06], [19, 105.13672720770504, 9.511424090883382e-06], [20, 104.48889689476374, 9.570394843072681e-06], [21, 103.80923782187855, 9.633054061295138e-06], [22, 103.09795705922977, 9.699513244724142e-06], [23, 102.35527131042102, 9.769892524315823e-06], [24, 101.58140684650502, 9.844321230075637e-06], [25, 100.77659943635368, 9.92293851541953e-06], [26, 99.9410942752631, 1.0005894044403262e-05], [27, 99.0751459100309, 1.0093348748717357e-05], [28, 98.17901816110276, 1.018547566201051e-05], [29, 97.25298404237755, 1.0282460840114219e-05], [30, 96.29732567757885, 1.0384504377080873e-05], [31, 95.3123342146178, 1.0491821528032964e-05], [32, 94.29830973634182, 1.0604643951689071e-05], [33, 93.25556116922093, 1.0723221086894825e-05], [34, 92.18440618927485, 1.084782167980537e-05], [35, 91.08517112503918, 1.097873548074283e-05], [36, 89.95819085771359, 1.1116275132541236e-05], [37, 88.80380871973053, 1.1260778275355875e-05], [38, 87.62237638948262, 1.1412609897213774e-05], [39, 86.4142537841585, 1.1572164963638446e-05], [40, 85.1798089503374, 1.1739871365325937e-05], [41, 83.91941795128646, 1.1916193229324826e-05], [42, 82.63346475280625, 1.210163464634393e-05], [43, 81.32234110591152, 1.2296743876293885e-05], [44, 79.98644642698677, 1.2502118104631889e-05], [45, 78.62618767680937, 1.271840883485882e-05], [46, 77.24197923616744, 1.2946328018634774e-05], [47, 75.8342427792642, 1.3186655043299725e-05], [48, 74.40340714535752, 1.3440244719524193e-05], [49, 72.94990820828464, 1.3708036439810542e-05], [50, 71.47418874346627, 1.399106471273399e-05], [51, 69.97669829294556, 1.4290471319662296e-05], [52, 68.45789302806378, 1.4607519392834042e-05], [53, 66.91823561099272, 1.4943609777956086e-05], [54, 65.35819505375842, 1.530030012575286e-05], [55, 63.7782465748373, 1.5679327258183582e-05], [56, 62.17887145423396, 1.608263348324098e-05], [57, 60.56055688801246, 1.6512397695569128e-05], [58, 58.92379583845149, 1.697107231078004e-05], [59, 57.26908688498719, 1.7461427349248434e-05], [60, 55.59693407117584, 1.79866033389501e-05], [61, 53.907846752227066, 1.855017516459582e-05], [62, 52.20233943946256, 1.9156229600776208e-05], [63, 50.48093164320263, 1.9809460076291046e-05], [64, 48.74414771513025, 2.0515283308350855e-05], [65, 46.99251668848935, 2.1279983930823316e-05], [66, 45.226572116132296, 2.211089528147769e-05], [67, 43.44685190930646, 2.301662735167693e-05], [68, 41.653898173245615, 2.4007356906689277e-05], [69, 39.84825704144153, 2.5095200499234297e-05], [70, 38.03047851044249, 2.6294699387635048e-05], [71, 36.20111627178323, 2.7623457588777304e-05], [72, 34.36072754315291, 2.9102992616908973e-05], [73, 32.50987289948909, 3.075988648407529e-05], [74, 30.649116101492798, 3.2627368328944863e-05], [75, 28.779023924817594, 3.4747530097351564e-05], [76, 26.900165986619683, 3.717449180415491e-05], [77, 25.013114572114585, 3.997902768633346e-05], [78, 23.118444461820445, 4.3255505432101024e-05], [79, 21.216732754746157, 4.713261045229979e-05], [80, 19.308558693554005, 5.1790504711977355e-05], [81, 17.39450348750281, 5.748942478975938e-05], [82, 15.475150137716824, 6.461972847441066e-05], [83, 13.551083257583796, 7.379483846358592e-05], [84, 11.622888893757757, 8.603712976530857e-05], [85, 9.691154350414262, 0.000103186881958727], [86, 7.756468011503157, 0.00012892465984736345], [87, 5.819419155179929, 0.00017183845558020838], [88, 3.8805977804072787, 0.00025769225686024267], [89, 1.9405944287743828, 0.0005153060243667545], [90, 0.0, 0.0005153060243667545]]

#
# dictionary define
#
distance_KM_lat_lot_dic = {}


for i, l_lat_lon in enumerate(distance_KM_lat_lot_list):

    distance_KM_lat_lot_dic[i] = l_lat_lon[2]

print(distance_KM_lat_lot_dic)


for i in range(91):

    print( distance_KM_lat_lot_dic[i] )


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

filename = 'CPU_geo_df.csv'
#filename = 'CPU_geo_dummy.csv'

df_CPU_geo = pd.read_csv(filename)
#print(df_CPU_geo)


header_CPU_geo = list(df_CPU_geo.columns.values)
#print(header_node_city_name)

l_CPU = df_CPU_geo.values.tolist()
#print(l_node_city_name)


#
#0 seq_no
#1 name_ens
#2 capital_jp
#3 capital_en
#4 iscapital
#5 Dpt_lat
#6 Dpt_lon

#seq_no   name_ens capital_jp       capital_en  iscapital        lat        lon
#0        Belgium      ブリュセル         Brussels          1  50.850300   4.351700
#1    Switzerland     チューリッヒ           Zurich          0  47.384200   8.531850
#2       Portugal       リスボン           Lisbon          1  38.722200  -9.139300
#3         Poland      ワルシャワ          Warsaw           1  52.229770  21.011780
#4    Netherlands    アムステルダム        Amsterdam          1  52.391500   4.903500


filename = 'node_city_geo.csv'

df_city_geo = pd.read_csv(filename)
print(df_city_geo)


header_city_geo = list(df_city_geo.columns.values)
#print(header_city_geo)

l_city_geo = df_city_geo.values.tolist()
print(l_city_geo)


# *******************************
# search node
# *******************************
def search_node_coord( l_city_geo, node_name ):

    for l_city in l_city_geo :

        print('l_city,city_name BF' , l_city , node_name)

        result_in = node_name in l_city 

        if result_in :

            print('l_city IN' , l_city)

            return l_city, l_city[5], l_city[6]

        else:

            pass

    print('error no city_name')



# *******************************
# leaf_nodeの販売チャネル分類から(仮に)東西南北を割り振り
# *******************************
#        direction = check_leaf_node(leaf_node_name) 

def check_direction_leaf_node( Arv_node_str ):

    leaf_node = []
    leaf_node = Arv_node_str[3:]

    if leaf_node == 'LEAF':

        direction = "N"

    elif  leaf_node == '_D': # Direct channel

        direction = "E"

    elif  leaf_node == '_I': # In direct channnel

        direction = "W"

    elif  leaf_node == '_N': # WEB channel

        direction = "S"

    else:

        print('leaf_node has NOT correct chennel option')


    return direction



# *******************************
# 出荷地の座標coordinatesに、方角(EWSN)と距離(500m)を与えて、着荷地の座標を算定
# *******************************
#        Arv_lat, Arv_lon = make_Arv(Dpt_lat, Dpt_lon, direction , distance)

def make_Arv_coordinates(Dpt_lat, Dpt_lon, direction , distance):

# direction="E","W","S","N"
# distance = 500 meter


    lat_dis = lat_KM_degree * distance / 1000

    lat_abs = abs( int(Dpt_lat) )

    lon_dis = distance_KM_lat_lot_dic[ lat_abs ] * distance / 1000

    #lon_dis = calc_lon_meter2degree(Dpt_lat, distance) # 緯度で変化する

    if direction == "E":

        Arv_lat = Dpt_lat
        Arv_lon = Dpt_lon + lon_dis

    elif direction == "W": 

        Arv_lat = Dpt_lat
        Arv_lon = Dpt_lon - lon_dis # WEST is MINUS to EAST

    elif direction == "S":

        Arv_lat = Dpt_lat - lat_dis
        Arv_lon = Dpt_lon

    elif direction == "N":

        Arv_lat = Dpt_lat + lat_dis
        Arv_lon = Dpt_lon

    else:

        print('direction must be E/W/S/N in this version')

    return Arv_lat, Arv_lon






l_geo_check = []

l_CPU_geo = []

for r in l_CPU:

    Arv_node_name = r[8]  #### Arv_entity = Arv_node_name
    #node_name = r[5] 

#0 df_seq_no

#1 seq_no
#2 control_flag
#3 priority_no
#4 modal
#5 LT
#6 Dpt_entity #### node_name
#7 Dpt_week
#8 Dpt_step
#9 Arv_entity
#10 Arv_week   #### Arv_node_name
#11 Arv_step

    print('Arv_node_name',Arv_node_name)

    print('type(Arv_node_name)',type(Arv_node_name))

    if len( str(Arv_node_name) ) == 3 : # is NOT leaf_node

        l_geo, Dpt_lat, Dpt_lon = search_node_coord(l_city_geo,Arv_node_name)

    else: #### if Arv_node_name is LEAF_node / Direct / InDirect / WEB

        # ******************
        # leafの時は、3桁でArv_nodeを検索してから、着荷地の緯度経度をつくる
        # ******************

        Arv_node_str = str(Arv_node_name)

        leaf_node_name = Arv_node_str[:3]

        print('leaf_node_name',leaf_node_name)

        l_geo, Dpt_lat, Dpt_lon = search_node_coord(l_city_geo, leaf_node_name)

        # ******************
        # each channels be located in E/W/S/N with Deirect/In_Direct/WEB/LEAF
        # ******************
        direction = "X"  # direction="E","W","S","N"

        direction = check_direction_leaf_node(Arv_node_str) 
        #direction = check_direction_leaf_node(leaf_node_name) 

        distance = 500   # meter

        Dpt_lat_F = float(Dpt_lat)
        Dpt_lon_F = float(Dpt_lon)

        print('Dpt_lat Dpt_lon',Dpt_lat,Dpt_lon)
        print('Dpt_lat_F Dpt_lon_F',Dpt_lat_F,Dpt_lon_F)

        print('direction distance',direction,distance)


        Arv_lat, Arv_lon = make_Arv_coordinates(Dpt_lat_F, Dpt_lon_F, direction , distance)

        #l_geo = update_Arv_location(l_geo, Arv_lat, Arv_lon )

        print('Arv_lat Arv_lon',Arv_lat,Arv_lon)

        l_geo[5] = Arv_lat
        l_geo[6] = Arv_lon


#0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27

#0,0,YTOLEAF202301009,F,1202301009,B,2,YTO,-1,0,YTOLEAF,1,0,
#2,YTO,Canada,トロント,Toronto,0,43.6534399,-79.3840901,
#2,YTO,Canada,トロント,Toronto,0,43.6534399,-79.3840901

#1,1,YTOLEAF202301014,F,1202301014,B,2,YTO,-1,1,YTOLEAF,1,1,2,YTO,Canada,トロント,Toronto,0,43.6534399,-79.3840901,2,YTO,Canada,トロント,Toronto,0,43.6534399,-79.3840901

#2,2,YTOLEAF202301016,F,1202301016,B,2,YTO,-1,2,YTOLEAF,1,2,2,YTO,Canada,トロント,Toronto,0,43.6534399,-79.3840901,2,YTO,Canada,トロント,Toronto,0,43.6534399,-79.3840901













        #l_geo_check.append(l_geo)



    l_CPU_geo_row = []

    l_CPU_geo_row = r + l_geo


#    #l_node_geo_row.append( r[0] )
#    #l_node_geo_row.append( l_geo )
#
#    l_node_geo_row.insert(0,r[0])


    l_CPU_geo.append(l_CPU_geo_row)


df_CPU_geogeo = pd.DataFrame(l_CPU_geo)

# ***********************
# 入力のCPUのheaderに"_Arv"をつけてheaderを作成
# ***********************
header_city_geo_Arv  = []

for col in header_city_geo:

    header_city_geo_Arv.append( col + "_Arv")

print('header_city_geo_Arv',header_city_geo_Arv)

df_CPU_geogeo.columns = header_CPU_geo + header_city_geo_Arv

# ***********************
#
#seq_no,control_flag,priority_no,modal,LT,Dpt_entity,Dpt_week,Dpt_step,Arv_entity,Arv_week,Arv_step,node_name,capital_en,name_ens,capital_jp,iscapital,lat,lon,node_name_Arv,capital_en_Arv,name_ens_Arv,capital_jp_Arv,iscapital_Arv,lat_Arv,lon_Arv
#YTOLEAF202301009,F,1202301009,B,2,YTO,-1,0,YTOLEAF,1,0,YTO,Toronto,Canada,トロント,0,43.6534399,-79.3840901,YTO,Toronto,Canada,トロント,0,43.65794658648729,-79.3840901
#YTOLEAF202301014,F,1202301014,B,2,YTO,-1,1,YTOLEAF,1,1,YTO,Toronto,Canada,トロント,0,43.6534399,-79.3840901,YTO,Toronto,Canada,トロント,0,43.66245327297458,-79.3840901
#YTOLEAF202301016,F,1202301016,B,2,YTO,-1,2,YTOLEAF,1,2,YTO,Toronto,Canada,トロント,0,43.6534399,-79.3840901,YTO,Toronto,Canada,トロント,0,43.66695995946187,-79.3840901
#
# ***********************


filename = 'CPU_Arv_geo_df.csv'
#filename = 'CPU_geo_geoArv.csv'


#df_header = pd.DataFrame(header_CPU_geo)
#
#df_header.to_csv( filename , encoding="utf8", mode='w', header=False, index=False)


df_CPU_geogeo.to_csv( filename , encoding="utf8", mode='a', header=True, index=False)


#df_CPU_geo.to_csv( filename , encoding="shift_jis")


#print('l_geo_check',l_geo_check)


print('end of process')

