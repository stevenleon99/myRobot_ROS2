```
build workspace:
colcon build
```

```
create package:
ament: code building envrionment, together with colcon
dependencies: python library
ros2 pkg create myRobot_Controller --build-type ament_python --dependencies rclpy
```

```
check pip installed so that python library can be retrieved
pip list
pip list | grep setuptools
may need to downgrade to 58.2.0 if encounter colcon error
setuptools                           59.6.0
```

```
run to see topic information graph:
rqt_graph

```

```
see the node info:
ros2 node info
see node list:
ros2 node list
see topic info:
ros2 topic info
see topic type detailed info:
ros2 interface show [type_name]

```

```
see the service list:
ros2 service list
see the service type:
ros2 service type
see detailed of the service type:
ros2 interface show [type_name_service]

```