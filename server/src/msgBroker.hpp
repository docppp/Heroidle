#ifndef HEROIDLE_MSGBROKER_HPP
#define HEROIDLE_MSGBROKER_HPP

#include <zmq.hpp>
#include "server.hpp"

class MsgBroker
{
    MsgBroker(Server* s, zmq::socket_t* sock) : server(s), socket(sock) {}
private:
    Server* server;
    zmq::socket_t* socket;
};

#endif //HEROIDLE_MSGBROKER_HPP
