from setuptools import setup, find_packages

setup (
    name="mi_primer_paquete",
    version="1.0",
    description="Creación del primer paquete distribuible de Python",
    author="Matias Christello",
    author_email='m.christello@hotmail.com',
    
    packages=find_packages(),
    package_data={'mi_primer_paquete': ['clients_db.json']}
)