# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import IBM_pb2 as IBM__pb2


class PredictorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Process = channel.unary_unary(
                '/Predictor/Process',
                request_serializer=IBM__pb2.Request.SerializeToString,
                response_deserializer=IBM__pb2.Response.FromString,
                )


class PredictorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Process(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PredictorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Process': grpc.unary_unary_rpc_method_handler(
                    servicer.Process,
                    request_deserializer=IBM__pb2.Request.FromString,
                    response_serializer=IBM__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Predictor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Predictor(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Process(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Predictor/Process',
            IBM__pb2.Request.SerializeToString,
            IBM__pb2.Response.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
