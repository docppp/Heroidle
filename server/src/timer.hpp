//
// Created by root on 4/1/22.
//

#ifndef HEROIDLE_TIMER_HPP
#define HEROIDLE_TIMER_HPP

#include <iostream>
#include <boost/asio.hpp>
#include <boost/bind/bind.hpp>
#include <iostream>
#include <thread>
#include <chrono>
#include <atomic>

class Timer {
    std::atomic<bool> active{true};

public:
    void setTimeout(auto function, int delay);
    void setInterval(auto function, int interval);
    void stop();

};

void Timer::setTimeout(auto function, int delay) {
    active = true;
    std::thread t([=]() {
        if(!active.load()) return;
        std::this_thread::sleep_for(std::chrono::milliseconds(delay));
        if(!active.load()) return;
        function();
    });
    t.detach();
}

void Timer::setInterval(auto function, int interval) {
    active = true;
    std::thread t([=]() {
        while(active.load()) {
            std::this_thread::sleep_for(std::chrono::milliseconds(interval));
            if(!active.load()) return;
            function();
        }
    });
    t.detach();
}

void Timer::stop() {
    active = false;
}

#endif //HEROIDLE_TIMER_HPP
