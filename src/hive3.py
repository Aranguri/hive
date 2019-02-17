from apiserve import ApiServer, ApiRoute
from hive2 import model_wrapper

class MyServer(ApiServer):
        @ApiRoute("/request")
        def addbar(req):
            return model_wrapper(req['category'][0], req['text'][0])

MyServer("127.0.0.1",8000).serve_forever()
