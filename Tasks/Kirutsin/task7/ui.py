from bl import register, authorization, shop_lst, user_cart_source, add_product_cart, delete_product_cart


def maincycle():

    autorisation = """
    o. Exit
    1. Login
    2. Register
    3. View shop
    """

    print("Hello!\nWelcome to the shop!")

    while True:
        print(autorisation)
        user_choise = input()

        if user_choise == "0":
            print("Goodbye")
            break

        elif user_choise == "1":
            while True:
                username = input('Enter your login please\n*0. For exit\n')
                if username == "0":
                    break

                password = input('Input your password\n*0. For exit\n')
                if password == "0":
                    break

                user_authorization_result = authorization(username, password)

                if user_authorization_result:
                    while True:
                        user_bo = """
                        o. Exit
                        1. View shop
                        2. Show shopping cart
                        """
                        user_bo = input(user_bo)

                        if user_bo == "0":
                            break
                        elif user_bo == "1":
                            table = f"""
                            \t|id   |product   |price   |currency   | 
                            """
                            content = shop_lst()
                            for i in range(content[1]):
                                table += f"""
                                \t|{content[0][i][3]}   |{content[0][i][0]}   |{content[0][i][1]}   |{content[0][i][2]}   |
                                """
                            print(table)

                        elif user_bo == "2":
                            while True:

                                user_card_table = f"""
                                \t|id   |product   |price   |currency   | 
                                """
                                content = user_cart_source(username)
                                for i in range(content[1]):
                                    user_card_table += f"""
                                    \t|{content[0][i][3]}   |{content[0][i][0]}   |{content[0][i][1]}   |{content[0][i][2]}   |
                                    """
                                print(user_card_table)
                                user_anser = input("""
                                0. Exit
                                1. Add product
                                2. Delete product
                                """)
                                if user_anser == "0":
                                    break
                                elif user_anser == "1":
                                    table = f"""
                                    \t|id   |product   |price   |currency   | 
                                    """
                                    content = shop_lst()
                                    for i in range(content[1]):
                                        table += f"""
                                        \t|{content[0][i][3]}   |{content[0][i][0]}   |{content[0][i][1]}   |{content[0][i][2]}   |
                                        """
                                    print("Our products:\n", table, "\nPlease provide ID")
                                    product_id = input("ID=")
                                    add_product_cart(product_id, username)
                                elif user_anser == "2":
                                    print("Please provide ID")
                                    product_id = input("ID=")
                                    delete_product_cart(product_id, username)

                        else:
                            print("Please choose correct point")

                elif not user_authorization_result:
                    print("Please check your login")

                else:
                    print("I am temporarily unavailable, please try again later ")

        elif user_choise == "2":
            username = input('Enter your login please\n')
            password = input('Input your password\n')
            user_process_result = register(username, password)

            if user_process_result:
                print("Done!\nThe login is already in use")

            elif not user_process_result:
                print("User always been here. Use please login")

            else:
                print("I am temporarily unavailable, please try again later ")

        elif user_choise == "3":

            table = f"""
                \t|id   |product   |price   |currency   | 
            """
            content = shop_lst()

            for i in range(content[1]):
                table += f"""
                \t|{content[0][i][3]}   |{content[0][i][0]}   |{content[0][i][1]}   |{content[0][i][2]}   |
                """
            print(table)

        else:
            print("Please choose correct point")

if __name__ == "__main__":
    maincycle()