from shared.errors.users_errors import UsersError


async def check_rate_limit(identifier,action_type:str,number_attempts:int,time:int,error_content:str,redis):
    redis_key = f"rate_limit:{action_type}:{identifier}"
    attempts = await redis.incr(redis_key)

    if attempts == 1:
         await redis.expire(redis_key,time)
    if attempts > number_attempts :
        raise UsersError(error_content)
    return attempts


