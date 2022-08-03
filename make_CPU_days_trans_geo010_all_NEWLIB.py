
#
#
#

import pandas as pd

from lib4distance_azimuth_lat_lon import *



#filename = 'CPU_Arv_geo_df_test_YTO.csv'

filename = 'CPU_Arv_geo_df.csv'

#filename = 'CPU_geo_dummy.csv'


#0 seq_no,
#1 control_flag,
#2 priority_no,
#3 modal,
#4 LT,
#5 Dpt_entity,
#6 Dpt_week,
#7 Dpt_step,
#8 Arv_entity,
#9 Arv_week,
#10Arv_step,
#11node_name,
#12capital_en,
#13name_ens,
#14capital_jp,
#15iscapital,
#16lat,
#17lon,
#18node_name_Arv,
#19capital_en_Arv,
#20name_ens_Arv,
#21capital_jp_Arv,
#22iscapital_Arv,
#23lat_Arv,
#24lon_Arv


#YTOLEAF202301009,F,1202301009,B,2,YTO,-1,0,YTOLEAF,1,0,YTO,Toronto,Canada,トロント,0,43.6534399,-79.3840901,YTO,Toronto,Canada,トロント,0,43.65794658648729,-79.3840901


df = pd.read_csv(filename)
#print(df)


header_df = list(df.columns.values)
#print(header_df)

l_CPU = df.values.tolist() # 数万件になる
#print(l_node_city_name)




# ******************************
# main start
# ******************************

l_geo_check = []

l_CPU_geo = []

days_a_week = 5  # 一週間の実働日=5

Dpt_day = 0 # 出荷日を週の小数点で表す

lat_day = 0
lon_day = 0


for r in l_CPU:

    Dpt_week = r[6]
    Arv_week = r[9]

    lat_D = r[16]
    lon_D = r[17]

    lat_A = r[23]
    lon_A = r[24]

    # 距離と方位を求める
    azimuth_D2A, azimuth_A2D, distance_r = find_Distance_Azimuth_from_Dpt2Arv(lat_D,lon_D,lat_A,lon_A)


    print('Dpt_week Arv_week',Dpt_week,Arv_week,'lat_D lon_D',lat_D,lon_D,'lat_A lon_A',lat_A,lon_A)


    trans_days = ( Arv_week - Dpt_week ) * days_a_week  # 例 2週間x 5日/週=10日

    # インターバル期間は週内の刻み 0.2 = 1/5 
    interval_day = 1 / days_a_week

    # 一回のインターバルで進む距離
    interval_distance = distance_r / trans_days



# ***********************************************************


#    dev_lat = lat_A - lat_D
#    dev_lon = lon_A - lon_D
#
#    interval_dev_lat = dev_lat / days_a_week
#    interval_dev_lon = dev_lon / days_a_week
#
#    print('trans_days interval_day dev_lat dev_lon',trans_days,interval_day)
#    print('dev_lat dev_lon  interval_dev_lat interval_dev_lon ',dev_lat, dev_lon,interval_dev_lat,interval_dev_lon)


    Dpt_day = Dpt_week

    lat_day = lat_D
    lon_day = lon_D

    print('init lat_day lon_day',lat_day,lon_day)

    for d in range( trans_days + 1 ):  # 10日の場合 0-9で変化

        Dpt_day = Dpt_week + interval_day * d

        #Dpt_day += interval_day

        #
        # 例 Dpt_week=1 interval=1/5(=0.2) x 3日の場合、Dpt_day = 1.6

        #lat_day += interval_dev_lat
        #lon_day += interval_dev_lon

        # ******************************
        # 出荷地から着荷地まで、等間隔インターバルでジャンプする地点を求める
        # ******************************

        distance_day = interval_distance * d  #出荷地からの距離を等倍で伸ばす

        lat_day, lon_day, azimuth_A2D_day = find_Arv_by_Dpt_and_Distance_Azimuth(lat_D, lon_D, azimuth_D2A, distance_day )


        print('jumpping interval  lat_day lon_day',lat_day,lon_day)
        

        l_CPU_geo_row = []

        l_CPU_geo_row = r + [ Dpt_day, lat_day, lon_day ]

        l_CPU_geo.append(l_CPU_geo_row)



df_CPU_geo = pd.DataFrame(l_CPU_geo)

# ***********************
# 入力のCPUのheaderに"_Arv"をつけてheaderを作成
# ***********************

header_day_trans  = [ 'Dpt_day', 'lat_day', 'lon_day' ]

df_CPU_geo.columns = header_df + header_day_trans

# ***********************
#
#seq_no,control_flag,priority_no,modal,LT,Dpt_entity,Dpt_week,Dpt_step,Arv_entity,Arv_week,Arv_step,node_name,capital_en,name_ens,capital_jp,iscapital,lat,lon,node_name_Arv,capital_en_Arv,name_ens_Arv,capital_jp_Arv,iscapital_Arv,lat_Arv,lon_Arv,Dpt_day,lat_day,lon_day

#YTOLEAF202301009,F,1202301009,B,2,YTO,-1,0,YTOLEAF,1,0,YTO,Toronto,Canada,トロント,0,43.6534399,-79.3840901,YTO,Toronto,Canada,トロント,0,43.65794658648729,-79.3840901,-1.0,43.65434123729746,-79.3840901

#YTOLEAF202301009,F,1202301009,B,2,YTO,-1,0,YTOLEAF,1,0,YTO,Toronto,Canada,トロント,0,43.6534399,-79.3840901,YTO,Toronto,Canada,トロント,0,43.65794658648729,-79.3840901,-0.8,43.65434123729746,-79.3840901

#YTOLEAF202301009,F,1202301009,B,2,YTO,-1,0,YTOLEAF,1,0,YTO,Toronto,Canada,トロント,0,43.6534399,-79.3840901,YTO,Toronto,Canada,トロント,0,43.65794658648729,-79.3840901,-0.6,43.65434123729746,-79.3840901
#
# ***********************


filename = 'CPU_days_trans_geo.csv'

df_CPU_geo.to_csv( filename , encoding="utf8", mode='w', header=True, index=False)

print(" filename = 'CPU_days_trans_geo.csv' ")
print('end of process')

