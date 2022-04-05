#include "server.hpp"

std::optional<json_t> Server::getPlayerInfo(const std::string &username) const
{
    for (const Player& p : onlinePlayers)
    {
        if (p.getUsername() == username) { return p.toJson(); }
    }
    return std::nullopt;
}

void Server::updateOnlinePlayers()
{
    for (Player& p : onlinePlayers) { p.update(); }
}

bool Server::createPlayer(const std::string &username)
{
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
    for (auto it = offlinePlayers.begin(); it != offlinePlayers.end(); ++it)
    {
        if (it->getUsername() == username)
        {
            onlinePlayers.push_back(std::move(*it));
            offlinePlayers.erase(it);
        }
    }
}