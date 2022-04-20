#ifndef HEROIDLE_KINGDOM_HPP
#define HEROIDLE_KINGDOM_HPP

#include <nlohmann/json.hpp>

using json_t = nlohmann::json;

struct Kingdom
{
    uint cityhall{1};
    uint goldmine{1};
    uint stonemine{1};
    uint sawmill{1};
    uint trainingroom{0};
    uint warehouse{1};

    json_t toJson() const
    {
        return
        {
            {"cityhall",        cityhall},
            {"goldmine",        goldmine},
            {"stonemine",       stonemine},
            {"sawmill",         sawmill},
            {"trainingroom",    trainingroom},
            {"warehouse",       warehouse}
        };
    }
};

#endif //HEROIDLE_KINGDOM_HPP
