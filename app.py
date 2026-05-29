from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 模拟的公共机场数据
LOUNGES_DATA = [
    {"id": "syd", "name": "Sydney Airport Lounge", "code": "Sydney Airport (SYD)", "price": 45.00, "city": "Sydney"},
    {"id": "mel", "name": "Melbourne Premium Lounge", "code": "Melbourne Airport (MEL)", "price": 40.00, "city": "Melbourne"},
    {"id": "bne", "name": "Brisbane Airport Lounge", "code": "Brisbane Airport (BNE)", "price": 38.00, "city": "Brisbane"},
    {"id": "per", "name": "Perth Airport Lounge", "code": "Perth Airport (PER)", "price": 45.00, "city": "Perth"}
]

# 1. 首页 (Lounge Search)
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html', lounges=LOUNGES_DATA, active_page='home')

# 2. 预订详情页 (Book Your Lounge)
@app.route('/book/<lounge_id>')
def book_lounge(lounge_id):
    lounge = next((l for l in LOUNGES_DATA if l["id"] == lounge_id), LOUNGES_DATA[0])
    return render_template('book.html', lounge=lounge, active_page='home')

# 3. 支付页面 (Payment) - 终极修复
@app.route('/payment', methods=['POST', 'GET'])
def payment():
    # 模拟数据，确保页面能渲染出 Sydney Airport Lounge
    p = {
        "name": request.args.get('name', 'Sydney Airport Lounge'), 
        "price": "$45.00"
    }
    return render_template('payment.html', p=p)

# 4. 我的预订
@app.route('/bookings')
def bookings():
    my_bookings = [
        {"name": "Sydney Airport Lounge", "date": "May 20, 2026", "time": "10:00 AM", "guests": "1 Guest", "price": "$45.00", "status": "Confirmed"},
        {"name": "Melbourne Premium Lounge", "date": "Jun 5, 2026", "time": "2:00 PM", "guests": "2 Guests", "price": "$80.00", "status": "Confirmed"},
        {"name": "Brisbane Airport Lounge", "date": "Apr 10, 2026", "time": "9:00 AM", "guests": "1 Guest", "price": "$38.00", "status": "Completed"}
    ]
    return render_template('bookings.html', bookings=my_bookings, active_page='bookings')

# 5. 取消预订页面
@app.route('/cancel-booking')
def cancel_booking():
    b = {
        "name": request.args.get('name', 'N/A'),
        "date": request.args.get('date', 'N/A'),
        "time": request.args.get('time', 'N/A'),
        "guests": request.args.get('guests', 'N/A'),
        "price": request.args.get('price', '$0.00')
    }
    return render_template('cancel_booking.html', b=b, active_page='bookings')

# 6. 其他认证/页面
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('bookings'))
    return render_template('login.html', active_page='profile')

@app.route('/register')
def register():
    return render_template('register.html', active_page='profile')

@app.route('/membership')
def membership():
    return render_template('membership.html', active_page='membership')

if __name__ == '__main__':
    app.run(debug=True, port=5000)