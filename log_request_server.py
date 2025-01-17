from flask import Flask, request

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
    return {"message": "Request received. Check server logs for details."}, 200

if __name__ == "__main__":
    # Bind to all IPv6 addresses (::)
    app.run(host="::", port=5000)

