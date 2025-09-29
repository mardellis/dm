from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    """Ana sayfa"""
    return render_template("index.html")

@app.route("/template/product")
def product_template():
    """3D Ürün Showcase template"""
    return render_template("product.html")

@app.route("/template/portfolio")
def portfolio_template():
    """Immersive Portfolio template"""
    return render_template("portfolio.html")

@app.route("/template/showroom")
def showroom_template():
    """Sanal Showroom template"""
    return render_template("showroom.html")

@app.route("/template/restaurant")
def restaurant_template():
    """Restoran 3D Menü template"""
    return render_template("restaurant.html")

@app.route("/template/dashboard")
def dashboard_template():
    """Kurumsal Dashboard template"""
    return render_template("dashboard.html")

@app.route("/api/contact", methods=["POST"])
def contact():
    """İletişim formu API endpoint"""
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")
        
        # Burada veritabanına kayıt yapabilir veya email gönderebilirsiniz
        print(f"İletişim Formu - Ad: {name}, Email: {email}, Mesaj: {message}")
        
        return jsonify({
            "status": "success",
            "message": "Mesajınız başarıyla gönderildi!"
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/api/cart/add", methods=["POST"])
def add_to_cart():
    """Sepete ürün ekleme API"""
    try:
        data = request.get_json()
        product_name = data.get("product_name")
        price = data.get("price")
        
        # Burada sepet işlemleri yapılabilir (session, database, etc.)
        print(f"Sepete Eklendi - Ürün: {product_name}, Fiyat: {price}")
        
        return jsonify({
            "status": "success",
            "message": f"{product_name} sepete eklendi!"
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)