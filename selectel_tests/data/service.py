from enum import Enum


class Service(Enum):
    cloud_servers = 'Облачные серверы'
    dedicated_servers = 'Выделенные серверы'
    dedicated_server_config = 'Конфигуратор выделенных серверов'
    managed_kubernetes = 'Managed Kubernetes'
    container_registry = 'Container Registry'
    cloud_databases = 'Облачные базы данных'
    cdn = 'CDN'
    object_storage = 'Объектное хранилище'
    file_storage = 'Файловое хранилище'
    cloud_vmware = 'Облако на базе VMware'
    firewalls = 'Межсетевые экраны'
