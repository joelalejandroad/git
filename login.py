def login(username, password):
    # Usuario y contraseña predefinidos
    USER = "admin"
    PASS = "1234"
    if username == USER and password == PASS:
        return True
    else:
        return False

# Ejemplo de uso
if __name__ == "__main__":
    user = input("Usuario: ")
    pwd = input("Contraseña: ")
    if login(user, pwd):
        print("Login exitoso")
    else:
        print("Usuario o contraseña incorrectos")