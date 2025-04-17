from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QGroupBox
)
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt, QSize
import os, shutil, tempfile, subprocess, sys

class OtimizadorPC(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("🛠️ Otimizador de PC")
        self.setGeometry(100, 100, 600, 720)
        self.setFixedSize(600, 720)

        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(30, 30, 30))
        palette.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(palette)

        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: #f0f0f0;
                font-family: 'Segoe UI', sans-serif;
            }
            QPushButton {
                background-color: #2d89ef;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
                margin-bottom: 8px;
            }
            QPushButton:hover {
                background-color: #1b65b8;
            }
            QLabel#titulo {
                font-size: 22px;
                font-weight: bold;
                color: #ffffff;
            }
            QLabel#status {
                font-size: 14px;
                color: #cccccc;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        self.label_titulo = QLabel("🧰 Otimizador de PC")
        self.label_titulo.setObjectName("titulo")
        self.label_titulo.setFont(QFont("Segoe UI", 20, QFont.Bold))
        self.label_titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_titulo)

        # Seções agrupadas
        layout.addWidget(self.criar_secao("Limpeza", [
            ("🧹 Limpar Temporários", self.limpar_temporarios),
            ("🗑️ Esvaziar Lixeira", self.esvaziar_lixeira),
            ("🧽 Limpar Cache do Windows Update", self.limpar_cache_windows_update),
            ("🧼 Limpar Prefetch", self.limpar_prefetch),
        ]))

        layout.addWidget(self.criar_secao("Desempenho", [
            ("🔄 Ativar Modo Desempenho (efeitos off)", self.desativar_efeitos_visuais),
            ("🎭 Desativar Efeitos de Transparência", self.desativar_transparencia),
            ("⚡ Plano de Energia: Alto Desempenho", self.mudar_plano_energia),
            ("🧯 Desativar Serviços Desnecessários", self.desativar_servicos),
            ("🛑 Desativar Serviços Inúteis", self.desativar_servicos_inuteis),
            ("🧠 Liberar Memória RAM", self.liberar_memoria_ram),
        ]))

        layout.addWidget(self.criar_secao("Sistema", [
            ("🔎 Verificar Sistema (sfc/scannow)", self.verificar_sfc),
            ("🧩 Otimizar Inicialização", self.otimizar_inicio),
            ("🧭 Desfragmentar Disco", self.desfragmentar_disco),
            ("🚫 Mostrar Programas de Inicialização", self.mostrar_programas_inicio),
            ("🛡️ Criar Ponto de Restauração", self.criar_ponto_restauracao),
        ]))

        self.status_label = QLabel("✅ Pronto para otimizar!")
        self.status_label.setObjectName("status")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def criar_secao(self, titulo, botoes):
        grupo = QGroupBox(titulo)
        vbox = QVBoxLayout()
        for texto, func in botoes:
            btn = QPushButton(texto)
            btn.clicked.connect(func)
            vbox.addWidget(btn)
        grupo.setLayout(vbox)
        return grupo

    # Funções (algumas omitidas por espaço, mas você pode colar as que já tem)
    def limpar_temporarios(self): pass
    def esvaziar_lixeira(self): pass
    def limpar_cache_windows_update(self): pass
    def limpar_prefetch(self): pass
    def desativar_efeitos_visuais(self): pass
    def desativar_transparencia(self): pass
    def mudar_plano_energia(self): pass
    def desativar_servicos(self): pass
    def desativar_servicos_inuteis(self): pass
    def liberar_memoria_ram(self): pass
    def verificar_sfc(self): pass
    def otimizar_inicio(self): pass
    def desfragmentar_disco(self): pass
    def mostrar_programas_inicio(self): pass
    def criar_ponto_restauracao(self): pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = OtimizadorPC()
    janela.show()
    sys.exit(app.exec_())
