import datetime

import bcrypt
from fastapi import HTTPException
from fastapi.openapi.models import Response
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from data.databaseservice import DatabaseService
from data.model.user import User
from services.delivery_task_service import DeliveryTaskService
from services.price_service import PriceService


class UserService:
    def __init__(self, database_service: DatabaseService):
        self.database_service = database_service

    async def create_user(self, login: str, name: str, surname: str, plain_password: str):
        hashed_password = bcrypt.hashpw(str.encode(plain_password), bcrypt.gensalt())
        created_user = User(login=login, password=hashed_password, name=name, surname=surname)

        return await self.database_service.save(created_user)

    async def get_user_by_login(self, login: str):
        async with AsyncSession(self.database_service.engine) as session:
            st = select(User) \
                .where(User.login == login) \
                .limit(1)
            result = (await session.execute(st)).first()

            if result:
                return result[0]

    async def get_user_by_id(self, user_id: int):
        async with AsyncSession(self.database_service.engine) as session:
            st = select(User) \
                .where(User.id == user_id) \
                .limit(1)
            result = (await session.execute(st)).first()

            if result:
                return result[0]

    async def check_user_password(self, login: str, plain_password: str):
        user = await self.get_user_by_login(login)
        if not user:
            raise HTTPException(401, "Неверный логин или пароль")

        return bcrypt.checkpw(str.encode(plain_password), str.encode(user.password))

    async def get_statistics(self, user_id: int):
        delivery_task_service = DeliveryTaskService(self.database_service)
        delivery_tasks = await delivery_task_service.get_all_user_tasks(user_id)

        price_service = PriceService(self.database_service)
        cost = (await price_service.get_cost()).cost

        cur_date = datetime.datetime.now().date()
        start_date = datetime.datetime.combine(cur_date, datetime.time(0, 0)) + datetime.timedelta(days=-cur_date.weekday())
        cur_week = {}
        for i in range(0, 7):
            cur_week[(start_date + datetime.timedelta(days=i)).date()] = 0

        summary_way_len = 0
        orders_count = 0

        today_summary_way_len = 0
        today_orders_count = 0
        for delivery_task in delivery_tasks:
            if delivery_task.status_id == 5:
                print(delivery_task)
                if delivery_task.date.date() == datetime.datetime.now().date():
                    today_summary_way_len += delivery_task.delivery_way_len
                    today_orders_count += len(delivery_task.orders)
                summary_way_len += delivery_task.delivery_way_len
                orders_count += len(delivery_task.orders)

                if (delivery_task.date.date() in cur_week.keys()):
                    cur_week[delivery_task.date.date()] += delivery_task.delivery_way_len * cost

        data = {}
        data["delivered"] = {}
        data["delivered"]["perDay"] = today_orders_count
        data["delivered"]["perMonth"] = orders_count
        data["earned"] = {}
        data["earned"]["perDay"] = today_summary_way_len * cost
        data["earned"]["perMonth"] = summary_way_len * cost
        keys = list(cur_week.keys())
        data["income"] = {}
        data["income"]["monday"] = cur_week.get(keys[0])
        data["income"]["tuesday"] = cur_week.get(keys[1])
        data["income"]["wednesday"] = cur_week.get(keys[2])
        data["income"]["thursday"] = cur_week.get(keys[3])
        data["income"]["friday"] = cur_week.get(keys[4])
        data["income"]["saturday"] = cur_week.get(keys[5])
        data["income"]["sunday"] = cur_week.get(keys[6])

        return data

