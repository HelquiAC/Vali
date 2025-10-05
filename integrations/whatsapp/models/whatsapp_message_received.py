from pydantic import BaseModel, Field
from typing import List


class WhatsappText(BaseModel):
    body: str

class WhatsappMessages(BaseModel):
    from_: str = Field(..., alias='from')
    id: str
    timestamp: str
    text: WhatsappText
    type: str

class WhatsappProfile(BaseModel):
    name: str

class WhatsappContacts(BaseModel):
    profile:WhatsappProfile
    wa_id: str    

class WhatsappMetaData(BaseModel):
    display_phone_number: str
    phone_number_id: str

class WhatsappValue(BaseModel):
    messaging_product: str
    metadata: WhatsappMetaData
    contacts: List[WhatsappContacts]
    messages: List[WhatsappMessages]

class WhatsappChanges(BaseModel):
    value: WhatsappValue
    field: str

class WhatsappEntry(BaseModel):
    id: str
    changes: List[WhatsappChanges]

class WhatsappPayload(BaseModel):
    object: str
    entry: List[WhatsappEntry]