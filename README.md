mkdir -p ~/servis_odev
cat << 'EOF' > ~/servis_odev/README.md
# RectangleArea Servisi (alan_interfaces & alan_py)

## Paketler
- alan_interfaces: RectangleArea.srv servis arayuzu (width, height -> area, success).
- alan_py: area_server (sunucu dugumu) ve area_client (istemci dugumu).

## Derleme ve Calistirma Komutlari
1. Workspace'e git ve derle:
   cd ~/ros2_ws
   colcon build --packages-select alan_interfaces alan_py
   source install/setup.bash

2. Sunucuyu baslat:
   ros2 run alan_py area_server

3. Istemci ile test et:
   ros2 run alan_py area_client 5.0 4.0
   ros2 run alan_py area_client 8.0 -3.0

4. ros2 service call ile dogrula:
   ros2 service call /calculate_rectangle_area alan_interfaces/srv/RectangleArea "{width: 6.5, height: 2.0}"

## Test Çıktıları

### Pozitif değerlerle çalıştırma
İstemci:
ros2 run alan_py area_client 5.0 4.0
Dikdörtgen Alanı (5.0 x 4.0): 20.0

Sunucu:
[INFO] [1795519383.946238511] [rectangle_area_server]: width=5.0, height=4.0 -> area=20.0

### Negatif değerle çalıştırma / Bonus
İstemci:
ros2 run alan_py area_client 8.0 -3.0
İşlem başarısız! Negatif veya sıfır değer girildi (8.0, -3.0).

Sunucu:
[WARN] [1795519824.972817677] [rectangle_area_server]: Geçersiz boyut reddedildi: width=8.0, height=-3.0

### `ros2 service call` ile doğrulama
İstemci:
ros2 service call /calculate_rectangle_area alan_interfaces/srv/RectangleArea "{width: 6.5, height: 2.0}"
requester: making request: alan_interfaces.srv.RectangleArea_Request(width=6.5, height=2.0)

response:
alan_interfaces.srv.RectangleArea_Response(area=13.0, success=True)

Sunucu:
[INFO] [1795519470.827413639] [rectangle_area_server]: width=6.5, height=2.0 -> area=13.0
EOF
