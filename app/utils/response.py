from fastapi.responses import JSONResponse

def success_response(data, status_code=200):
    return JSONResponse(content={"data": data, "message": "Success"}, status_code=status_code)

def error_response(message, status_code):
    return JSONResponse(content={"message": message}, status_code=status_code)
