from typing import List, Literal

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class BaseSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,  # ORMオブジェクトの属性とPydanticモデル間の変換を許可
        alias_generator=to_camel,  # キャメルケース変換を自動化
        populate_by_name=True,  # スネークケース名でのアクセスも許可
    )


class PredictionInput(BaseSchema):
    # --- 顧客属性 ---
    state: str = Field(
        ..., pattern="^[A-Z]{2}$", description="居住州（2文字コード）", examples=["NJ"]
    )
    area_code: str = Field(
        ...,
        pattern=r"^area_code_\d{3}$",
        description="エリアコード",
        examples=["area_code_415"],
    )
    account_length: int = Field(..., gt=0, description="契約期間（月数）")

    # --- プラン情報 ---
    international_plan: Literal["yes", "no"] = Field(
        ..., description="国際通話プラン", examples=["yes"]
    )
    voice_mail_plan: Literal["yes", "no"] = Field(
        ..., description="ボイスメールプラン", examples=["yes"]
    )
    number_vmail_messages: int = Field(..., ge=0, description="ボイスメールの件数")

    # --- 通話利用状況 ---
    total_day_minutes: float = Field(..., ge=0, description="昼間の通話時間（分）")
    total_day_calls: int = Field(..., ge=0, description="昼間の通話回数")
    total_day_charge: float = Field(..., ge=0, description="昼間の通話料金")

    total_eve_minutes: float = Field(..., ge=0, description="夕方の通話時間（分）")
    total_eve_calls: int = Field(..., ge=0, description="夕方の通話回数")
    total_eve_charge: float = Field(..., ge=0, description="夕方の通話料金")

    total_night_minutes: float = Field(..., ge=0, description="夜間の通話時間（分）")
    total_night_calls: int = Field(..., ge=0, description="夜間の通話回数")
    total_night_charge: float = Field(..., ge=0, description="夜間の通話料金")

    total_intl_minutes: float = Field(..., ge=0, description="国際通話の時間（分）")
    total_intl_calls: int = Field(..., ge=0, description="国際通話の回数")
    total_intl_charge: float = Field(..., ge=0, description="国際通話の料金")

    # --- サポート状況 ---
    number_customer_service_calls: int = Field(
        ..., ge=0, description="カスタマーサービスへの通話回数"
    )

    model_config = ConfigDict(
        **BaseSchema.model_config,
        extra="ignore",  # 定義外のカラムは無視
    )


class CustomerDetail(BaseSchema):
    name: str
    state: str
    area_code: str
    contract_months: int


class PredictionResult(BaseSchema):
    probability: float = Field(..., ge=0, le=1, description="解約予測確率（0.0〜1.0）")


class PredictionOutput(BaseSchema):
    customer: CustomerDetail
    prediction: PredictionResult


class CustomerItem(BaseSchema):
    id: int
    customer_name: str
    customer_code: str


class CustomerListOutput(BaseSchema):
    total_count: int
    items: List[CustomerItem]
