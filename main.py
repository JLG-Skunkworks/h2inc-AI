import globvar
import sys
import gi
import gui

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, GObject  # noqa

#global ai

if __name__ == "__main__":
    globvar.init()
    print(globvar.ai.getVersion(), globvar.ai.getCopyright(), globvar.ai.getAuthor(), globvar.ai.getContact(), sep = " - ")
    app = Gtk.Application(application_id="org.gtk.Example")
    app.connect("activate", gui.on_activate)
    app.run(None)