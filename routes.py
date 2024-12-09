

from flask import request, jsonify
from models import books, members

def register_routes(app):
    # BOOKS routes
    @app.route('/books', methods=['GET'])
    def get_books():
        return jsonify(books), 200

    @app.route('/books', methods=['POST'])
    def add_book():
        data = request.json
        book = {
            "id": len(books) + 1,
            "title": data["title"],
            "author": data["author"]
        }
        books.append(book)
        return jsonify({"message": "Book added successfully!", "book": book}), 201

    @app.route('/books/<int:book_id>', methods=['PUT'])
    def update_book(book_id):
        data = request.json
        book = next((b for b in books if b["id"] == book_id), None)
        if not book:
            return jsonify({"error": "Book not found"}), 404
        book.update(data)
        return jsonify({"message": "Book updated successfully!", "book": book}), 200

    @app.route('/books/<int:book_id>', methods=['DELETE'])
    def delete_book(book_id):
        global books
        books = [b for b in books if b["id"] != book_id]
        return jsonify({"message": "Book deleted successfully!"}), 200

    # MEMBERS routes
    @app.route('/members', methods=['GET'])
    def get_members():
        return jsonify(members), 200

    @app.route('/members', methods=['POST'])
    def add_member():
        data = request.json
        member = {
            "id": len(members) + 1,
            "name": data["name"],
            "email": data["email"]
        }
        members.append(member)
        return jsonify({"message": "Member added successfully!", "member": member}), 201

    @app.route('/members/<int:member_id>', methods=['PUT'])
    def update_member(member_id):
        data = request.json
        member = next((m for m in members if m["id"] == member_id), None)
        if not member:
            return jsonify({"error": "Member not found"}), 404
        member.update(data)
        return jsonify({"message": "Member updated successfully!", "member": member}), 200

    @app.route('/members/<int:member_id>', methods=['DELETE'])
    def delete_member(member_id):
        global members
        members = [m for m in members if m["id"] != member_id]
        return jsonify({"message": "Member deleted successfully!"}), 200
