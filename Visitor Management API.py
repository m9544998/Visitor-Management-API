from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database
conn = sqlite3.connect("visitors.db")
conn.execute("""
CREATE TABLE IF NOT EXISTS visitors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    visitor_name TEXT,
    purpose TEXT,
    person_to_meet TEXT,
    status TEXT
)
""")
conn.commit()
conn.close()


# POST - Add Visitor
@app.route("/visitors", methods=["POST"])
def add_visitor():
    data = request.get_json()

    conn = sqlite3.connect("visitors.db")
    conn.execute("""
        INSERT INTO visitors
        (visitor_name, purpose, person_to_meet, status)
        VALUES (?, ?, ?, ?)
    """, (
        data["visitor_name"],
        data["purpose"],
        data["person_to_meet"],
        data["status"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Visitor Added Successfully"}), 201


# GET - All Visitors
@app.route("/visitors", methods=["GET"])
def get_visitors():
    conn = sqlite3.connect("visitors.db")
    conn.row_factory = sqlite3.Row

    visitors = conn.execute(
        "SELECT * FROM visitors"
    ).fetchall()

    conn.close()

    return jsonify([dict(visitor) for visitor in visitors])


# GET - Visitor By ID
@app.route("/visitors/<int:id>", methods=["GET"])
def get_visitor(id):
    conn = sqlite3.connect("visitors.db")
    conn.row_factory = sqlite3.Row

    visitor = conn.execute(
        "SELECT * FROM visitors WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()

    if visitor is None:
        return jsonify({"message": "Visitor Not Found"}), 404

    return jsonify(dict(visitor))


# PUT - Update Visitor
@app.route("/visitors/<int:id>", methods=["PUT"])
def update_visitor(id):
    data = request.get_json()

    conn = sqlite3.connect("visitors.db")

    conn.execute("""
        UPDATE visitors
        SET visitor_name=?, purpose=?, person_to_meet=?, status=?
        WHERE id=?
    """, (
        data["visitor_name"],
        data["purpose"],
        data["person_to_meet"],
        data["status"],
        id
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Visitor Updated Successfully"})


# DELETE - Delete Visitor
@app.route("/visitors/<int:id>", methods=["DELETE"])
def delete_visitor(id):
    conn = sqlite3.connect("visitors.db")

    conn.execute(
        "DELETE FROM visitors WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Visitor Deleted Successfully"})


if __name__ == "__main__":
    app.run(debug=True)