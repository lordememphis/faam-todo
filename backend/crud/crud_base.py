from typing import TypeVar, Generic, List, Any

from bson import ObjectId
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from pymongo import ReturnDocument

from backend.db.database import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, collection: str):
        self.collection = collection

    async def create(self, request: Request, obj: CreateSchemaType) -> ModelType:
        data = jsonable_encoder(obj)
        db_obj = await request.app.db_database[self.collection].insert_one(data)
        return await self.get_by_id(request, db_obj.inserted_id)

    async def get_by_id(self, request: Request, obj_id: str) -> ModelType | None:
        if not ObjectId.is_valid(obj_id):
            return None
        return await request.app.db_database[self.collection].find_one({'_id': ObjectId(obj_id)})

    def get_multi(self, request: Request, skip: int = 0, length: int = 10) -> List[ModelType]:
        return request.app.db_database[self.collection].find().skip(skip).to_list(length)

    def get_all(self, request: Request) -> List[ModelType]:
        return request.app.db_database[self.collection].find().to_list(None)

    async def update(self, request: Request, obj_id: str, obj_in: Any) -> ModelType | None:
        if not ObjectId(obj_id):
            return None
        data = jsonable_encoder(obj_in)
        return await request.app.db_database[self.collection] \
            .find_one_and_update({'_id': ObjectId(obj_id)},
                                 {'$set': {k: v for k, v in data.items() if v is not None}},
                                 return_document=ReturnDocument.AFTER)

    async def delete(self, request: Request, obj_id: str) -> ModelType | None:
        if not ObjectId.is_valid(obj_id):
            return None
        return await request.app.db_database[self.collection].find_one_and_delete({'_id': ObjectId(obj_id)})
