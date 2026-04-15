import sys
from PyQt6 import QtWidgets, uic
from threading import Thread
from ia_engine import preguntar_a_gemini

class ChatBotWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interfaz.ui", self)
        self.setStyleSheet("""
    QMainWindow { background-color: #1e1e1e; }
    QTextEdit { 
        background-color: #252526; 
        color: #d4d4d4; 
        border-radius: 10px; 
        padding: 10px;
        font-size: 14px;
    }
    QLineEdit { 
        background-color: #3c3c3c; 
        color: white; 
        border-radius: 5px;
        padding: 5px;
    }
    QPushButton {
        background-color: #0e639c;
        color: white;
        font-weight: bold;
        border-radius: 5px;
    }
    QPushButton:hover { background-color: #1177bb; }
""")
        #conexiones
        self.btn_enviar.clicked.connect(self.iniciar_hilo_ia)
        self.input_mensaje.returnPressed.connect(self.iniciar_hilo_ia)

    def iniciar_hilo_ia(self):
        texto_usuario = self.input_mensaje.text().strip()
        if not texto_usuario:
            return
        
        # Mostrar lo que escribió el usuario
        self.txt_chat.append(f"<b>Tú:</b> {texto_usuario}")
        self.input_mensaje.clear()
        
        # hilo para que la IA no trabe la ventana
        hilo = Thread(target=self.proceso_ia, args=(texto_usuario,))
        hilo.start()

    def proceso_ia(self, mensaje):
        # La IA piensa (esto tarda unos segundos)
        respuesta = preguntar_a_gemini(mensaje)
        
        # Mostramos la respuesta (usando invoke para seguridad de hilos)
        self.txt_chat.append(f"<b>IA:</b> {respuesta}<br>")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = ChatBotWindow()
    ventana.show()
    sys.exit(app.exec())