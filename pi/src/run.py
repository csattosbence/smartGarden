from main import create_app, socketio

app = create_app()
with app.app_context():
    socketio.run(app)
