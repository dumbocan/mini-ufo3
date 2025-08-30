import os
import json
import shutil
from pathlib import Path

class GestorProyectos:
    def __init__(self, carpeta_proyectos="proyectos"):
        self.carpeta_proyectos = Path(carpeta_proyectos)
        self.carpeta_proyectos.mkdir(exist_ok=True)
    
    def crear_proyecto(self, nombre_proyecto, tecnologia="python"):
        """Crea un nuevo proyecto con la tecnología especificada"""
        ruta_proyecto = self.carpeta_proyectos / nombre_proyecto
        ruta_proyecto.mkdir(exist_ok=True)
        
        # Metadata del proyecto
        metadata = {
            "nombre": nombre_proyecto,
            "tecnologia": tecnologia,
            "estado": "creado",
            "dependencias": []
        }
        
        # Crear archivo de metadata
        with open(ruta_proyecto / "metadata.json", "w") as f:
            json.dump(metadata, f, indent=2)
        
        # Copiar Dockerfile correspondiente
        dockerfile_template = f"templates/Dockerfile.{tecnologia}"
        if os.path.exists(dockerfile_template):
            shutil.copy(dockerfile_template, ruta_proyecto / "Dockerfile")
        
        return ruta_proyecto

    def listar_proyectos(self):
        """Lista todos los proyectos existentes"""
        proyectos = []
        for item in self.carpeta_proyectos.iterdir():
            if item.is_dir():
                metadata_file = item / "metadata.json"
                if metadata_file.exists():
                    with open(metadata_file, "r") as f:
                        metadata = json.load(f)
                        proyectos.append(metadata)
        return proyectos

    def get_proyecto(self, nombre_proyecto):
        """Obtiene la información de un proyecto específico"""
        ruta_proyecto = self.carpeta_proyectos / nombre_proyecto
        metadata_file = ruta_proyecto / "metadata.json"
        
        if metadata_file.exists():
            with open(metadata_file, "r") as f:
                return json.load(f)
        return None

# Prueba básica del gestor
if __name__ == "__main__":
    gestor = GestorProyectos()
    
    # Crear proyecto de prueba
    proyecto = gestor.crear_proyecto("mi-web-python", "python")
    print(f"Proyecto creado en: {proyecto}")
    
    # Listar proyectos
    proyectos = gestor.listar_proyectos()
    print("Proyectos existentes:", proyectos)