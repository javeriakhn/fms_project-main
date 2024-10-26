from flask import Flask, render_template, request, redirect, session
from connect import get_db_connection

app = Flask(__name__)
app.secret_key = "some_secret_key"

# Home route
@app.route('/')
def home():
    session['curr_date'] = session.get('curr_date', '2024-01-01')  # Simulated date
    return render_template('home.html', current_date=session['curr_date'])

# FMS dashboard route
@app.route('/fms')
def fms():
    return render_template('fms.html')  # Renders the Farm Management System Dashboard

# Mobs page
@app.route('/mobs')
def mobs():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT mobs.name AS mob_name, paddocks.name AS paddock_name
        FROM mobs
        LEFT JOIN paddocks ON mobs.paddock_id = paddocks.id
        ORDER BY mobs.name ASC
    """)
    mobs = cursor.fetchall()
    return render_template('mobs.html', mobs=mobs)

# Stock by mob page
@app.route('/mobs/stock')
def stock_by_mob():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT mobs.name AS mob_name, paddocks.name AS paddock_name, stock.id AS stock_id, stock.age_years
        FROM mobs
        LEFT JOIN stock ON mobs.id = stock.mob_id
        LEFT JOIN paddocks ON mobs.paddock_id = paddocks.id
        ORDER BY mobs.name ASC, stock.id ASC
    """)
    stock = cursor.fetchall()
    return render_template('stock.html', stock=stock)

# Paddocks page
@app.route('/paddocks')
def paddocks():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT paddocks.name, paddocks.area, paddocks.dm_per_ha, mobs.name AS mob_name
        FROM paddocks
        LEFT JOIN mobs ON paddocks.id = mobs.paddock_id
        ORDER BY paddocks.name ASC
    """)
    paddocks = cursor.fetchall()

    # Highlight paddocks based on DM/ha
    for paddock in paddocks:
        if paddock['dm_per_ha'] < 1500:
            paddock['highlight'] = 'red'
        elif paddock['dm_per_ha'] < 1800:
            paddock['highlight'] = 'yellow'
        else:
            paddock['highlight'] = ''

    return render_template('paddocks.html', paddocks=paddocks)

# Move mobs between paddocks
@app.route('/mobs/move', methods=['POST'])
def move_mobs():
    mob_id = request.form['mob_id']
    paddock_id = request.form['paddock_id']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE mobs SET paddock_id = %s WHERE id = %s", (paddock_id, mob_id))
    connection.commit()
    
    return redirect('/mobs')

# Add new paddock
@app.route('/paddocks/add', methods=['POST'])
def add_paddock():
    name = request.form['name']
    area = request.form['area']
    dm_per_ha = request.form['dm_per_ha']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO paddocks (name, area, dm_per_ha) VALUES (%s, %s, %s)", (name, area, dm_per_ha))
    connection.commit()
    
    return redirect('/paddocks')

# Start Flask app
if __name__ == '__main__':
    app.run(debug=True)
