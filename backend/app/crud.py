from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from backend.app.models.customer_metrics import CustomerMetrics


def get_customers(db: Session, skip: int, limit: int):
    """指定した範囲の顧客データと総件数を取得する"""
    stmt = db.query(CustomerMetrics)

    total_count = stmt.count()
    target_customers = (
        stmt.order_by(CustomerMetrics.id.asc()).offset(skip).limit(limit).all()
    )
    return {"total_count": total_count, "items": target_customers}


def check_db_health(db: Session):
    """DB接続を確認する（失敗時はそのまま例外を投げる）"""
    db.execute(text("SELECT 1"))
