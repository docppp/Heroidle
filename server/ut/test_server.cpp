#include <gtest/gtest.h>
#include <algorithm>
#include <optional>
#include "server.hpp"

bool checkIfPlayerIsOnline(Server& s, const char* username)
{
    auto vOn = s.getOnlinePlayersUsername();
    auto vOff = s.getOfflinePlayersUsername();
    if (std::find(vOn.begin(), vOn.end(), username) != vOn.end() and
        std::find(vOff.begin(), vOff.end(), username) == vOff.end() and
        s.getOnlinePlayerInfo(username) != std::nullopt)
    {
        return true;
    }
    return false;
}

bool checkIfPlayerIsOffline(Server& s, const char* username)
{
    auto vOn = s.getOnlinePlayersUsername();
    auto vOff = s.getOfflinePlayersUsername();
    if (std::find(vOn.begin(), vOn.end(), username) == vOn.end() and
        std::find(vOff.begin(), vOff.end(), username) != vOff.end() and
        s.getOnlinePlayerInfo(username) == std::nullopt)
    {
        return true;
    }
    return false;
}

TEST(TestServer, createdPlayerIsOnline)
{
    Server s{};
    s.createPlayer("user1");
    EXPECT_TRUE(checkIfPlayerIsOnline(s, "user1"));
}

TEST(TestServer, logoutPlayerIsNotOnline)
{
    Server s{};
    s.createPlayer("user1");
    s.logoutPlayer("user1");
    EXPECT_TRUE(checkIfPlayerIsOffline(s, "user1"));
}

TEST(TestServer, multipleLoginLogout)
{
    Server s{};
    s.createPlayer("user1");
    s.loginPlayer("user1");
    EXPECT_TRUE(checkIfPlayerIsOnline(s, "user1"));
    s.loginPlayer("user1");
    EXPECT_TRUE(checkIfPlayerIsOnline(s, "user1"));
    s.logoutPlayer("user1");
    s.logoutPlayer("user1");
    EXPECT_TRUE(checkIfPlayerIsOffline(s, "user1"));
}
