from pydantic import BaseModel


class DeliveryTaskChangeStatusDTO(BaseModel):
    delivery_task_id: int
    new_status_id: int
