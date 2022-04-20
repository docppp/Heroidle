#ifndef HEROIDLE_SERVER_HPP
#define HEROIDLE_SERVER_HPP

#include <mutex>
#include <optional>
#include <string>
#include <vector>
#include <zmq.hpp>
#include "player.hpp"

class Server
{
public:
    Server();

    void loadPlayers();
    void saveOnlinePlayersToDB();
    void updateOnlinePlayers();
    void forcePlayerSave(const std::string& username);
    bool createPlayer(const std::string& username);
    void loginPlayer(const std::string& username);
    void logoutPlayer(const std::string& username);

    std::optional<json_t> getOnlinePlayerInfo(const std::string& username) const;
    std::vector<std::string> getOnlinePlayersUsername() const;
    std::vector<std::string> getOfflinePlayersUsername() const;

private:
    std::mutex mutex;

    zmq::context_t ctx;
    zmq::socket_t sock;

    std::vector<Player> onlinePlayers;
    std::vector<Player> offlinePlayers;
};


#endif //HEROIDLE_SERVER_HPP
