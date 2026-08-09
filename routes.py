from flask import render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash


def register_routes(app):
    @app.route('/sms', methods=['GET'])
    def sms_route():
        sms, receiver = request.args.get('sms'), request.args.get('host')