#include "CarModel.h"
void updatePosition(CarState& car, double dt)
{
    car.x = car.x + car.speed * dt;
};