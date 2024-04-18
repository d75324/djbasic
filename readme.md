Ejemplo Básico de Django para hacer pruebas

*** VER ***

Error en:
http://127.0.0.1:1716/todos/
y en:
http://127.0.0.1:1716/dos/

** ERROR **
OperationalError at /dos/
table datos_profesionales has no column named usuario_id

La columna usuario_id la crea Django cuando detecta una ForeginKey, -para guardar el dato que llega de la otra tabla?

El Profesional debe ser un Usuario. Por eso, cuando voy a registrar un nuevo Profesional, necesito que el nombre lo tome del modelo Profesionales - done!

