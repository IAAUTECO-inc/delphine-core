import sys
import logging
from PySide6.QtWidgets import QApplication
from koalixcrm.gui.mainwindow import MainWindow
from koalixcrm.database import init_db
from config import get_logger

logger = get_logger(__name__)

def main():
    logger.info("Starting KoalixCRM Application...")
    
    # Initialize Database
    try:
        init_db()
        logger.info("Database initialized successfully.")
    except Exception as e:
        logger.critical(f"Failed to initialize database: {e}")
        sys.exit(1)

    app = QApplication(sys.argv)
    app.setApplicationName("KoalixCRM")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
