using System;
using Grpc.Core;
using Grpc.Net.Client;

namespace client
{
    class Medicamento
    {
        static void Main(string[] args)
        {
            // Este conmutador debe establecerse antes de crear GrpcChannel/HttpClient.
            AppContext.SetSwitch(
                "System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport", true);
            var channel = GrpcChannel.ForAddress("http://localhost:5500");
            //Canal que se conecta a la direccion en la cual se va a encontrar mi servicio
            var client = new Farmacia.FarmaciaClient(channel);

            var medicamento = new Medicamento{id = 1, nombre = "Abaloparatida", 2, codigo = "DFR-64938-3", tipo = "colirio"};
        }
    }
}
