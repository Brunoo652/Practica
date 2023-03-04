import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def show_print(signaled_object):
    print("El usuario ha cerrado la ventana correctamente")


window = Gtk.Window(title="HOLA MUNDO")
window.show()
window.connect("destroy", Gtk.main_quit)
Gtk.main()