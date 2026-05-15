def init_redis_cache(redis,redis_backend,fast_api_cache):
    fast_api_cache.init(redis_backend(redis),prefix='rawyverse_cache')