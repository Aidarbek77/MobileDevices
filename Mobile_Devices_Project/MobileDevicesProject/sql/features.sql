SELECT feature_id FROM devices_device_features
WHERE device_id = (SELECT id FROM devices_device WHERE name = 'iPhone 14');
