#ifndef HEROIDLE_WAREHOUSE_HPP
#define HEROIDLE_WAREHOUSE_HPP

#include <nlohmann/json.hpp>
#include <array>

using json_t = nlohmann::json;

struct Resource
{
    uint amount{1000};
    uint on_hand{0};
    uint on_hand_max{100};

    json_t toJson() const
    {
        return
        {
            {"amount", amount},
            {"on_hand", on_hand},
            {"on_hand_max", on_hand_max}
        };
    }
};

struct Warehouse
{
    Resource gold;
    Resource stone;
    Resource wood;

    constexpr std::array<Resource*, 3> getResourcesArray()
    {
        return std::array<Resource*, 3> {&gold, &stone, &wood};
    }

    json_t toJson() const
    {
        return
        {
            {"gold",        gold.toJson()},
            {"stone",        stone.toJson()},
            {"wood",       wood.toJson()}
        };
    }
};

#endif //HEROIDLE_WAREHOUSE_HPP
