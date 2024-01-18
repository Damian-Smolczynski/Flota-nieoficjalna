# TODO 3 - Gdzie umiejscawiać alembic - potrzebuje przecież pipenva - czy traktujemy go jako osobny serwis?
# TODO 4 - Czy jest jakaś zauważalna różnica pomiędzy
"""
The core difference between python:3.11 and python:3.11-slim Docker images lies in
 their sizes and the number of packages pre-installed.
python:3.11 Image: This is the standard Python 3.11 Docker image,
 it's larger in size because they include a decent number of common
  debian packages. This can be quite handy because it saves you from
   having to install these common tools when building your image.
python:3.11-slim Image: This is a minimally equipped Python 3.11
 Docker image which occupies less space compared to the standard image.
  It doesn't include many common packages which means that your image
  is going to be lightweight.
The choice depends on your use case. If you need a smaller image
 and you're sure that your application doesn't need any extra packages
 included in the non-slim version, you're better off using the slim version.
  Otherwise,
 if you're not sure what dependencies your application might need or
 if a few extra hundred MBs don't matter to you, you should use the
 non-slim version.
"""