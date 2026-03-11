# from server import Base
# from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, Text, Float, JSON, func

# Example model class with various field types
# This class is just an example and should be replaced with your actual model.

# class Item(Base):
#     __tablename__ = 'items'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(100), nullable=False)
#     expiration_date = Column(Date, nullable=False)
#     opened_date = Column(Date)
#     expiration_days_after_open = Column(Integer, default=7)
#     user_id = Column(String(100), nullable=False)
#     price = Column(Float)
#     created_at = Column(DateTime, default=func.current_timestamp())
#     is_active = Column(Boolean, default=True)
#     description = Column(Text)
#     data = Column(JSON)
#
#     def __repr__(self):
#         return f'<Item {self.name}>'