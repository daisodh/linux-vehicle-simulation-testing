#include<iostream>
#include <string>
#include <string>
#include <stdexcept>
#include "CarModel.h"
#include <cmath>
#include <fstream>
using namespace std;


int main(int argc, char* argv[]){
if (argc != 3)
{
    // 提示用户正确输入格式
cerr << "Usage: ./car_sim <speed> <steps>" << endl;
    // 结束程序
    return 1;
}
CarState states;
size_t pos =0;
size_t speedpos = 0;
states.x=0;
states.y=0;
int steps;
try{
states.speed=stod(argv[1],&speedpos);
 steps=stoi(argv[2],&pos);}
catch(const invalid_argument&e){
	cerr<<"请输入正确格式"<<endl;
	return 1;
}
catch (const out_of_range& e)
{
    cerr << "输入数值超出允许范围" << endl;
    return 1;
}
if(states.speed<0||states.speed>30||!isfinite(states.speed)){
	  cerr << "速度超出允许范围" << endl;
	  return 1;
}
if (steps <= 0 || steps > 1000 )
{
    cerr << "steps超出允许范围" << endl;
    return 1;
}
if (pos != string(argv[2]).size())
{
    cerr << "运动次数包含非法字符" << endl;
    return 1;
}
if (speedpos != string(argv[1]).size())
{
    cerr << "速度包含非法字符" << endl;
    return 1;
}
double dt=1;
ofstream file("trajectory.csv");

if (!file.is_open())
{
    cerr << "无法创建轨迹文件" << endl;
    return 1;
}
file << "time_s,x_m,y_m,speed_mps\n";
file << 0 << "," << states.x
	<<","<<states.y
	<<","<<states.speed<<endl;;
	
for(int i=0;i<steps;i++){
	updatePosition(states,dt);
	file<<(i+1)*dt
	<<","<<states.x
	<<","<<states.y
	<<","<<states.speed<<'\n';
}
file.close();

if (!file)
{
    cerr << "轨迹文件写入失败" << endl;
    return 1;
}

cout<<states.x<<endl;
cout<<states.y<<endl;
cout<<states.speed<<endl;
return 0;
}
