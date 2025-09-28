# ESP Simulator Server

Este projeto é um simulador de servidor ESP que simula dados RSSI (Received Signal Strength Indicator) para localização de motos em um pátio usando Flask.

## Funcionalidades

- Simula 5 ESPs posicionados em um pátio (4 nos cantos e 1 no centro)
- Gera dados RSSI baseados na distância simulada
- API REST para simulação e obtenção de coordenadas dos ESPs

## Pré-requisitos

- Python 3.6 ou superior
- pip (gerenciador de pacotes do Python)

## Instalação das Dependências

1. **Clone ou baixe o projeto** (se ainda não tiver feito)

3. **Instale as dependências necessárias:**
   ```bash
   pip install flask
   ```

   Ou, alternativamente, você pode criar um arquivo `requirements.txt` e instalar usando:
   ```bash
   pip install -r requirements.txt
   ```

## Como Iniciar o Projeto

1. **Execute o servidor:**
   ```bash
   python esp_simulator_server.py
   ```

2. **O servidor será iniciado em:**
   - Host: `0.0.0.0` (todas as interfaces de rede)
   - Porta: `5001`
   - URL local: `http://localhost:5001`

3. **Você verá uma mensagem similar a:**
   ```
   * Running on all addresses (0.0.0.0)
   * Running on http://127.0.0.1:5001
   * Running on http://[seu-ip]:5001
   ```

## Endpoints da API

### POST /simulate
Simula a localização de uma moto e retorna dados RSSI.

**Exemplo de requisição:**
```json
{
    "id": "moto123"
}
```

**Exemplo de resposta:**
```json
{
    "motoId": "moto123",
    "rssiPorEsp": {
        "esp1": -85.23,
        "esp2": -92.45,
        "esp3": -78.12,
        "esp4": -89.67,
        "esp_central": -82.34
    },
    "localizacaoSorteada": {
        "x": 0.7234,
        "y": 0.4567
    }
}
```

### GET /patio-coords
Retorna as coordenadas dos ESPs no pátio.

**Exemplo de resposta:**
```json
{
    "coordenadas": [
        {"nome": "esp1", "x": 0.0, "y": 0.0},
        {"nome": "esp2", "x": 0.0, "y": 1.0},
        {"nome": "esp3", "x": 1.0, "y": 0.0},
        {"nome": "esp4", "x": 1.0, "y": 1.0},
        {"nome": "esp_central", "x": 0.5, "y": 0.5}
    ]
}
```

## Testando a API

Você pode testar a API usando:

### Com curl:
```bash
# Testar simulação
curl -X POST http://localhost:5001/simulate -H "Content-Type: application/json" -d "{\"id\": \"moto123\"}"

# Obter coordenadas dos ESPs
curl http://localhost:5001/patio-coords
```

### Com um cliente HTTP como Postman ou Insomnia
- Configure requisições para os endpoints mencionados acima

## Estrutura do Projeto

```
python-teste/
├── esp_simulator_server.py    # Arquivo principal do servidor
└── README.md                  # Este arquivo
```

## Como Funciona

1. **ESPs Simulados:** O sistema simula 5 ESPs posicionados nos cantos e centro de um pátio quadrado
2. **Simulação RSSI:** Calcula valores RSSI baseados na distância euclidiana entre a posição sorteada da moto e cada ESP
3. **Ruído:** Adiciona um ruído aleatório de ±2 dBm para simular condições reais
4. **Localização Aleatória:** Para cada requisição, sorteia uma nova posição dentro dos limites do pátio

## Parando o Servidor

Para parar o servidor, pressione `Ctrl + C` no terminal onde ele está rodando.
