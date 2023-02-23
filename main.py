from app import CrazyVillage

from logging import basicConfig, INFO, info, error
basicConfig(level=INFO, format='%(message)s')


def main():
    """ Initializes and runs the CrazyVillage application """
    try:
        app = CrazyVillage()
        app.run()
        info('❌ Игра закрылась!')

    except Exception as err:
        # Handling exceptions
        error(f'❌❌❌ Возникла ошибка при запуске игры:')
        error(f'{err}')
        exit(1)


if __name__ == '__main__':
    main()
