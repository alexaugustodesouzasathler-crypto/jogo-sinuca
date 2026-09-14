## 🎱 Jogo de Sinuca (Bilhar)

Um jogo de sinuca desenvolvido em Python com Pygame, simulando a física de bilhar real.

### 📋 Funcionalidades

- **Simulação de Física Realista**: Atrito, colisões elásticas e movimento das bolas
- **Bola Branca Controlável**: Clique e arraste para definir força e direção
- **15 Bolas Numeradas**: Dispostas em triângulo no início do jogo
- **Paredes e Caçapas**: Mesa realista com 6 caçapas
- **Sistema de Rebote**: Bolas ricocheteiam nas paredes com amortecimento

### 🚀 Como Executar

1. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

2. **Execute o jogo**:
```bash
python main.py
```

### 🎮 Como Jogar

1. A **bola branca** começa no lado esquerdo da mesa
2. Mova o mouse sobre a bola branca para ver a linha de mira
3. Clique e arraste para definir a força do tiro
4. Solte o clique para disparar
5. As bolas colidem e deslizam pela mesa com atrito realista
6. Clique novamente quando todas as bolas pararem para fazer outro tiro

### 📁 Estrutura do Projeto

- **main.py**: Loop principal do jogo
- **bola.py**: Classe que define as bolas
- **mesa.py**: Classe que define a mesa e suas paredes
- **fisica.py**: Cálculos de física (colisões, atrito, gravidade)

### 🔧 Tecnologias

- **Python 3.x**
- **Pygame**: Biblioteca para desenvolvimento de jogos

### 📝 Notas

- O jogo ainda não implementa sistema de pontuação
- Futuros aprimoramentos podem incluir: som, efeitos especiais, e lógica de turnos

### 👨‍💻 Autor

Desenvolvido por alexaugustodesouzasathler-crypto

---

Divirta-se jogando! 🎉
