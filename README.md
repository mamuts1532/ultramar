# Ultramar

Proyecto basico en Django  con 2 aplicaciones. Booking y Vehicle.

En la app Booking se realizo CRUD desde el modelo en base de datos, para realizar una actualización se debe hacer sobre el id del booking como ejemplo: ```http://127.0.0.1:8000/1/update/```, donde 1 es el id del objeto en la base de datos, el id debe existir sino, no sera encontrado. Para borrar un objeto de la base de datos se debe ir a una url como ejemplo: ```http://127.0.0.1:8000/1/delete/```, luego se debe confirmar, 1 es el id del objeto en la base de datos, el id debe existir sino, no sera encontrado.
