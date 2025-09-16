from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app, origins="*")

# Produtos MangaVerse para o nicho anime
MANGAVERSE_PRODUCTS = [
    {
        "id": 1,
        "name": "Figura Holográfica Naruto Uzumaki - Edição Dimensional",
        "short_description": "Figura premium com projeção holográfica e efeitos de chakra em movimento",
        "description": "Uma obra-prima da tecnologia holográfica aplicada ao universo Naruto. Esta figura exclusiva apresenta projeções de chakra em tempo real, mudança de expressões faciais e efeitos sonoros autênticos da série.",
        "price": 599.99,
        "compare_price": 899.99,
        "featured_image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&h=300&fit=crop",
        "category": "figuras",
        "tags": ["naruto", "holográfico", "exclusivo", "chakra"],
        "rating_average": 4.9,
        "rating_count": 247,
        "in_stock": True,
        "stock_count": 3,
        "is_exclusive": True,
        "is_featured": True
    },
    {
        "id": 2,
        "name": "Mangá Holográfico One Piece - Volume Interdimensional",
        "short_description": "Edição especial com páginas holográficas e realidade aumentada integrada",
        "description": "Primeira edição mundial de mangá com tecnologia holográfica. As páginas ganham vida com animações 3D, efeitos sonoros e experiência de realidade aumentada através do app MangaVerse.",
        "price": 189.99,
        "compare_price": 299.99,
        "featured_image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&h=300&fit=crop",
        "category": "mangas",
        "tags": ["one piece", "holográfico", "realidade aumentada", "exclusivo"],
        "rating_average": 4.8,
        "rating_count": 156,
        "in_stock": True,
        "stock_count": 7,
        "is_exclusive": False,
        "is_featured": True
    },
    {
        "id": 3,
        "name": "Cosplay Holográfico Sailor Moon - Conjunto Dimensional",
        "short_description": "Cosplay com fibras holográficas e efeitos luminosos integrados",
        "description": "Revolucionário cosplay com fibras ópticas integradas que criam efeitos holográficos reais. Inclui tiara com cristais luminosos, varinha com projeções mágicas e saia com efeitos de movimento.",
        "price": 399.99,
        "compare_price": 599.99,
        "featured_image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&h=300&fit=crop",
        "category": "cosplay",
        "tags": ["sailor moon", "cosplay", "holográfico", "luminoso"],
        "rating_average": 4.7,
        "rating_count": 89,
        "in_stock": True,
        "stock_count": 5,
        "is_exclusive": False,
        "is_featured": True
    },
    {
        "id": 4,
        "name": "Figura Holográfica Goku Ultra Instinct - Edição Limitada",
        "short_description": "Figura com aura holográfica e efeitos de energia em movimento perpétuo",
        "description": "Edição limitada numerada com apenas 100 unidades mundiais. Apresenta aura Ultra Instinct em holografia real, cabelos que mudam de cor e base com efeitos de energia ki em movimento contínuo.",
        "price": 799.99,
        "compare_price": 1199.99,
        "featured_image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&h=300&fit=crop",
        "category": "figuras",
        "tags": ["dragon ball", "goku", "ultra instinct", "limitada", "holográfico"],
        "rating_average": 4.9,
        "rating_count": 312,
        "in_stock": True,
        "stock_count": 2,
        "is_exclusive": True,
        "is_featured": True
    },
    {
        "id": 5,
        "name": "Camiseta Holográfica Attack on Titan - Design Dimensional",
        "short_description": "Camiseta com estampa holográfica que muda com o movimento e temperatura",
        "description": "Tecnologia têxtil revolucionária que muda a estampa baseada no movimento corporal e temperatura ambiente. Mostra diferentes cenas épicas de Attack on Titan conforme você se move.",
        "price": 149.99,
        "compare_price": 229.99,
        "featured_image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&h=300&fit=crop",
        "category": "roupas",
        "tags": ["attack on titan", "camiseta", "holográfico", "interativo"],
        "rating_average": 4.6,
        "rating_count": 134,
        "in_stock": True,
        "stock_count": 12,
        "is_exclusive": False,
        "is_featured": False
    },
    {
        "id": 6,
        "name": "Poster Holográfico Demon Slayer - Coleção Interdimensional",
        "short_description": "Set com 5 posters holográficos com efeitos de profundidade e movimento",
        "description": "Coleção exclusiva de 5 posters com tecnologia holográfica avançada. Cada poster apresenta cenas em movimento, efeitos de respiração dos personagens e mudança de cenários dia/noite.",
        "price": 119.99,
        "compare_price": 189.99,
        "featured_image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&h=300&fit=crop",
        "category": "acessorios",
        "tags": ["demon slayer", "poster", "holográfico", "coleção"],
        "rating_average": 4.5,
        "rating_count": 67,
        "in_stock": True,
        "stock_count": 15,
        "is_exclusive": False,
        "is_featured": False
    },
    {
        "id": 7,
        "name": "Action Figure Holográfica Luffy Gear 5 - Edição Especial",
        "short_description": "Figure com transformações holográficas e efeitos de borracha em tempo real",
        "description": "Primeira action figure do mundo com transformações holográficas do Gear 5. Apresenta mudanças de forma em tempo real, efeitos de borracha e risadas características do Luffy.",
        "price": 699.99,
        "compare_price": 999.99,
        "featured_image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&h=300&fit=crop",
        "category": "figuras",
        "tags": ["one piece", "luffy", "gear 5", "holográfico", "transformação"],
        "rating_average": 4.8,
        "rating_count": 198,
        "in_stock": True,
        "stock_count": 4,
        "is_exclusive": True,
        "is_featured": True
    },
    {
        "id": 8,
        "name": "Katana Holográfica Demon Slayer - Réplica Dimensional",
        "short_description": "Réplica com lâmina holográfica e efeitos de respiração dos pilares",
        "description": "Réplica oficial com tecnologia holográfica que simula as técnicas de respiração. A lâmina muda de cor e padrão conforme diferentes estilos de respiração são ativados via sensor de movimento.",
        "price": 449.99,
        "compare_price": 699.99,
        "featured_image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&h=300&fit=crop",
        "category": "acessorios",
        "tags": ["demon slayer", "katana", "holográfico", "respiração"],
        "rating_average": 4.7,
        "rating_count": 123,
        "in_stock": True,
        "stock_count": 6,
        "is_exclusive": False,
        "is_featured": True
    },
    {
        "id": 9,
        "name": "Mangá Holográfico Jujutsu Kaisen - Volume Maldito",
        "short_description": "Edição com técnicas amaldiçoadas em holografia e efeitos sonoros",
        "description": "Volume especial com as técnicas amaldiçoadas em holografia real. Cada jutsu ganha vida nas páginas com efeitos visuais e sonoros autênticos da animação.",
        "price": 199.99,
        "compare_price": 319.99,
        "featured_image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&h=300&fit=crop",
        "category": "mangas",
        "tags": ["jujutsu kaisen", "holográfico", "técnicas", "maldições"],
        "rating_average": 4.6,
        "rating_count": 87,
        "in_stock": True,
        "stock_count": 9,
        "is_exclusive": False,
        "is_featured": False
    },
    {
        "id": 10,
        "name": "Cosplay Holográfico Nezuko - Conjunto Completo",
        "short_description": "Cosplay com efeitos de transformação demônio e bambú holográfico",
        "description": "Cosplay completo com tecnologia de transformação holográfica. O bambú apresenta efeitos luminosos e o kimono muda de padrão simulando a transformação demônio de Nezuko.",
        "price": 359.99,
        "compare_price": 549.99,
        "featured_image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&h=300&fit=crop",
        "category": "cosplay",
        "tags": ["demon slayer", "nezuko", "cosplay", "transformação"],
        "rating_average": 4.8,
        "rating_count": 156,
        "in_stock": True,
        "stock_count": 8,
        "is_exclusive": False,
        "is_featured": True
    }
]

# Categorias MangaVerse
CATEGORIES = [
    {"id": "figuras", "name": "Figuras Holográficas", "description": "Action figures com tecnologia holográfica"},
    {"id": "mangas", "name": "Mangás Interdimensionais", "description": "Mangás com realidade aumentada e holografia"},
    {"id": "cosplay", "name": "Cosplay Dimensional", "description": "Cosplays com efeitos holográficos integrados"},
    {"id": "roupas", "name": "Roupas Interativas", "description": "Roupas com tecnologia holográfica"},
    {"id": "acessorios", "name": "Acessórios Holográficos", "description": "Acessórios com efeitos especiais"}
]

@app.route('/')
def home():
    return jsonify({
        "message": "🎭 MangaVerse API - Sua Dimensão Otaku",
        "version": "2.0.0",
        "status": "online",
        "features": [
            "Produtos holográficos",
            "Tecnologia interdimensional", 
            "Experiência otaku premium"
        ]
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "MangaVerse API"})

@app.route('/api/products')
def get_products():
    try:
        # Filtros
        search = request.args.get('search', '').lower()
        category = request.args.get('category', 'all')
        featured_only = request.args.get('featured', 'false').lower() == 'true'
        
        # Filtrar produtos
        filtered_products = MANGAVERSE_PRODUCTS.copy()
        
        if search:
            filtered_products = [
                p for p in filtered_products 
                if search in p['name'].lower() or 
                   search in p['short_description'].lower() or
                   any(search in tag.lower() for tag in p['tags'])
            ]
        
        if category != 'all':
            filtered_products = [p for p in filtered_products if p['category'] == category]
            
        if featured_only:
            filtered_products = [p for p in filtered_products if p['is_featured']]
        
        return jsonify({
            "products": filtered_products,
            "total": len(filtered_products),
            "categories": CATEGORIES,
            "message": "Produtos holográficos carregados com sucesso"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/products/<int:product_id>')
def get_product(product_id):
    try:
        product = next((p for p in MANGAVERSE_PRODUCTS if p['id'] == product_id), None)
        if not product:
            return jsonify({"error": "Produto não encontrado na dimensão"}), 404
            
        return jsonify({
            "product": product,
            "message": "Produto holográfico encontrado"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/categories')
def get_categories():
    try:
        return jsonify({
            "categories": CATEGORIES,
            "message": "Categorias interdimensionais carregadas"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/featured')
def get_featured():
    try:
        featured_products = [p for p in MANGAVERSE_PRODUCTS if p['is_featured']]
        
        return jsonify({
            "products": featured_products,
            "total": len(featured_products),
            "message": "Produtos em destaque na dimensão"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/search')
def search_products():
    try:
        query = request.args.get('q', '').lower()
        if not query:
            return jsonify({"products": [], "total": 0, "message": "Query vazia"})
        
        results = [
            p for p in MANGAVERSE_PRODUCTS 
            if query in p['name'].lower() or 
               query in p['short_description'].lower() or
               any(query in tag.lower() for tag in p['tags'])
        ]
        
        return jsonify({
            "products": results,
            "total": len(results),
            "query": query,
            "message": f"Busca interdimensional por '{query}' concluída"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para popular dados (útil para testes)
@app.route('/api/seed', methods=['POST'])
def seed_data():
    try:
        return jsonify({
            "message": "Dados MangaVerse já estão carregados na dimensão",
            "products_count": len(MANGAVERSE_PRODUCTS),
            "categories_count": len(CATEGORIES)
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

