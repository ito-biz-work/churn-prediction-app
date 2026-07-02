from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.sql import func

from backend.app.database import Base
from config.settings import TABLE_NAME


class CustomerMetrics(Base):
    __tablename__ = TABLE_NAME

    # データベース用のユニークID（主キー）
    id = Column(Integer, primary_key=True, index=True)

    # システム項目
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), onupdate=func.now(), server_default=func.now()
    )

    # 退会確率
    churn_probability = Column(Float, nullable=True)

    # 画面表示用のダミー情報
    customer_code = Column(String)
    customer_name = Column(String)

    # 顧客属性
    state = Column(String)
    area_code = Column(String)
    account_length = Column(Integer)

    # プラン情報
    international_plan = Column(String)
    voice_mail_plan = Column(String)
    number_vmail_messages = Column(Integer)

    # 通話利用状況
    total_day_minutes = Column(Float)
    total_day_calls = Column(Integer)
    total_day_charge = Column(Float)

    total_eve_minutes = Column(Float)
    total_eve_calls = Column(Integer)
    total_eve_charge = Column(Float)

    total_night_minutes = Column(Float)
    total_night_calls = Column(Integer)
    total_night_charge = Column(Float)

    total_intl_minutes = Column(Float)
    total_intl_calls = Column(Integer)
    total_intl_charge = Column(Float)

    # サポート状況
    number_customer_service_calls = Column(Integer)
