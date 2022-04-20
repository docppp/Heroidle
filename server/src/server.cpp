#include <iostream>
#include "server.hpp"

Server::Server()
{
    sock = zmq::socket_t(ctx, zmq::socket_type::rep);
    sock.bind("tcp://127.0.0.1:5050");
    const std::string last_endpoint = sock.get(zmq::sockopt::last_endpoint);
    std::cout << "Connecting to " << last_endpoint << std::endl;
}

std::optional<json_t> Server::getOnlinePlayerInfo(const std::string &username) const
{
    for (const Player& p : onlinePlayers)
    {
        if (p.getUsername() == username) { return p.toJson(); }
    }
    return std::nullopt;
}

void Server::updateOnlinePlayers()
{
    std::scoped_lock lock(mutex);
    for (Player& p : onlinePlayers) { p.update(); }
}

bool Server::createPlayer(const std::string &username)
{
    std::scoped_lock lock(mutex);
    for (const Player& p : onlinePlayers)
    {
        if (p.getUsername() == username) { return false; }
    }
    for (const Player& p : offlinePlayers)
    {
        if (p.getUsername() == username) { return false; }
    }
    onlinePlayers.push_back(Player{username});
    return true;
}

void Server::loginPlayer(const std::string &username)
{
    std::scoped_lock lock(mutex);
    for (auto it = offlinePlayers.begin(); it != offlinePlayers.end(); ++it)
    {
        if (it->getUsername() == username)
        {
            onlinePlayers.push_back(std::move(*it));
            offlinePlayers.erase(it);
            return;
        }
    }
}

void Server::logoutPlayer(const std::string &username)
{
    std::scoped_lock lock(mutex);
    for (auto it = onlinePlayers.begin(); it != onlinePlayers.end(); ++it)
    {
        if (it->getUsername() == username)
        {
            offlinePlayers.push_back(std::move(*it));
            onlinePlayers.erase(it);
            return;
        }
    }
}

std::vector<std::string> Server::getOnlinePlayersUsername() const
{
    std::vector<std::string> result;
    for (const Player& p : onlinePlayers) { result.push_back(p.getUsername()); }
    return result;
}

std::vector<std::string> Server::getOfflinePlayersUsername() const
{
    std::vector<std::string> result;
    for (const Player& p : offlinePlayers) { result.push_back(p.getUsername()); }
    return result;
}