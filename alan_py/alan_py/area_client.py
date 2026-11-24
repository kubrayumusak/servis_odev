import sys
import rclpy
from rclpy.node import Node
from alan_interfaces.srv import RectangleArea


class RectangleAreaClient(Node):
    def __init__(self):
        super().__init__('rectangle_area_client')
        self.client = self.create_client(RectangleArea, 'calculate_rectangle_area')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Servis bekleniyor...')

    def send_request(self, width: float, height: float):
        req = RectangleArea.Request()
        req.width = width
        req.height = height
        future = self.client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()


def main(args=None):
    rclpy.init(args=args)

    if len(sys.argv) != 3:
        print('Kullanım: ros2 run alan_py area_client <width> <height>')
        rclpy.shutdown()
        return

    try:
        width = float(sys.argv[1])
        height = float(sys.argv[2])
    except ValueError:
        print('Hata: width ve height sayısal değer olmalıdır.')
        rclpy.shutdown()
        return

    node = RectangleAreaClient()
    result = node.send_request(width, height)

    if result is not None:
        if result.success:
            print(f'Dikdörtgen Alanı ({width} x {height}): {result.area}')
        else:
            print(f'İşlem başarısız! Negatif veya sıfır değer girildi ({width}, {height}).')
    else:
        print('Servis çağrısı başarısız oldu.')

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
