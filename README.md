# LineTrace_Bacon
知能ロボコン ベーコン班のプログラム

## 構成
main.py => これで完成
linetrace.py => 松本担当。走行関係。

capture.py => 須田担当。ボール関係。角度指定以外完成

objects.py => 須田担当？(竜征含む)。arduinoとの通信を隠蔽した物理層。


モータ制御は「objects.mc = objects.motor_control(mL, mR)」

ボールのゲート制御は「objects.gate_control(clr)」

色のインデックスはb=0, y=1, r=2

他センサー系は必要そうなのは書いてますので適当に推測して取得してください。

必要に応じて追加してください
```
#マイコンのsetup
sudo modprobe ftdi-sio
sudo chmod 777 /sys/bus/usb-serial/drivers/ftdi_sio/new_id
sudo echo "165c 0009" > /sys/bus/usb-serial/drivers/ftdi_sio/new_id
sudo chmod a+wrx /dev/ttyUSB0
```

```
def func1():
	# 初期化部分をここに書く
	yield None
	
	while True:
		if reigai:
			yield func2 # 関数オブジェクトを渡す。()はなし
		# ループ部分をここに書く
		yield None	# ←ステップごとに進んだ距離を関数内で使用する場合は 「dx = yield None」
```
cuiからwifi設定する
```
#例
sudo nmcli connection mod "profilename" \
 ipv4.addresses "192.168.4.111/24" \
 ipv4.gateway "192.168.4.1" \
 ipv4.dns "192.168.0.1,8.8.8.8" \
 ipv4.method "manual"
```
