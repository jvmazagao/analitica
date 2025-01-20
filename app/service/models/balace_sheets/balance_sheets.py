
from typing import Union
from pydantic import BaseModel, Field, model_validator, RootModel, root_validator


class BankBalanceSheet(BaseModel):
    asset: str = Field(alias='Ativo')
    deposits: str = Field(alias='Depósitos')
    credit_card: str = Field(alias='Cart. de Crédito')
    net_worth: str = Field(alias='Patrim. Líq')
    financial_income: str = Field(alias='Result Int Financ')
    service_income: str = Field(alias='Rec Serviços')
    net_income: str = Field(alias='Lucro Líquido')

class GenericBalanceSheet(BaseModel):
    asset: str = Field(alias='Ativo')
    gross_debt: str = Field(alias='Dív. Bruta')
    cash: str = Field(alias='Disponibilidades')
    net_debt: str = Field(alias='Dív. Líquida')
    current_asset: str = Field(alias='Ativo Circulante')
    net_worth: str = Field(alias='Patrim. Líq')
    net_revenue: str = Field(alias='Receita Líquida')
    ebit: str = Field(alias='EBIT')
    net_income: str = Field(alias='Lucro Líquido')

class BalanceSheet(RootModel):
    root: Union[BankBalanceSheet, GenericBalanceSheet]

    @model_validator(mode="before")
    def validate_balance_sheet(cls, values):
        # Detect the type of balance sheet and instantiate the appropriate model
        if "Depósitos" in values:
            return  BankBalanceSheet(**values)
        return GenericBalanceSheet(**values)
