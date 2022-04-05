#include "server.hpp"

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
            return;
        }
    }
}

void Server::logoutPlayer(const std::string &username)
{
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