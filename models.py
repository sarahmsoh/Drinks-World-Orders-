from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///database.db')
Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship('Customer', backref='orders')
    order_date = Column(String)
    total = Column(Float)

    def __repr__(self):
        return f"Order('{self.order_date}', '{self.total}')"


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


    def __repr__(self):
        return f"Customer('{self.name}', '{self.email}')"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

class OrderORM:
    @classmethod
    def create(cls, customer_id, order_date, total):
        order = Order(customer_id=customer_id, order_date=order_date, total=total)
        session.add(order)
        session.commit()
        return order

    @classmethod
    def delete(cls, id):
        order = session.query(Order).get(id)
        if order:
            session.delete(order)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls):
        return session.query(Order).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(Order).get(id)

    @classmethod
    def find_by_customer_id(cls, customer_id):
        return session.query(Order).filter_by(customer_id=customer_id).all()

class CustomerORM:
    @classmethod
    def create(cls, name, email):
        customer = Customer(name=name, email=email)
        session.add(customer)
        session.commit()
        return customer

    @classmethod
    def delete(cls, id):
        customer = session.query(Customer).get(id)
        if customer:
            session.delete(customer)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls):
        return session.query(Customer).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(Customer).get(id)

    @classmethod
    def find_by_name(cls, name):
        return session.query(Customer).filter_by(name=name).first()