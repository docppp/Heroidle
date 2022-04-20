#ifndef HEROIDLE_RESOURCE_HPP
#define HEROIDLE_RESOURCE_HPP

#include <cstdio>
#include <string>
#include <utility>
#include <array>
#include <nlohmann/json.hpp>
#include "calculator.hpp"
#include "kingdom.hpp"
#include "warehouse.hpp"

using json_t = nlohmann::json;

struct Character
{
    uint lvl{1};
    uint exp{0};
    uint honor{0};

    json_t toJson() const
    {
        return
        {
            {"lvl",     lvl},
            {"exp",     exp},
            {"honor",   honor}
        };
    }
};

class Player
{
public:
    explicit Player(std::string name) :
    username(std::move(name)),
    kingdom(Kingdom{}),
    warehouse(Warehouse{}),
    calc(Calculator{&kingdom, &warehouse})
    {
    }

    Player(const Player&) = delete;
    Player& operator=(const Player&) = delete;

    Player(Player&&) = default;
    Player& operator=(Player&&) = default;

    void update()
    {
        calc.updateResources();
    }

    void moveFromHand()
    {
        for (auto res : warehouse.getResourcesArray())
        {
            res->amount += res->on_hand;
            res->on_hand = 0;
        }
    }

    const std::string getUsername() const { return username; }

    json_t toJson() const
    {
        return
        {
                {"user",        username},
                {"character",   character.toJson()},
                {"kingdom",     kingdom.toJson()},
                {"warehouse",   warehouse.toJson()},
                {"income",      calc.toJsonIncome()}
        };
    }

private:
    std::string username;
    Calculator calc;
    Character character;
    Kingdom kingdom;
    Warehouse warehouse;
};

#endif //HEROIDLE_RESOURCE_HPP
