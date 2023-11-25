def log_request(logger, req, res):
    logger(f"Request: {req.method} {req.url} - Payload: {req.data} - Response: {res.status_code}, {res.content}")