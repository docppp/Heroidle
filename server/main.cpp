//#include <chrono>
//#include <thread>
//#include <iostream>
//#include <ctime>
//#include "resource.hpp"
//#include <zmqpp/zmqpp.hpp>
//
//int main()
//{
//    auto x = std::chrono::steady_clock::now() + std::chrono::milliseconds(1000);
//    std::chrono::time_point<std::chrono::system_clock> time_point;
//
//    time_point = std::chrono::system_clock::now();
//    std::time_t ttp = std::chrono::system_clock::to_time_t(time_point);
//    std::cout << std::ctime(&ttp);
//
//    std::this_thread::sleep_until(x);
//
//    time_point = std::chrono::system_clock::now();
//    std::time_t ttp2 = std::chrono::system_clock::to_time_t(time_point);
//    std::cout << std::ctime(&ttp2);
//}

#include <iostream>
#include <zmq.hpp>
#include <boost/asio.hpp>
#include <boost/thread/thread.hpp>
#include <boost/bind/bind.hpp>
#include "timer.hpp"

int main()
{
    Timer t = Timer();
    t.setInterval([&]() {
        std::cout << "Hey.. After each 1s..." << std::endl;
    }, 1000);

    zmq::context_t ctx;
    zmq::socket_t sock(ctx, zmq::socket_type::rep);
    sock.bind("tcp://127.0.0.1:5050");
    const std::string last_endpoint = sock.get(zmq::sockopt::last_endpoint);
    std::cout << "Connecting to " << last_endpoint << std::endl;

    zmq::message_t msg;

    auto res = sock.recv(msg);
    std::cout << msg.to_string() << "\n";

    sock.send(zmq::str_buffer("response"));

//    std::cout << "Got " << *ret
//              << " messages" << std::endl;
    return 0;
}