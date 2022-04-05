#ifndef HEROIDLE_SERVER_HPP
#define HEROIDLE_SERVER_HPP

#include <optional>
#include <string>
#include <vector>
#include "resource.hpp"

class Server
{
public:
    Server() = default;

    void loadPlayers();
    void saveOnlinePlayersToDB();
    std::optional<json_t> getOnlinePlayerInfo(const std::string& username) const;
    void updateOnlinePlayers();
    void forcePlayerSave(const std::string& username);
    bool createPlayer(const std::string& username);
    void loginPlayer(const std::string& username);
    void logoutPlayer(const std::string& username);
    std::vector<std::string> getOnlinePlayersUsername() const;
    std::vector<std::string> getOfflinePlayersUsername() const;

private:
    std::vector<Player> onlinePlayers;
    std::vector<Player> offlinePlayers;
};


#endif //HEROIDLE_SERVER_HPP
