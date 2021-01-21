# Django & Vue application

An extremely simple crud application for managing user orders, that is completly based on rest API. Builded with Vue js, Django and Bootstrap.

## Setup

**Build a stack of applications to run a complete service**
```bash
docker-compose build
```

**Migrate**
```shell
docker-compose run django python3 manage.py migrate
```

**Make migrations**
```sh
docker-compose run django python3 manage.py makemigrations
```

**Run entire app**
```console
docker-compose up
```

There should now be two servers running:
- [http://127.0.0.1:5000](http://127.0.0.1:5000) is the Django app
- [http://127.0.0.1:8081](http://127.0.0.1:8081) is the React app

## Using `docker-compose run` to issue one-off commands

If you want to run a one-off command, like installing dependencies, you can use the `docker-compose run <service_name> <cmd>`.

For example, to install a Javascript dependency and save that information to `package.json` we could run:
```console
docker-compose run --rm frontend npm install --save axios
```

If you want to be on a shell for one of the Docker services, you can do something like:
`docker-compose run --rm frontend bash`

## License
