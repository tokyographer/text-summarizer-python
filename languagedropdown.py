from tkinter.ttk import Combobox

class dropdown(Combobox):
    def __init__(self, window, filename):
        super().__init__(window)
        self.values = []
        self.populate_values(filename)

    def populate_values(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                language = line.strip()
                self.values.append(language)
        self['values'] = self.values
