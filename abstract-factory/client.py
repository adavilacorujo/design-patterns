# should only be concered with calling the object and executing code
from concrete_products import create_app


if __name__ == '__main__':
    config = {
        'style': 'finance',
        'title': 'Finance Dashboard',
        'data_api': 'https://localhost',
        'OS': 'WINDOWS'
    }

    app = create_app(**config)
    app.create_UI()
    print(app.paint())