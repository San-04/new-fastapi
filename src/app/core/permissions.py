"""Service layer for permissions logic."""

from src.app.database.db import Database


def has_permission(user_id: int, permission_name: str) -> bool:
    """Return True if user has the specified permission."""
    sql = f"""
        SELECT u.id
        FROM usuario u
        JOIN roles r ON u.role_id = r.id
        JOIN role_permissions rp ON r.id = rp.role_id
        JOIN permissions p ON rp.permission_id = p.id
        WHERE u.id = {user_id}
        AND p.name = "{permission_name}";
    """
    result = Database().mysql_execute(sql, db="tienda_plus")
    return bool(result)
