from flask import Flask, jsonify, render_template, request
import sqlite3
import subprocess

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

# Serve the HTML Dashboard
@app.route('/')
def index():
    return render_template('generated_dashboard.html')

# API endpoint pre naštartovanie BMAD CrewAI
@app.route('/api/run-crew', methods=['POST'])
def run_crew():
    data = request.json
    idea = data.get('idea')
    if not idea:
        return jsonify({"error": "Nezadali ste žiaden nápad. Prosím vyplňte vyhľadávacie pole."}), 400
    
    try:
        # Spustenie scriptu na pozadí (neblokuje request)
        # Preposielame `idea` ako argument pre `sys.argv[1]`
        subprocess.Popen(
            ["python3", "bmad_all_agents.py", idea],
            cwd="/Users/macbookprosukromne/Documents/BMAD"
        )
        return jsonify({
            "message": "BMAD 21-Agent Tím bol úspešne prebudený a naštartovaný! Sledujte terminál pre živý prenos. Výsledok sa uloží do súboru THE_ULTIMATE_HIERARCHICAL_STARTUP.md"
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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
