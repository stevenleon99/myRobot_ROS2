from setuptools import find_packages, setup

package_name = 'myrobot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='steve',
    maintainer_email='1301637976@qq.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # creat executable can be handly run from commandline
            # [package_name.python_file_name.function_name]
            "test_node = myrobot_controller.first_node:main",
            "draw_circle = myrobot_controller.draw_circle:main",
            "get_pose = myrobot_controller.get_pose:main",
            "turtle_controller = myrobot_controller.turtle_controller:main",
            "set_pencolor = myrobot_controller.set_pencolor:main"
        ],
    },
)
