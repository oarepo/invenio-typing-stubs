from werkzeug.local import LocalProxy

current_service: LocalProxy[object]
current_resource: LocalProxy[object]
