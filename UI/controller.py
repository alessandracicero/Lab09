import flet as ft

from testModel import dstnc


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        self._view.txt_result.controls.clear()
        try:
            dstnc = int(self._view.txt_distanza.value)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Inserisci valore numerico"))
            self._view.update_page()
            return

        self._model.buildGraph(dstnc)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumNodi()} aeroporti e {self._model.getNumArchi()} voli "))

        res = self._model.getArchiPeso()
        for i in res:
            self._view.txt_result.controls.append(ft.Text(f"{i[0]} --> {i[1]}: {i[2]} miglia"))

        self._view.update_page()