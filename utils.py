def log_request(logger, req, res):
    logger(f"Request: Header: {req.headers}\nMethod:{req.method}\nURL:{req.url}\nPayload: {req.data}\nResponse: {res.status_code}, {res.content}")