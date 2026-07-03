from sqlalchemy.orm import Session

from backend.app.models.customer_metrics import CustomerMetrics


def get_customers(db: Session, skip: int = 0, limit: int = 5):
    """指定した範囲の顧客データと総件数を取得する"""
    total_count = db.query(CustomerMetrics).count()
    target_customers = db.query(CustomerMetrics).offset(skip).limit(limit).all()
    return {"total_count": total_count, "items": target_customers}
