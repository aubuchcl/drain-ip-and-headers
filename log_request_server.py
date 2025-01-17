from flask import Flask, request
import json 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
def log_request():
    # Get originating IP address
    originating_ip = request.remote_addr

    # Get request headers
    headers = dict(request.headers)

    # Get request body (if any)
    body = request.get_data(as_text=True)

    # Log details to the console
    print("=== Incoming Request ===")
    print(f"Originating IP: {originating_ip}")
    print("Headers:")
    for key, value in headers.items():
        print(f"  {key}: {value}")
    print("Body:")
    print(body if body else "  No body data")
    print("========================")

    # Respond to the client

    # Convert request object to a dictionary
    request_dict = {
        "method": request.method,
        "url": request.url,
        "headers": headers,
        "args": request.args.to_dict(),  # Query parameters
        "form": request.form.to_dict(),  # Form data
        "json": request.json,            # JSON body (parsed if content-type is application/json)
        "data": body                     # Raw body data
    }

    # Log details to the console
    print("=== Incoming Request ===")
    print(f"Originating IP: {originating_ip}")
    print("Entire Request Object as Dictionary:")
    print(json.dumps(request_dict, indent=2))  # Pretty-print the dictionary
    print("========================")


    return {"message": "Request received. Check server logs for details."}, 200

if __name__ == "__main__":
    # Bind to all IPv6 addresses (::)
    app.run(host="::", port=5000)

