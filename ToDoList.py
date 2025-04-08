import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QCalendarWidget, QWidget, QVBoxLayout, QListWidget, QPushButton, QLineEdit, \
    QListWidgetItem


class ToDo:
    def __init__(self, task):
        self.task = task


class ToDoList(QWidget):
    def __init__(self):
        super().__init__()
        self.delete_button = None
        self.calendar = None
        self.date_picker = None
        self.add_to_do_button = None
        self.to_do_list = None
        self.ToDos = []
        self.new_to_do = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Alysha's To Do List")
        self.resize(800, 600)

        layout = QVBoxLayout(self)

        # Erstellen der Liste für ToDos
        self.to_do_list = QListWidget()
        layout.addWidget(self.to_do_list)

        # Erstellen des Buttons zum Hinzufügen von To-Dos
        self.add_to_do_button = QPushButton('Add To-Do', self)
        layout.addWidget(self.add_to_do_button)

        # Korrekte Verbindung des Buttons mit der Funktion add_to_do
        self.add_to_do_button.clicked.connect(self.add_to_do)

        # Eingabefeld für neue To-Do-Aufgaben
        self.new_to_do = QLineEdit(self)
        layout.addWidget(self.new_to_do)

        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.setFirstDayOfWeek(Qt.Monday)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        layout.addWidget(self.calendar)

    def add_to_do(self):
        to_do_text = self.new_to_do.text().strip()
        if to_do_text:
            new_to_do = ToDo(to_do_text)
            self.ToDos.append(new_to_do)
            item = QListWidgetItem(to_do_text)
            item.setCheckState(Qt.Unchecked)
            self.to_do_list.addItem(item)
            self.new_to_do.clear()

    def show(self):
        super().show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ToDoList()
    pink_stylesheet = """
    QWidget {
        background-color: #FFE6F0;
        color: #4B0036;
        font-size: 16px;
    }

    QLineEdit, QDateEdit {
        background-color: #FFFFFF;
        color: #4B0036;
        border: 2px solid #FFB6C1;
        border-radius: 6px;
        padding: 6px;
    }

    QPushButton {
        background-color: #FFB6C1;
        color: #4B0036;
        border: none;
        border-radius: 6px;
        padding: 8px;
    }

    QPushButton:hover {
        background-color: #FF69B4;
    }

    QListWidget {
        background-color: #FFFFFF;
        color: #4B0036;
        border: 2px solid #FFB6C1;
        border-radius: 6px;
    }
    """
    app.setStyleSheet(pink_stylesheet)
    ex.show()
    sys.exit(app.exec())
