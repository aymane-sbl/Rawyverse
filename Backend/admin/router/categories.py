from fastapi import APIRouter , Depends, HTTPException,status
from redis.commands.search import result

from admin.services.manager_categories import ManagerCategories
from admin.shemas.categories_schema import CategoriesSchema
from shared.dependcices.dependcices import conn_dep, redis_dep,lang_dep
from shared.dependcices.securite_decode_token import decode_token
from shared.errors.admin_errors import AdminError
from shared.errors.auth_errors import TokenError

from shared.errors.categories_errors import CategoriesError
from shared.errors.db_errors import DbError

router = APIRouter(prefix="/api/v1/admin/categories", tags=["Admin-categories"])

@router.get("/")
async def get_categories(connection : conn_dep,redis:redis_dep,lang:lang_dep , payload = Depends(decode_token)):
    try:
        services = ManagerCategories(connection=connection, redis=redis, lang=lang)
        result = await  services.get_categories(payload=payload)
        return result
    except AdminError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    except DbError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    # except Exception as e:
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="error in server")


@router.post("/",status_code=status.HTTP_201_CREATED)
async def add_categories(category_schema: CategoriesSchema,connection : conn_dep,redis:redis_dep,lang:lang_dep,payload = Depends(decode_token)):
    try:
        services = ManagerCategories(connection=connection, redis=redis, lang=lang)
        result = await services.add_categories(category_name=category_schema.category_name, payload=payload)
        return result
    except AdminError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=str(e))
    except CategoriesError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    except DbError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
    # except Exception as e:
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="error in server")

@router.delete("/")
async def delete_categories(category_schema: CategoriesSchema,connection : conn_dep,redis:redis_dep,lang:lang_dep,payload = Depends(decode_token)):
    try :
        services = ManagerCategories(connection=connection, redis=redis, lang=lang)
        result = await services.remove_categories(category_name=category_schema.category_name, payload=payload)
        return result
    except CategoriesError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except AdminError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    except DbError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    # except Exception as e:
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="error in server")
