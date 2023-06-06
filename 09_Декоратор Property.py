
class Notebook:

    def __init__(self, list_val: list):
        self._notes = list_val

    @property
    def notes_list(self):
        for numb, val in enumerate(self._notes, 1):
            print(f'{numb}.{val}')

note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list