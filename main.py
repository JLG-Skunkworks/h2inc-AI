"""Main module for h2inc GUI"""
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk # noqa
import globvar
import gui
import h2inc_AI as h2inc

if __name__ == "__main__":
    globvar.AI = h2inc.H2incAi("h2inc_AI")
    print(globvar.AI.get_version(), globvar.AI.get_copyright(), globvar.AI.get_author(), globvar.AI.get_contact(), sep = " - ")
    app = Gtk.Application(application_id="org.gtk.Example")
    app.connect("activate", gui.on_activate)
    app.run(None)
    