import datetime


class cryOSTempSensor(object):
    def __init__(self, description, input_file, test_mode=False):
        self.temp = 0
        self.description = description

    def update_sensor(self):
        # TODO: connect to sensor code
        self.temp = 0


class cryOSHardware(object):
    def __init__(self):
        self.temp_sensors = list()
        self.last_refresh = None

    def add_temp_sensor(self, description, test_mode=False):
        self.temp_sensors.append(cryOSTempSensor(description=description, input_file=None, test_mode=test_mode))

    def update_temp_sensors(self):
        for sensor in self.temp_sensors:
            sensor.update_sensor()
        self.last_refresh = datetime.datetime.now()

    def get_temp_sensors_as_dict(self):
        """

        :return: reads of each sensor by description
        """
        sensor_reads = dict()
        for sensor in self.temp_sensors:
            sensor_reads[sensor.description] = sensor.temp
        return sensor_reads


if __name__ == '__main__':
    test_cryOS_rig = cryOSHardware()
    test_cryOS_rig.add_temp_sensor('hotside', test_mode=True)
    test_cryOS_rig.add_temp_sensor('coldside', test_mode=True)

    test_cryOS_rig.update_temp_sensors()

    test_sensor_results = test_cryOS_rig.get_temp_sensors_as_dict()

    print(test_sensor_results)
