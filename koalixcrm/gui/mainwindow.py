from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QToolBar, QStatusBar
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KoalixCRM - Desktop")
        self.resize(1024, 768)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        label = QLabel("Welcome to KoalixCRM")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        
        # Toolbar
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)
        
        action_customers = QAction("Customers", self)
        action_customers.setStatusTip("Manage Customers")
        action_customers.triggered.connect(self.show_customers)
        toolbar.addAction(action_customers)
        
        action_contracts = QAction("Contracts", self)
        action_contracts.setStatusTip("Manage Contracts")
        toolbar.addAction(action_contracts)

        # Status Bar
        self.setStatusBar(QStatusBar(self))
        
    def show_customers(self):
        self.statusBar().showMessage("Switching to Customers view...")
        # Logic to switch central widget or open new window would go here
