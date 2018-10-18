class DataBase:
    _counter = None
    _open_message = None
    _close_message = None

    def __init__(self):
        self.count = self._counter
        type(self)._counter += 1
        print(f'\n {self._open_message}: {self.count}')

    def close(self):
        print(f'\n{self._close_message}: {self.count}')


class Connection(DataBase):
    _counter = 1
    _open_message = 'Opening Costly DataBase Connection'
    _close_message = 'Closing Costly DataBase Connection'


class Session(DataBase):
    _counter = 1
    _open_message = 'Opening Cheap DataBase Session'
    _close_message = 'Rolling Back Cheap DataBase Session'


if __name__ == '__main__':
    db_objects = [Connection() for i in range(3)]
    db_objects.extend([Session() for i in range(3)])
    for conn in db_objects:
        conn.close()
