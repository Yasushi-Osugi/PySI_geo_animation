#
#

import pyproj
grs80 = pyproj.Geod(ellps='GRS80')




## *********************
## Distance and Azimuth by 2 points (lat, lon)
## *********************
#
#ret = grs80.inv(lon0, lat0, lon1, lat1)
#print(f"進む方向：{ret[0]:.2f}度、進む距離：{ret[2]:.2f}m")
#
## [出力]
## 進む方向：45.00度、進む距離：18000.00m


# ******************************
# 2地点間の方位角と距離
# ******************************
def find_Distance_Azimuth_from_Dpt2Arv(latD,lonD,latA,lonA):

    result = grs80.inv(lonD, latD, lonA, latA)

#print(f"進む方向：{result[0]:.2f}度、進む距離：{result[2]:.2f}m")


    azimuth_Dpt2Arv = result[0]
    azimuth_Arv2Dpt = result[1]

    distance        = result[2]

    return azimuth_Dpt2Arv, azimuth_Arv2Dpt, distance


# ******************************
# ある1地点間からの距離と方位角
# ******************************
#

def find_Arv_by_Dpt_and_Distance_Azimuth(latD, lonD, azimuth_D2A, distance):

    lonA, latA, azimuth_A2D = grs80.fwd(lonD, latD, azimuth_D2A, distance)

    return latA, lonA, azimuth_A2D




# ******************************
# run 
# ******************************
#
#latD = 24.288472   # 南鳥島の緯度
#lonD = 153.9707894 # 南鳥島の経度
#latA = 24.4559224  # 与那国島の緯度
#lonA = 122.9187629 # 与那国島の経度
#
#print(latD,lonD,latA,lonA)
#
#
#azimuth_Dpt2Arv, azimuth_Arv2Dpt, distance = find_Distance_Azimuth_from_Dpt2Arv(latD,lonD,latA,lonA)
#
#print( azimuth_Dpt2Arv, azimuth_Arv2Dpt, distance )
#
#
#latA, lonA, azimuth_A2D = find_Arv_by_Dpt_and_Distance_Azimuth(latD, lonD, azimuth_Dpt2Arv, distance)
#
#print( latA, lonA, azimuth_A2D )

