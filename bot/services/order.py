from collections import OrderedDict
from functools import lru_cache
from io import BytesIO

import xlsxwriter
from pyexcel_ods3 import save_data
from sqlalchemy import select

from services.base import BaseService
from db.storages import app_context
from models.app import Appeal
from models.views import AppealView


class OrderService(BaseService):
    _context = app_context

    async def _extract_data(self) -> list[Appeal]:
        async with self.context.session_builder.begin() as session:
            query = select(Appeal).order_by(Appeal.creation_date.asc())
            result = await session.execute(query)
            models = result.scalars().all()
            return models

    @staticmethod
    def _transform_data(data: list[Appeal]) -> list[AppealView]:
        return [
            AppealView(
                n=x+1,
                date=data[x].creation_date.isoformat(),
                text=data[x].text
            ) for x in range(len(data))
        ]

    @staticmethod
    def _generate_order_xlsx(data: list[AppealView]) -> BytesIO:
        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        worksheet.write(0, 0, "№")
        worksheet.write(0, 1, "Дата")
        worksheet.write(0, 2, "Ответ пользователя")

        for i in range(len(data)):
            worksheet.write(i+1, 0, data[i].n)
            worksheet.write(i+1, 1, data[i].date)
            worksheet.write(i+1, 2, data[i].text)

        worksheet.set_column(0, 0, 3)
        worksheet.set_column(1, 1, 25)

        workbook.close()
        output.seek(0)
        return output

    @staticmethod
    def _generate_order_ods(data: list[AppealView]) -> BytesIO:
        output = BytesIO()
        sheet_data = OrderedDict()
        data_to_write = [["№", "Дата", "Ответ пользователя"]]
        for x in data:
            data_to_write.append(
                [x.n+1, x.date, x.text]
            )
        sheet_data.update({'Sheet1': data_to_write})
        save_data(output, sheet_data)
        output.seek(0)
        return output

    async def get_admin_order_xlsx(self) -> BytesIO:
        raw_data = await self._extract_data()
        transformed_data = self._transform_data(raw_data)
        order = self._generate_order_xlsx(transformed_data)
        return order

    async def get_admin_order_ods(self) -> BytesIO:
        raw_data = await self._extract_data()
        transformed_data = self._transform_data(raw_data)
        order = self._generate_order_ods(transformed_data)
        return order


@lru_cache
def get_order_service() -> OrderService:
    return OrderService()
