SELECT * FROM devices_device
WHERE category_id = (SELECT id FROM devices_category WHERE name = 'Смартфоны');
