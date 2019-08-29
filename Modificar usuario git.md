Listado 1: Configurando Git para la subida.

# Siempre puedes curiosear con lo existente en la configuración...
git config --global --list
 
# Primero, elimina el usuario actual (nombre y correo).
git config --global --unset-all user.name
git config --global --unset-all user.email
 
# Luego, vuelve a configurar las propiedades con tus datos.
git config --global --add user.name "El nuevo usuario"
git config --global --add user.email "nuevo@correo.com"
