# PySI_geo_animation
Python plotly demo that is visualization for Global Supply Chain. global PSI. showing demand and supply activities for one year, week by week. 

ここでご紹介するサプライチェーン可視化のデモは、Pythonのplotlyライブラリを使用しています。
使用している可視化の元データは、グローバルWeekly PSI連携処理によって、世界各国の最終需要情報をもとに生成された約20万件の購入オーダー(PO: Purchase Order)を使用しています。
世界地図の上にあるグローバル供給拠点・マザープラント(JPN)から需要地(欧州、米州など)に向かって購入オーダーPOが移動する様子をアニメーションで表示します。
アニメーションのtime stepはWeeklyの中を実働5日とみなして、1/5 = 0.2 week間隔としています。 

可視化のための入力データ生成方法については、下記のpdfファイル「可視化データ生成手順」を参照ください。
本内容に関連する情報は、下記のnoteのURL記事および関連する過去記事を参照ください。
https://note.com/osuosu1123/n/ndaacd017d283

[animation_data_generation_GUIDE.pdf](https://github.com/Yasushi-Osugi/PySI_geo_animation/files/9248100/animation_data_generation_GUIDE.pdf)
