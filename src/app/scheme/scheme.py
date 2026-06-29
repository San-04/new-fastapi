from typing import List
from pydantic import BaseModel, EmailStr

class CreateUserSchema(BaseModel):
    """
        Schema for creating a new user.
    """
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    age: int
    mobile: str
    dateBirth: str
    role_id: int

class UpdateUserSchema(BaseModel):
    """
        Schema for update user.
    """
    id: int
    firstName: str
    lastName: str
    email: EmailStr
    age: int
    mobile: str
    dateBirth: str
    status: int
    role_id: int

class DeleteUserSchema(BaseModel):
    """
        Schema for delete user.
    """
    id: int

class CreateRoleSchema(BaseModel):
    """
        Schema for creating a new role.
    """
    name: str
    descripcion: str

class UpdateRoleSchema(BaseModel):
    """
        Schema for update role.
    """
    id: int
    name: str
    descripcion: str

class DeleteRoleSchema(BaseModel):
    """
        Schema for delete role.
    """
    id: int

class CreatePermissionSchema(BaseModel):
    """
        Schema for creating a new permission.
    """
    name: str
    descripcion: str
    role_ids: List[int]

class UpdatePermissionSchema(BaseModel):
    """
        Schema for update permission.
    """
    id: int
    name: str
    descripcion: str
    role_ids: List[int]

class DeletePermissionSchema(BaseModel):
    """
        Schema for delete permission.
    """
    id: int