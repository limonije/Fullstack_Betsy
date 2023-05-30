from peewee import Model, SqliteDatabase, CharField, TextField
from peewee import ForeignKeyField, IntegerField, DecimalField

db = SqliteDatabase('betsy.db')
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField(index=True)
    street_address = CharField()
    postal_code = CharField(max_length=6)
    city = CharField()
    bill_info = CharField()


class Tag(BaseModel):
    name = CharField(unique=True, index=True)


class Product(BaseModel):
    name = CharField(index=True)
    description = TextField()
    price_per_unit = DecimalField(decimal_places=2, auto_round=True)
    quantity = IntegerField()
    owner = ForeignKeyField(User)
    tag = ForeignKeyField(Tag, backref='products')


class ProductTag(BaseModel):
    product = ForeignKeyField(Product, backref='producttags')
    tag = ForeignKeyField(Tag, backref='producttags')


class Transaction(BaseModel):
    product_sold = ForeignKeyField(Product)
    # seller = ForeignKeyField(User)
    buyer = ForeignKeyField(User)
    amount_sold = IntegerField()

    # class Meta:
    #    indexes = (
    #        (('seller', 'buyer'), True),
    #    )


def create_tables():
    with db:
        db.drop_tables([User, Product, Tag, ProductTag, Transaction])
        db.create_tables([User, Product, Tag, ProductTag, Transaction])


def print_all_users():
    query_all = User.select()
    for user in query_all:
        print(user.id, user.name)


def print_all_tags():
    query_all = Tag.select()
    for tag in query_all:
        print(tag.id, tag.name)


def print_all_products():
    query_all = Product.select()
    for prod in query_all:
        print("Index", prod.id, prod.name, "(s) that seller", prod.owner.name,
              "with ID", prod.owner.id, "has in stock", prod.quantity)


def print_all_transactions():
    query_all = Transaction.select()
    for t in query_all:
        print(t.buyer.name, "bought", t.amount_sold, t.product_sold.name,
              "(s) with index", t.product_sold.id)
