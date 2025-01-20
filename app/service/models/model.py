from datetime import datetime
from typing import Optional, Dict

from pydantic import BaseModel, Field

from service.models.balace_sheets.balance_sheets import BalanceSheet

class Oscillations(BaseModel):
    day: Optional[str] = Field(alias='Dia')
    month: Optional[str] = Field(alias='Mês')
    last_30_days: Optional[str] = Field(alias='30 dias')
    last_12_months: Optional[str] = Field(alias='12 meses')

class Fundamentus(BaseModel):
    price_earnings: str = Field(alias='P/L')
    earnings_per_share: str = Field(alias='LPA')
    price_book_value: str = Field(alias='P/VP')
    book_value_per_share: str = Field(alias='VPA')
    price_ebit: str = Field(alias='P/EBIT')
    gross_margin: str = Field(alias='Marg. Bruta')
    price_sales: str = Field(alias='PSR')
    ebit_margin: str = Field(alias='Marg. EBIT')
    price_assets: str = Field(alias='P/Ativos')
    net_margin: str = Field(alias='Marg. Líquida')
    price_working_capital: str = Field(alias='P/Cap. Giro')
    ebit_assets: str = Field(alias='EBIT / Ativo')
    price_current_assets: str = Field(alias='P/Ativ Circ Liq')
    roic: str = Field(alias='ROIC')
    dividend_yield: str = Field(alias='Div. Yield')
    roe: str = Field(alias='ROE')
    enterprise_value_ebitda: str = Field(alias='EV / EBITDA')
    current_ratio: str = Field(alias='Liquidez Corr')
    enterprise_value_ebit: str = Field(alias='EV / EBIT')
    gross_dividend_assets: str = Field(alias='Div Br/ Patrim')
    revenue_growth_5_years: str = Field(alias='Cres. Rec (5a)')
    asset_turnover: str = Field(alias='Giro Ativos')
    
class Stock(BaseModel):
    stock: str = Field(alias='Papel')
    price: str = Field(alias='Cotação')
    type: str = Field(alias='Tipo')
    last_quotation_date: str = Field(alias='Data últ cot')
    company: str = Field(alias='Empresa')
    min_52_weeks: str = Field(alias='Min 52 sem')
    max_52_weeks: str = Field(alias='Max 52 sem')
    sector: str = Field(alias='Setor')
    subsector: str = Field(alias='Subsetor')
    average_volume: str = Field(alias='Vol $ méd (2m)')
    market_value: str = Field(alias='Valor de mercado')
    last_balance: str = Field(alias='Últ balanço processado')
    firm_value: Optional[str] = Field(alias='Valor da firma')
    number_of_shares: str = Field(alias='Nro. Ações')
    oscillations: Oscillations = Field(alias='Oscilações')
    fundamentus: Fundamentus = Field(alias='Indicadores fundamentalistas')
    balance_sheet: BalanceSheet = Field(alias='Dados Balanço Patrimonial')
