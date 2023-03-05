import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell


class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()

    def __init__(self):
        super().__init__()
        self.connect("destroy", Gtk.main_quit)
        self.add(self.flowbox)
        cell_one = Cell("Serie 1", Gtk.Image.new_from_file("catalog\data\serie1.jpg"))
        cell_two = Cell("Serie 2", Gtk.Image.new_from_file("serie2.jpg"))
        cell_three = Cell("Serie 3", Gtk.Image.new_from_file("serie3.jpg"))
        cell_four = Cell("Serie 4", Gtk.Image.new_from_file("serie4.jpg"))
        cell_five = Cell("Serie 5", Gtk.Image.new_from_file("serie5.jpg"))
        self.flowbox.add(cell_one)
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)
