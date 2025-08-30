import docker
import os
import tempfile

def ejecutar_codigo_seguro(codigo_python):
    """
    Ejecuta código Python de forma segura dentro de un contenedor Docker.
    """
    try:
        cliente = docker.from_env()
        
        # Crear un archivo temporal con el código
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(codigo_python)
            temp_file_path = f.name
        
        try:
            # Ejecutar en contenedor con Python ya instalado
            resultado = cliente.containers.run(
                image="python:3.9-slim",  # ¡Imagen con Python preinstalado!
                command=f"python /tmp/codigo.py",
                remove=True,
                stdout=True,
                stderr=True,
                mem_limit="100m",
                network_mode="none",
                volumes={
                    temp_file_path: {'bind': '/tmp/codigo.py', 'mode': 'ro'}
                }
            )
            
            salida = resultado.decode('utf-8') if resultado else ""
            return {"salida": salida, "error": None}
            
        finally:
            # Limpiar: eliminar el archivo temporal
            os.unlink(temp_file_path)
        
    except docker.errors.ContainerError as e:
        return {"salida": None, "error": e.stderr.decode('utf-8') if e.stderr else str(e)}
    except Exception as e:
        return {"salida": None, "error": f"Error: {str(e)}"}

# Código de prueba
if __name__ == "__main__":
    codigo_de_prueba = "print('¡Hola desde dentro de Docker!')\nprint(2 + 2)"
    resultado = ejecutar_codigo_seguro(codigo_de_prueba)
    print("Salida:", resultado["salida"])
    print("Error:", resultado["error"])
    codigo_de_prueba = "print('¡Hola desde dentro de Docker!')\nprint(2 + 2)"
    resultado = ejecutar_codigo_seguro(codigo_de_prueba)
    print("Salida:", resultado["salida"])
    print("Error:", resultado["error"])