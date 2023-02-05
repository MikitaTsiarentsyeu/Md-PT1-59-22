from data import select_user, create_user, validation_password, view_shop, user_cart, select_product_info, add_product, \
    delete_product


def register(login, password):
    """
    :param login: user login
    :param password: user password
    :return: True == User created success, False == user always been here, ERROR == config/unknown error
    """
    chec_user = select_user(login)
    if chec_user is None:
        return None
    elif chec_user:
        return False
    elif not chec_user:
        create_user(login,password)
        return True

def authorization(login, password):
    """

    :param login: user login
    :param password: password login
    :return: True == Success authorization ; False == failed authorization
    """
    result = validation_password(login, password)
    if result is None:
        return None
    elif result:
        return True
    elif not result:
        return False

def shop_lst():
    """
    This raw need to visualise
    :return: content and row count
    """
    source = view_shop()
    result = len(source)
    return [source, result]

def user_cart_source(user):
    """
    This raw need to visualise
    :return: content and row count
    """
    source = user_cart(user)
    result = len(source)
    return [source, result]

def add_product_cart(id_row_product, user):
    """

    :param id_row_product: id ROW in shop table
    :param user: login user
    :return: True - all fine: False correct parameters need
    """
    info = select_product_info(id_row_product)
    if info == []:
        return False
    add_product(user, info[0][0], info[0][1], info[0][2])
    return True

def delete_product_cart(id_row_product, user):
    delete_product(id_row_product, user)
    return True

if __name__ == "__main__":
    # print(authorization('admin', '123'))
    # print(shop_lst())
    # print(add_product_cart('3', 'admin'))
    delete_product_cart('1', "admin")