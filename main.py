from controllers.menu import MenuControllers
from views.menu import MenuViews


def main():
    MenuViews.app_title()
    MenuControllers().main_menu_start()


if __name__ == "__main__":
    main()
