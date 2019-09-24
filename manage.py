from app import create_app,db
from flask_script import Manager , Server
from app.models import User, Blog, Subscribe, Comments
from flask_migrate import Migrate,MigrateCommand

app=create_app()

manager =  Manager(app)
migrate = Migrate(app,db)
manager.add_command('server',Server(use_debugger=True))
manager.add_command('db',MigrateCommand)

@manager.shell
def add_shell_context():
    return dict(app = app,db = db,User = User, Blog=Blog, Subscribe=Subscribe,Comments=Comments )

if __name__=="__main__":
    manager.run()
