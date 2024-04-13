#include <chrono>
#include <iostream>
#include "behaviortree_cpp_v3/action_node.h"
#include "behaviortree_cpp_v3/bt_factory.h"

using namespace std::chrono_literals;

class ApproachBall : public BT::SyncActionNode
{
public:
  ApproachBall(const std::string& name) :
      BT::SyncActionNode(name, {})
  {}

  // You must override the virtual function tick()
  BT::NodeStatus tick() override
  {
    std::cout << "ApproachBall: " << this->name() << std::endl;
    
    return BT::NodeStatus::SUCCESS;
  }
};

class BallApproachPlayer2 : public BT::SyncActionNode
{
public:
  BallApproachPlayer2(const std::string& name) :
      BT::SyncActionNode(name, {})
  {}

   //You must override the virtual function tick()
  BT::NodeStatus tick() override
  {
    std::cout << "BallApproachPlayer2: " << this->name() << std::endl;
    std::this_threads::sleep_for(5s)
    return BT::NodeStatus::SUCCESS;
  }
};

class Goalkick : public BT::SyncActionNode
{
public:
  Goalkick(const std::string& name) :
      BT::SyncActionNode(name, {})
  {}

  // You must override the virtual function tick()
  BT::NodeStatus tick() override
  {
    std::cout << "Goalkick: " << this->name() << std::endl;
    std::this_threads::sleep_for(5s)
    return BT::NodeStatus::SUCCESS;
  }
};


int main()
{

 BT::BehaviorTreeFactory factory;

 factory.registerNodeType<ApproachBall>("ApproachBall");

factory.registerNodeType<ApproachObject>("BallApproachPlayer2");

factory.registerNodeType<ApproachObject>("Goalkick");

 auto tree=factory.createTreeFromFile("/home/vboxuse/ros2_ws/src/behavior_tree/src/tree.xml");

 tree.tickRoot();

return 0;
}










