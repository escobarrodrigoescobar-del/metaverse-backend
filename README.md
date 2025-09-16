# 🎭 MangaVerse Backend API

Backend holográfico para a loja MangaVerse com produtos interdimensionais.

## 🚀 Recursos

- **10 produtos holográficos** temáticos de anime
- **5 categorias** especializadas
- **Sistema de busca** avançado
- **Filtros** por categoria e destaque
- **API REST** completa
- **CORS** configurado para qualquer origem

## 📡 Endpoints

### Produtos
- `GET /api/products` - Lista todos os produtos
- `GET /api/products?search=naruto` - Busca por termo
- `GET /api/products?category=figuras` - Filtra por categoria
- `GET /api/products?featured=true` - Apenas produtos em destaque
- `GET /api/products/{id}` - Produto específico

### Categorias
- `GET /api/categories` - Lista todas as categorias

### Busca
- `GET /api/search?q=holográfico` - Busca avançada

### Utilitários
- `GET /` - Informações da API
- `GET /health` - Status de saúde
- `POST /api/seed` - Popular dados (já carregados)

## 🎯 Produtos Inclusos

1. **Figura Holográfica Naruto** - R$ 599,99
2. **Mangá Holográfico One Piece** - R$ 189,99
3. **Cosplay Holográfico Sailor Moon** - R$ 399,99
4. **Figura Goku Ultra Instinct** - R$ 799,99
5. **Camiseta Attack on Titan** - R$ 149,99
6. **Poster Demon Slayer** - R$ 119,99
7. **Action Figure Luffy Gear 5** - R$ 699,99
8. **Katana Demon Slayer** - R$ 449,99
9. **Mangá Jujutsu Kaisen** - R$ 199,99
10. **Cosplay Nezuko** - R$ 359,99

## 🎨 Categorias

- **Figuras Holográficas** - Action figures com tecnologia holográfica
- **Mangás Interdimensionais** - Mangás com realidade aumentada
- **Cosplay Dimensional** - Cosplays com efeitos holográficos
- **Roupas Interativas** - Roupas com tecnologia holográfica
- **Acessórios Holográficos** - Acessórios com efeitos especiais

## 🔧 Deploy

Este backend está otimizado para deploy no Render, Heroku ou qualquer plataforma que suporte Flask.

### Variáveis de Ambiente
- `PORT` - Porta do servidor (padrão: 5000)

### Comandos
```bash
# Instalar dependências
pip install -r requirements.txt

# Executar localmente
python main.py

# Deploy (Procfile configurado)
gunicorn main:app
```

## ✨ Características Especiais

- **Produtos temáticos** para o nicho anime/manga
- **Descrições detalhadas** com tecnologia holográfica
- **Preços competitivos** com comparação
- **Sistema de avaliações** dos otakus
- **Controle de estoque** em tempo real
- **Tags** para busca avançada
- **Produtos exclusivos** e em destaque

