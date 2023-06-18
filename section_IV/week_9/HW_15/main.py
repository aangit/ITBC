from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from device_model import DeviceModel
from typing import Optional

app = FastAPI()

class DeviceSchema(BaseModel):
    device_model_id: int
    model_name: str
    model_number: str
    water_capacity_liters: float
    coffee_capacity_kgs: float
    milk_capacity_kgs: float
    sugar_capacity_kgs: float
    sweetener_capacity_count: int
    cups_capacity_count: int

    class Config:
        orm_mode = True

class DeviceSchemaIn(BaseModel):
    model_name: str
    model_number: str
    water_capacity_liters: float 
    coffee_capacity_kgs: float
    milk_capacity_kgs: float 
    sugar_capacity_kgs: float
    sweetener_capacity_count: int
    cups_capacity_count: int

    class Config:
        orm_mode = True

class DeviceSchemaUpdate(BaseModel):
    model_name: Optional[str]
    model_number: Optional[str] 
    water_capacity_liters: Optional[float] 
    coffee_capacity_kgs: Optional[float] 
    milk_capacity_kgs: Optional[float] 
    sugar_capacity_kgs: Optional[float] 
    sweetener_capacity_count: Optional[int]
    cups_capacity_count: Optional[int]

    class Config:
        orm_mode = True


#get all devices 
@app.get("/api/devices", response_model= list[DeviceSchema])
def get_all_devices():
    all_devices = DeviceModel.get_device_model_from_db()
    return all_devices

#find device by id
@app.get("/api/devices/{device_model_id}", response_model= DeviceSchema)
def get_device_model_by_id(device_id: int):
    try:
        return DeviceModel.find_device_model_by_id(device_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail= "There is no device with such id in the database.")

#create
@app.post("/api/devices", response_model= DeviceSchema)
def create_device(device: DeviceSchemaIn):
    return DeviceModel.create_device_model(model_name= device.model_name, model_number= device.model_number, water_capacity_liters= device.water_capacity_liters, coffee_capacity_kgs=device.coffee_capacity_kgs, milk_capacity_kgs= device.milk_capacity_kgs, sugar_capacity_kgs= device.sugar_capacity_kgs, sweetener_capacity_count= device.sweetener_capacity_count, cups_capacity_count= device.cups_capacity_count)

#update
@app.put("/api/devices/{device_model_id}")
def update_device(device_model_id: int, to_update: DeviceSchemaUpdate):
    try:
        DeviceModel.update_device_model(device_model_id=device_model_id, **to_update.dict(exclude_unset=True))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.delete("/api/devices/{device_model_id}")
def delete_device(device_model_id: int):
    try:
        flag = DeviceModel.delete_device_model([device_model_id])
        if flag:
            return {f"Device deleted"}
        else:
            raise HTTPException(status_code=404, detail="Device not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=e.__str__)