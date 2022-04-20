#ifndef HEROIDLE_CALCULATOR_HPP
#define HEROIDLE_CALCULATOR_HPP

#include <nlohmann/json.hpp>
#include "kingdom.hpp"
#include "warehouse.hpp"

using json_t = nlohmann::json;

class Calculator
{
public:
    explicit Calculator(Kingdom* k, Warehouse* w) : kingdom(k), warehouse(w) {}

    void updateResources()
    {
        warehouse->gold.on_hand += getGoldIncome();
        warehouse->stone.on_hand += getStoneIncome();
        warehouse->wood.on_hand += getWoodIncome();

        for (auto res : warehouse->getResourcesArray())
        {
            if (res->on_hand > res->on_hand_max) { res->on_hand = res->on_hand_max; }
        }
    }

    json_t toJsonIncome() const
    {
        return
        {
            {"gold_income", getGoldIncome()},
            {"stone_income", getStoneIncome()},
            {"wood_income", getWoodIncome()},
        };
    }

private:
    uint getGoldIncome() const { return kingdom->goldmine*10; }
    uint getStoneIncome() const { return kingdom->stonemine*10; }
    uint getWoodIncome() const { return kingdom->sawmill*10; }

    Kingdom* kingdom;
    Warehouse* warehouse;
};
#endif //HEROIDLE_CALCULATOR_HPP
