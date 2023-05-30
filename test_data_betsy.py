import models


def populate_test_database():

    models.create_tables()

    models.User.create(
        name='Mo',
        street_address='Bloemstraat 5',
        postal_code='1234AB', city='Utrech',
        bill_info='mo@leve.nl')
    models.User.create(
        name='Jans', street_address='Bloemstraat 9',
        postal_code='1111AA', city='Mestrech',
        bill_info='jans@leve.nl')
    models.User.create(
        name='Nelis',
        street_address='Rode Bloemstraat 7',
        postal_code='3434NV', city='Adam',
        bill_info='nelis@leve.nl')
    models.User.create(
        name='Lov', street_address='Bloemstraat 3',
        postal_code='5555ZZ', city='Rotjeknor',
        bill_info='lov@leve.nl')

    models.Product.create(
        name='Sweater', description='Blue cotton sweater',
        price_per_unit=24.99, quantity=10, owner=1, tag=1)
    models.Product.create(
        name='sweater', description='Sale Red Cotton Sweater',
        price_per_unit=14.99, quantity=20, owner=2, tag=1)
    models.Product.create(
        name='Lego', description='Lego set Zweinstein 76399',
        price_per_unit=47.99, quantity=15, owner=1, tag=3)
    models.Product.create(
        name='lego', description='Lego set Zweinstein 76400',
        price_per_unit=20.99, quantity=25, owner=3, tag=3)
    models.Product.create(
        name='Jacket', description='Leather jacket black',
        price_per_unit=124.99, quantity=5, owner=4, tag=1)
    models.Product.create(
        name='Nike', description='Air Jordan 1 Mid',
        price_per_unit=129.99, quantity=10, owner=2, tag=2)
    models.Product.create(
        name='Nike', description='Dunk High',
        price_per_unit=119.99, quantity=5, owner=4, tag=2)

    models.Tag.create(name='Clothes')
    models.Tag.create(name='Shoes')
    models.Tag.create(name='Toys')


if __name__ == "__main__":
    populate_test_database()
