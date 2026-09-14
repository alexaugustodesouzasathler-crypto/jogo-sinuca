import math

class Fisica:
    ATRITO = 0.98  # Coeficiente de atrito
    GRAVIDADE = 0.0  # Sem gravidade (mesa plana)
    ELASTICIDADE = 0.95  # Elasticidade das colisões
    
    @staticmethod
    def aplicar_atrito(bola):
        """Aplica atrito à bola, diminuindo sua velocidade"""
        bola.vx *= Fisica.ATRITO
        bola.vy *= Fisica.ATRITO
        
        # Parar completamente se a velocidade for muito pequena
        if abs(bola.vx) < 0.1:
            bola.vx = 0
        if abs(bola.vy) < 0.1:
            bola.vy = 0
    
    @staticmethod
    def aplicar_gravidade(bola):
        """Aplica gravidade à bola"""
        bola.vy += Fisica.GRAVIDADE
    
    @staticmethod
    def detectar_colisao_bolas(bola1, bola2):
        """Detecta colisão entre duas bolas e aplica física"""
        # Calcular distância entre bolas
        dx = bola2.x - bola1.x
        dy = bola2.y - bola1.y
        distancia = math.sqrt(dx**2 + dy**2)
        
        # Verificar colisão
        distancia_minima = bola1.raio + bola2.raio
        if distancia < distancia_minima:
            # Normalizar vetor de colisão
            nx = dx / distancia
            ny = dy / distancia
            
            # Separar bolas para evitar sobreposição
            sobreposicao = distancia_minima - distancia
            bola1.x -= nx * sobreposicao / 2
            bola1.y -= ny * sobreposicao / 2
            bola2.x += nx * sobreposicao / 2
            bola2.y += ny * sobreposicao / 2
            
            # Calcular velocidades relativas
            dvx = bola2.vx - bola1.vx
            dvy = bola2.vy - bola1.vy
            
            # Calcular velocidade relativa ao longo do vetor de colisão
            velocidade_relativa = dvx * nx + dvy * ny
            
            # Não processar se as bolas estão se afastando
            if velocidade_relativa >= 0:
                return
            
            # Calcular impulso (considerando massas iguais)
            impulso = -2 * velocidade_relativa / 2
            impulso *= Fisica.ELASTICIDADE
            
            # Aplicar impulso
            bola1.vx -= impulso * nx
            bola1.vy -= impulso * ny
            bola2.vx += impulso * nx
            bola2.vy += impulso * ny
