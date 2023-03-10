'''This is the main GUI file for h2inc-AI'''
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, GObject  # noqa



class DataObject(GObject.GObject):
    """_summary_"""
    def __init__(self, fruit: str, color: str):
        """_summary_

        Args:
            fruit (str): _description_
            color (str): _description_
        """
        super(DataObject, self).__init__()
        self.fruit = fruit
        self.color = color


def setup(widget, item):
    """Setup the widget to show in the Gtk.Listview"""
    label = Gtk.Label()
    label.props.xalign = 0.0
    item.set_child(label)


def bind_fruit(widget, item):
    """bind data from the store object to the widget"""
    label = item.get_child()
    obj = item.get_item()
    label.set_label(obj.fruit)


def bind_color(widget, item):
    """bind data from the store object to the widget"""
    label = item.get_child()
    obj = item.get_item()
    label.set_label(obj.color)


def on_activate(app):
    """_summary_

    Args:
        app (_type_): _description_
    """
    import globvar
    ver = globvar.AI.get_version()
    win = Gtk.ApplicationWindow(
        application=app,
        title="h2inc-AI "+ver,
        default_height=400,
        default_width=400,
    )
    sw = Gtk.ScrolledWindow()
    column_view = Gtk.ColumnView()
    column_view.props.show_row_separators = True
    column_view.props.show_column_separators = True
    fruit_col = Gtk.ColumnViewColumn.new("Fruit")
    fruit_col.set_resizable(True)
    fruit_col.set_fixed_width(200)
    fruit_factory = Gtk.SignalListItemFactory()
    fruit_factory.connect("setup", setup)
    fruit_factory.connect("bind", bind_fruit)
    fruit_col.set_factory(fruit_factory)
    column_view.append_column(fruit_col)
    color_col = Gtk.ColumnViewColumn.new("Color")
    color_col.set_resizable(True)
    color_col.set_fixed_width(200)
    color_factory = Gtk.SignalListItemFactory()
    color_factory.connect("setup", setup)
    color_factory.connect("bind", bind_color)
    color_col.set_factory(color_factory)
    column_view.append_column(color_col)
    selection = Gtk.SingleSelection()
    store = Gio.ListStore.new(DataObject)
    selection.set_model(store)
    column_view.set_model(selection)
    store.append(DataObject("Apple", "Green"))
    store.append(DataObject("Apple", "Yellow"))
    store.append(DataObject("Apple", "Red"))
    store.append(DataObject("Banana", "Yellow"))
    sw.set_child(column_view)
    win.set_child(sw)
    win.present()