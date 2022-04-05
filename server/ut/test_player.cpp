#include <gtest/gtest.h>
#include <nlohmann/json.hpp>
#include "resource.hpp"

extern const json_t newPlayerJson;

TEST(TestPlayer, testPlayerJson)
{
    Player p{"user1"};
    EXPECT_EQ(p.toJson(), newPlayerJson);
}


const json_t newPlayerJson = {
            {"user",    "user1"},
            {"character",
                        {
                                {"lvl",     1},
                                {"exp",     0},
                                {"honor",   0}
                        }
            }, // character
            {"kingdom",
                        {
                                {"cityhall",        1},
                                {"goldmine",        1},
                                {"stonemine",       1},
                                {"sawmill",         1},
                                {"trainingroom",    0}
                        }
            }, // kingdom
            {"warehouse",
                        {
                                {"gold",
                                        {
                                                    {"amount",      1000},
                                                    {"onhand",      0},
                                                    {"onhandmax",   100},
                                                    {"income",      10}
                                            }
                                },
                                {"stone",
                                        {
                                                    {"amount",      1000},
                                                    {"onhand",      0},
                                                    {"onhandmax",   100},
                                                    {"income",      10}
                                            }
                                },
                                {"wood",
                                        {
                                                    {"amount",      1000},
                                                    {"onhand",      0},
                                                    {"onhandmax",   100},
                                                    {"income",      10}
                                            }
                                }
                        }
            } // warehouse
};

