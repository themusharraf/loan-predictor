from prometheus_client import Counter, Histogram, generate_latest
from starlette.requests import Request
from fastapi import APIRouter, Response

REQUEST_COUNT = Counter(
    "request_count", "Total request count", ["method", "endpoint", "http_status"]
)

REQUEST_LATENCY = Histogram(
    "request_latency_seconds", "Request latency", ["endpoint"]
)

router = APIRouter()


@router.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")


async def prometheus_middleware(request: Request, call_next):
    import time
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    REQUEST_COUNT.labels(request.method, request.url.path, response.status_code).inc()
    REQUEST_LATENCY.labels(request.url.path).observe(process_time)
    return response
