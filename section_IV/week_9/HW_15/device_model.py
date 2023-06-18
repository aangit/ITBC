from database_connector import mycursor


class DeviceModel:
    def __init__(self, device_model_id: int, model_name: str, model_number: str, water_capacity_liters: float, coffee_capacity_kgs: float,
                 milk_capacity_kgs: float, sugar_capacity_kgs: float, sweetener_capacity_count: int, cups_capacity_count: int):
        self.device_model_id = device_model_id
        self.model_name = model_name
        self.model_number = model_number
        self.water_capacity_liters = water_capacity_liters
        self.coffee_capacity_kgs = coffee_capacity_kgs
        self.milk_capacity_kgs = milk_capacity_kgs
        self.sugar_capacity_kgs = sugar_capacity_kgs
        self.sweetener_capacity_count = sweetener_capacity_count
        self.cups_capacity_count = cups_capacity_count

    def __repr__(self) -> str:
        return f"""Device model id: {self.device_model_id}\nDevice model name: {self.model_name}\nDevice model number: {self.model_number}\nDevice water capacity (l): {self.water_capacity_liters}\nDevice coffee capacity (kg): {self.coffee_capacity_kgs}\nDevice milk capacity (kg): {self.milk_capacity_kgs}\nDevice sugar capacity (kg): {self.sugar_capacity_kgs}\nDevice sweetener capacity: {self.sweetener_capacity_count}\nDevice total cups: {self.cups_capacity_count}\n """

    @staticmethod
    def get_device_model_from_db():
        sql = " select device_model_id, model_name, model_number, water_capacity_liters , coffee_capacity_kgs, milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count from device_model  "
        mycursor.execute(sql)
        results = mycursor.fetchall()
        return [DeviceModel.create_from_row(row) for row in results]

    @staticmethod
    def find_device_model_by_id(id: int):
        sql = " select device_model_id, model_name, model_number, water_capacity_liters , coffee_capacity_kgs, milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count from device_model where device_model_id = (%s)  "
        val = (id,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        if result:
            return DeviceModel.create_from_row(result)
        else:
            raise Exception(
                f"There is no device with id {id}. Please try again. ")

    @staticmethod
    def create_device_model(model_name, model_number, water_capacity_liters, coffee_capacity_kgs, milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count):
        sql = """insert into device_model (model_name, model_number, water_capacity_liters , coffee_capacity_kgs, milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count)
                    values (%s, %s, %s, %s, %s, %s, %s, %s) """
        val = (model_name, model_number, water_capacity_liters, coffee_capacity_kgs,
               milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count)
        mycursor.execute(sql, val)
        device_model_id = mycursor.lastrowid
        return DeviceModel(device_model_id=device_model_id, model_name=model_name, model_number=model_number, water_capacity_liters=water_capacity_liters,
                           coffee_capacity_kgs=coffee_capacity_kgs, milk_capacity_kgs=milk_capacity_kgs, sugar_capacity_kgs=sugar_capacity_kgs,
                           sweetener_capacity_count=sweetener_capacity_count, cups_capacity_count=cups_capacity_count)

    @staticmethod
    def find_device_model_by_name(model_name: str):
        sql = """ select device_model_id, model_name, model_number, water_capacity_liters , coffee_capacity_kgs, milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count 
                from device_model where lower(trim(model_name)) = %s """
        val = (model_name.lower(),)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        devices = [DeviceModel.create_from_row(row) for row in result]
        return devices

    @staticmethod
    def delete_device_model(device_model_ids: list):
        delete_strings = ','.join(['%s'] * len(device_model_ids))
        try:
            sql = f" DELETE FROM device_model WHERE device_model_id IN ({delete_strings}) "
            val = tuple(device_model_ids)
            mycursor.execute(sql, val)
            if len(device_model_ids) == mycursor.rowcount:
                return True
            if mycursor.rowcount > 0:
                raise Exception(f"Havent deleted all devices")
            else:
                return False
        except:
            raise Exception("Deletion failed")

    @staticmethod
    def create_from_row(row):
        return DeviceModel(device_model_id=row[0], model_name=row[1], model_number=row[2], water_capacity_liters=row[3],
                           coffee_capacity_kgs=row[4], milk_capacity_kgs=row[
            5], sugar_capacity_kgs=row[6], sweetener_capacity_count=row[7],
            cups_capacity_count=row[8])

    @staticmethod
    def update_device_model(device_model_id: int, **kwargs):
        updates = {}
        for key, value in kwargs.items():
            if value is not None:
                updates[key] = value
        if not updates:
            raise Exception("No updates provided")
        updates_string = ', '.join([f'{key} = %s' for key in updates.keys()])
        sql = f"UPDATE device_model SET {updates_string} WHERE device_model_id = %s"
        mycursor.execute(sql, tuple(updates.values())+(device_model_id,))