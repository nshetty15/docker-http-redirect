import os
from flask import Flask, request
import urllib.parse
from waitress import serve

app = Flask(__name__)

PORT = int(os.environ.get("PORT", 80))
REDIRECT_TARGET = os.environ.get("REDIRECT_TARGET")
REDIRECT_STATUS_CODE = os.environ.get("REDIRECT_STATUS_CODE", 301)
FLASK_ENV = os.environ.get("FLASK_ENV", "PRODUCTION").upper()

if not REDIRECT_TARGET:
    print("ERROR: REDIRECT_TARGET environment variable not found. Exiting.")
    exit(1)

print(
    f"ENV vars - FLASK_ENV={FLASK_ENV}, PORT={PORT}, REDIRECT_TARGET={REDIRECT_TARGET}, REDIRECT_STATUS_CODE={REDIRECT_STATUS_CODE}"
)

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

@app.route("/", methods=HTTP_METHODS, defaults={"path": ""})
@app.route("/<path:path>", methods=HTTP_METHODS)
def catch_all(path):
    parsed_redirect_target = urllib.parse.urlparse(REDIRECT_TARGET)
    new_redirect_url = urllib.parse.urlparse(request.url)._replace(
        scheme=parsed_redirect_target.scheme, netloc=parsed_redirect_target.netloc
    )
    headers = {"Location": new_redirect_url.geturl()}
    return "", int(REDIRECT_STATUS_CODE), headers

if __name__ == "__main__":
    print(f"INFO: running flask app on port: {PORT}")
    print(
        f"INFO: redirecting all traffic to {REDIRECT_TARGET} with HTTP status code {REDIRECT_STATUS_CODE}"
    )
    if FLASK_ENV == "DEVELOPMENT":
        app.run(host="0.0.0.0", port=PORT, debug=True)
    else:
        serve(app, host="0.0.0.0", port=PORT)
