# Django & Vue application

An extremely simple crud application for managing user orders, that is completly based on rest API. Builded with Vue js, Django and Bootstrap.

## Setup

**Build a stack of applications to run a complete service**
```console
docker-compose build
```

**Migrate**
```console
docker-compose run django python3 manage.py migrate
```

**Make migrations**
```console
docker-compose run django python3 manage.py makemigrations
```

**Run entire app**
```console
docker-compose up
```

There should now be two servers running:
- [http://127.0.0.1:5000](http://127.0.0.1:5000) is the Django app
- [http://127.0.0.1:8081](http://127.0.0.1:8081) is the React app

## Using 'docker-compose run' to issue one-off commands

If you want to run a one-off command, like installing dependencies, you can use the:
```console
docker-compose run <service_name> <cmd>
```

For example, to install a Javascript dependency and save that information to `package.json` we could run:
```console
docker-compose run --rm frontend npm install --save axios
```

If you want to be on a shell for one of the Docker services, you can do something like:
```console
docker-compose run --rm frontend bash
```

## API Documentation

For swagger documentation, go to `/redoc/` or `/doc/` endpoint.

## License
Copyright 2020 Grzegorz Piechnik

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
