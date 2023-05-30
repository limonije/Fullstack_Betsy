__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

import models
import test_data_betsy
test_data_betsy.populate_test_database()

M = models
M.print_all_users()


def delete_user(name):
    query_search = (M.User.select().where
                    (M.User.name.contains(name)))
    for user in query_search:
        user.delete_instance()
        M.print_all_users


def search(term):
    query_search = (M.Product.select().where
                    (M.Product.name.contains(term) |
                     M.Product.description.contains(term)))
    for prod in query_search:
        return [prod.name, prod.owner.name]


# print(search('Jordan'))


def list_user_products(user_id):
    query_user_products = (M.Product.select(M.Product, M.User)
                            .join(M.User)
                            .where(M.User.id == user_id))
    for prod in query_user_products:
        print(
            "Seller", prod.owner.name, "has", prod.quantity, prod.name,
            "(s) in stock with description", prod.description,
            "for a price per unit of", prod.price_per_unit)


# list_user_products(4)


def list_products_per_tag(tag_id):
    M.print_all_tags()
    query = (M.Product.select(M.Product, M.Tag)
             .join(M.Tag)
             .where(M.Tag.id == tag_id))
    for prodtag in query:
        return [prodtag.tag.name, prodtag.name, prodtag.description]


# list_products_per_tag(2)


def add_product_to_catalog(user_id, product):
    M.Product.create(
        name=product, description=product, price_per_unit=99.99, quantity=2,
        owner=user_id, tag=1)


# add_product_to_catalog(4, 'Ski jacket')
# search('jacket')
# list_user_products(4)


def update_stock(product_id, new_quantity):
    product = M.Product.select().where(M.Product.id == product_id).first()
    product.quantity = new_quantity
    product.save()


# update_stock(8, 3)
# list_user_products(4)


def purchase_product(product_id, buyer_id, quantity):
    M.Transaction.create(product_sold=product_id, buyer=buyer_id,
                         amount_sold=quantity)
    M.print_all_transactions()


# purchase_product(1, 4, 2)


def remove_product(product_id):
    query_remove = (M.Product.select().where
                    (M.Product.id == product_id))
    for product in query_remove:
        product.delete_instance()


# remove_product(5)
# list_user_products(4)


# Handle a purchase
M.print_all_products()
# Give Product ID, buyer ID and amount to purchase product
purchase_product(1, 4, 2)
# Check list all products to identify the seller ID and current stock,
# adjust value of stock to right amount to update stock
update_stock(1, 8)
# Check if stock is adjusted correctly by viewing the current list of products
# of the seller based on the seller ID.
list_user_products(1)
