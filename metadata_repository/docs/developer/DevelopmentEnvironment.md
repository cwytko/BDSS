# Development Environment

To set up a development environment for the metadata repository, follow these steps:

1. [Install Python 3.4+](http://docs.python-guide.org/en/latest/starting/installation/).

2. Create a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

   ```Shell
   cd /path/to/bdss/metadata_repository
   virtualenv -p /path/to/python3 venv
   ```

3. Activate the virtualenv.

   ```Shell
   source venv/bin/activate
   ```

4. Install requirements.

   ```Shell
   pip install -r requirements.txt
   ```

5. Configure the application.

   ```Shell
   cp app/app_config.example.yml app/app_config.yml
   ```

   Edit `app/app_config.yml` and replace the `database_url` value with the URL of your database.
   If you use a path to an SQLite database, it will be automatically created if it doesn't exist.
   For other database types, you may have to install an additional driver. See the
   [SQLAlchemy documentation](http://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls)
   for more information.

6. Create the database schema.

   This project uses [Alembic](https://alembic.readthedocs.org/en/latest/) for database migrations.
   To migrate your database to the latest version, run:

   ```Shell
   alembic upgrade head
   ```

7. Generate a [secret key for Flask sessions](http://flask.pocoo.org/docs/0.10/quickstart/#sessions).

   This will generate a new secret key using the method described in the Flask documentation and store
   it in your `app/app_config.yml` file.

   ```Shell
   ./scripts/generate_flask_key
   ```

8. Start the development server.

   ```Shell
   ./scripts/serve
   ```

   By default, this server will only be accessible at `localhost`. To make it publicly accessible, run
   the script with the `--public` option.

# Vagrant

Alternatively, you can launch an instance of the metadata repository in a virtual machine. The VM is
configured to use [PostgreSQL](http://www.postgresql.org/) for the database and
[Apache](https://httpd.apache.org/) for the web server.

**Note**: The VM setup requires your `database_url` in `app/app_config.yml` to be set to
`postgresql+psycopg2://bdss:bdss@localhost/bdss`. The VM provision script will set this value if
`app/app_config.yml` does not exist, but it will not overwrite an existing file so you may have to
change the value manually.

1. Install VirtualBox and Vagrant

   * [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
   * [Vagrant](http://docs.vagrantup.com/v2/installation/index.html)

2. Launch VM

   ```Shell
   cd /path/to/bdss/metadata_repository
   vagrant up
   ```

3. Open [http://localhost:8000](http://localhost:8000) in a web browser.

   Port 8000 is forwarded to the VM's port 80.