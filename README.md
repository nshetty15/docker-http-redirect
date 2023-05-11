# docker-http-redirect
Docker container that can be configured to redirect all incoming HTTP traffic to a target location.

### ENV Variables

- PORT =  Port on which the web server listen's on. Default is 80.
- REDIRECT_TARGET = (Required) Target location where all traffic should be redirected to. This should contain both HTTP scheme and netloc. Eg: https://www.example.com
- REDIRECT_STATUS_CODE = Use any redirect status code like 301, 302, 303, 307, 308. Default is 301.
- FLASK_ENV = default is PRODUCTION which runs waitress server. Other option is DEVELOPMENT which runs flask dev server.

## Docker Image
- Docker Hub - https://hub.docker.com/r/nshetty15/docker-http-redirect
- Dockerfile - https://github.com/nshetty15/docker-http-redirect/blob/59e960ce8ad3d8d457b18def115305dbf8afadab/Dockerfile

## How to run?

```sh
docker run --rm -d -p 5000:5000 -e PORT=5000 -e REDIRECT_TARGET=https://www.my-domain.com/sports -e REDIRECT_STATUS_CODE=308 nshetty15/docker-http-redirect
```

Once the container is running, simply send the request to the running application
```sh
curl --location --request GET 'localhost:5000/sports'
```
Check the logs to see the redirection take place.

```sh
GET http://localhost:5000/sports   308
GET https://www.my-domain.com/sports 200
```
## License

MIT



