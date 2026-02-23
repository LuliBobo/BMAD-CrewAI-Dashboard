from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('sales_dashboard.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            total_sales REAL,
            new_leads INTEGER,
            conversion_rate REAL,
            active_users INTEGER
        )
    ''')
    
    # Pridáme vzorové dáta, ak je tabuľka prázdna
    cursor.execute('SELECT COUNT(*) FROM metrics')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO metrics (total_sales, new_leads, conversion_rate, active_users)
            VALUES (12450.0, 342, 12.4, 1200)
        ''')
        
    conn.commit()
    conn.close()

# API endpoint to get metrics
@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    try:
        conn = sqlite3.connect('sales_dashboard.db')
        cursor = conn.cursor()
        cursor.execute('SELECT total_sales, new_leads, conversion_rate, active_users FROM metrics ORDER BY id DESC LIMIT 1')
        row = cursor.fetchone()
        conn.close()

        if row:
            metrics = {
                "total_sales": row[0],
                "new_leads": row[1],
                "conversion_rate": row[2],
                "active_users": row[3]
            }
            return jsonify(metrics), 200
        else:
            return jsonify({"error": "No metrics found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
