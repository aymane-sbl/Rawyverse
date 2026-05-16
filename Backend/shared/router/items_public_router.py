from fastapi import APIRouter,Depends, HTTPException,Query,Path,status

from shared.services.manager_public_items import ManagerPublicItems
from shared.dependcices.dependcices import conn_dep, redis_dep, lang_dep
from shared.errors.db_errors import DbError
from shared.errors.items_errors import ItemsError

router = APIRouter(prefix="/api/v1/items", tags=["public-items"])
@router.get("/")
async def get_items(connection : conn_dep,redis:redis_dep,lang:lang_dep,page:int=Query(default=1,gt=0),limit:int=Query(default=20,gt=1)):
    try :
        services = ManagerPublicItems(connection=connection, redis=redis, lang=lang)
        result = await services.get_items(page=page,limit_items=limit,)
        return result
    except DbError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    # except Exception as e:
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="error in server")
@router.get("/details/{id}")
async def get_items_by_id(connection : conn_dep,redis:redis_dep,lang:lang_dep,id:int=Path(...)):
    try:
        services = ManagerPublicItems(connection=connection, redis=redis, lang=lang)
        result = await services.get_items_by_id(id=id)
        return result
    except ItemsError as e :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))
    except DbError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    # except Exception as e:
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="error in server")