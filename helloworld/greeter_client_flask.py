#Una vez iniciado el servidor tanto del grpc y el servidor de flask entonces esto ya se puede visualizar en el navegador
from flask import Flask #Se importa la libreria
import grpc

import helloworld_pb2
import helloworld_pb2_grpc
app=Flask(__name__) #Variable especial __name__ que devuelve el string para poder ejecutar el programa
@app.route('/') #mapea la dirección 

def run():
  channel = grpc.insecure_channel('localhost:50051') #canal local que se abre del servidor al cliente grpc
  stub = helloworld_pb2_grpc.GreeterStub(channel)
  response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
  return "Nuevo cliente recibido" + response.message


if __name__ == '__main__': #ejecución del script, aquí se mantiene el __main__ porque no se esta importando de otro script
  app.run(host='localhost') 
