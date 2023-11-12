from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()

"""
base_model.py
engine/
    __init__.py
    file_storage.py
"""
