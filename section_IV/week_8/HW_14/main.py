
from device_model import DeviceModel

if __name__ == "__main__":

    # Getting all the devices from the database.
    devices = DeviceModel.get_device_model_from_db()
    for device in devices:
        print(device)

    # Getting the device model with id 7 from the database.
    device_model_1 = DeviceModel.find_device_model_by_id(7)
    print(device_model_1)

    # Creating a new device.
    try:
        new_device = DeviceModel.create_device_model(
            "Rohnson", "099", 4, 32, 6, 8, 9, 500)
        print(new_device)
    except Exception as e:
        print(e)

    # Deleting all devices with the given name from the database.
    try:
        machine_models = DeviceModel.find_device_model_by_name("Rohnson")
        print(machine_models)
        device_model_ids = [
            machine_model.device_model_id for machine_model in machine_models]
        print(device_model_ids)
        if DeviceModel.delete_device_model(device_model_ids):
            print("All machines deleted")
        else:
            print("Nothing has been deleted")
    except Exception as e:
        print(e)

    # Updating chosen paramtres with the desired values for a chosen device.
    device_model_1 = DeviceModel.find_device_model_by_id(5)
    device_model_1.milk_capacity_kgs = 6
    device_model_1.coffee_capacity_kgs = 13
    device_model_1.cups_capacity_count = 700
    device_model_1.update_device_model()
