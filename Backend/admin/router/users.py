from fastapi import APIRouter,HTTPException,status,Depends
from pydantic import EmailStr

from admin.services.manager_users import ManagerUsersService
from admin.shemas.users_schemas import AdminUsersSchema
from shared.dependcices.dependcices import conn_dep,redis_dep,lang_dep
from shared.dependcices.securite_decode_token import decode_token
from shared.errors.db_errors import DbError
from shared.errors.users_errors import UsersError

router = APIRouter(prefix="/api/v1/admin/manager-users",tags=["Admin-Users"])
@router.get("/")
async def get_all_users(connection :conn_dep,redis:redis_dep,lang:lang_dep):
    try :
        services = ManagerUsersService(connection, redis, lang)
        result = await  services.get_all_users()
        return result
    except DbError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail= str(e))

@router.delete("/")
async def delete_users(connection :conn_dep,redis:redis_dep,lang:lang_dep,admin_users_schema:AdminUsersSchema,payload = Depends(decode_token)):
    try :
        services = ManagerUsersService(connection, redis, lang)
        result = await  services.delete_user(email=admin_users_schema.email,payload=payload)
        return result
    except UsersError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= str(e))
    except DbError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail= str(e))

@router.get("/length-table")
async def length_table(connection : conn_dep,redis:redis_dep,lang:lang_dep):
    try:
        services = ManagerUsersService(connectin=connection, redis=redis, lang=lang)
        result =await services.length_table()
        return result
    except DbError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))