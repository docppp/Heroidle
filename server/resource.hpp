#ifndef HEROIDLE_RESOURCE_HPP
#define HEROIDLE_RESOURCE_HPP


#include <cstdio>
#include <string>
#include <utility>
#include <array>

struct Resource
{
    uint amount{1000};
    uint on_hand{0};
    uint on_hand_max{100};
};

struct Warehouse
{
    uint lvl{1};
    Resource gold;
    Resource stone;
    Resource wood;

    constexpr std::array<Resource*, 3> getResourcesArray()
    {
        return std::array<Resource*, 3> {&gold, &stone, &wood};
    }
};

struct Kingdom
{
    uint cityhall{1};
    uint goldmine{1};
    uint stonemine{1};
    uint sawmill{1};
    uint trainingroom{1};
};

struct Character
{
    uint lvl{1};
    uint exp{0};
    uint honor{0};
};

class Player
{
public:
    explicit Player(std::string username) : username(std::move(username)) {}

    void update()
    {
        warehouse.gold.on_hand += kingdom.goldmine*10;
        warehouse.stone.on_hand += kingdom.stonemine*10;
        warehouse.wood.on_hand += kingdom.sawmill*10;

        for (auto res : warehouse.getResourcesArray())
        {
            if (res->on_hand > res->on_hand_max) { res->on_hand = res->on_hand_max; }
        }
    }

    void moveFromHand()
    {
        for (auto res : warehouse.getResourcesArray())
        {
            res->amount += res->on_hand;
            res->on_hand = 0;
        }
    }

private:
    std::string username;
    Character character;
    Kingdom kingdom;
    Warehouse warehouse;
};

#endif //HEROIDLE_RESOURCE_HPP
