from flask import Blueprint

app_views = Blueprint(__name__)

app.register_blueprint('app_views', url_refix=/api/v1)