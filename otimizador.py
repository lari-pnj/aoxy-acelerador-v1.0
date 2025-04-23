from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QGroupBox, QGridLayout, QHBoxLayout
)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import sys

class OtimizadorPC(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("🛠️ Otimizador Aoxy")
        self.setGeometry(100, 100, 600, 720)
        self.setFixedSize(600, 720)

        self.init_ui()

    def init_ui(self):
        # Aplicando o tema original (escuro)
        self.aplicar_tema_escuro()

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Cabeçalho com título e imagem ao lado
        topo_layout = QHBoxLayout()
        self.label_imagem = QLabel()
        self.label_imagem.setPixmap(QPixmap("imagem ").scaledToHeight(30))  # Coloque o caminho da sua imagem
        self.label_imagem.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.label_titulo = QLabel("🧰 Otimizador Aoxy")
        self.label_titulo.setObjectName("titulo")
        self.label_titulo.setFont(QFont("Segoe UI", 28, QFont.Bold))
        self.label_titulo.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        topo_layout.addWidget(self.label_imagem)  # Adicionando a imagem
        topo_layout.addWidget(self.label_titulo)
        topo_layout.addStretch()
        layout.addLayout(topo_layout)

        layout.addWidget(self.criar_secao_grade("Limpeza", [
            ("🧹 Limpar Temporários", self.limpar_temporarios),
            ("🗑️ Esvaziar Lixeira", self.esvaziar_lixeira),
            ("🧽 Limpar Cache do Windows Update", self.limpar_cache_windows_update),
            ("🧼 Limpar Prefetch", self.limpar_prefetch),
        ]))

        layout.addWidget(self.criar_secao_grade("Desempenho", [
            ("🔄 Ativar Modo Desempenho (efeitos off)", self.desativar_efeitos_visuais),
            ("🎭 Desativar Efeitos de Transparência", self.desativar_transparencia),
            ("⚡ Plano de Energia: Alto Desempenho", self.mudar_plano_energia),
            ("🧯 Desativar Serviços Desnecessários", self.desativar_servicos),
            ("🛑 Desativar Serviços Inúteis", self.desativar_servicos_inuteis),
            ("🧠 Liberar Memória RAM", self.liberar_memoria_ram),
        ]))

        layout.addWidget(self.criar_secao_grade("Sistema", [
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

    def aplicar_tema_escuro(self):
        # Aplicando o tema escuro com fundo preto e botões azuis
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: #f0f0f0;
                font-family: 'Segoe UI', sans-serif;
            }
            QGroupBox {
                background-color: rgba(44, 62, 80, 0.8);
                color: white;
                font-weight: bold;
                border: 1px solid #444;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                padding-left: 10px;
                font-size: 16px;
                color: white;
            }
            QPushButton {
                background-color: #2d89ef;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
                margin-bottom: 6px;
            }
            QPushButton:hover {
                background-color: #1b65b8;
            }
            QLabel#titulo {
                color: white;
                font-size: 28px;
                font-weight: bold;
            }
            QLabel#status {
                color: #cccccc;
            }
        """)

    def criar_secao_grade(self, titulo, botoes):
        grupo = QGroupBox(titulo)
        grupo.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 1px solid #444;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                padding-left: 10px;
                font-size: 16px;
                color: white;
            }
        """)
        grid = QGridLayout()
        grid.setSpacing(8)
        colunas = 2
        for i, (texto, func) in enumerate(botoes):
            btn = QPushButton(texto)
            btn.setMinimumHeight(35)
            btn.setMaximumHeight(45)
            btn.setStyleSheet("font-size: 13px;")
            btn.clicked.connect(func)
            row = i // colunas
            col = i % colunas
            grid.addWidget(btn, row, col)
        grupo.setLayout(grid)
        return grupo

    # Funções de otimização (a serem implementadas)
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
