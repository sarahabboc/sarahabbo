#airtable.py
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import requests
import json

# Airtable API details
URL = "https://api.airtable.com/v0/appsBBnPozbpqblxu/Table%201"
HEADERS = {"Authorization": "Bearer pat8KQI9h9IBd86cG.f88c25b0cd3cd4e9bc7ce0a3b14b1a3fecc8d9824202c3aa6d4ce41e9b3fc347"}

class AirTableController(Node):
    def __init__(self):
        super().__init__('airtable_controller')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(2.0, self.fetch_and_publish)  # Runs every 2 seconds

    def fetch_and_publish(self):
        r = requests.get(url=URL, headers=HEADERS, params={})
        if r.status_code == 200:
            data = r.json()
            print(data)  # Debugging: See what's being received

            if "records" in data and len(data["records"]) > 0:
                fields = data["records"][0]["fields"]
                

                cmd_type = fields.get("Command", "").lower()
                twist_msg = Twist()

                if cmd_type == "linear":
                    twist_msg.linear.x = float(fields.get("X", 0))
                    twist_msg.linear.y = float(fields.get("Y", 0))
                    twist_msg.linear.z = float(fields.get("Z", 0))
                elif cmd_type == "angular":
                    twist_msg.angular.x = float(fields.get("X", 0))
                    twist_msg.angular.y = float(fields.get("Y", 0))
                    twist_msg.angular.z = float(fields.get("Z", 0))
                else:
                    self.get_logger().warn("Unknown Command Type")

                #second record
                fields = data["records"][1]["fields"]
                cmd_type = fields.get("Command", "").lower()

                if cmd_type == "linear":
                    twist_msg.linear.x = float(fields.get("X", 0))
                    twist_msg.linear.y = float(fields.get("Y", 0))
                    twist_msg.linear.z = float(fields.get("Z", 0))
                elif cmd_type == "angular":
                    twist_msg.angular.x = float(fields.get("X", 0))
                    twist_msg.angular.y = float(fields.get("Y", 0))
                    twist_msg.angular.z = float(fields.get("Z", 0))
                else:
                    self.get_logger().warn("Unknown Command Type")

                #send message
                self.publisher.publish(twist_msg)
                self.get_logger().info(f"Published: {twist_msg}")

def main(args=None):
    rclpy.init(args=args)
    node = AirTableController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
