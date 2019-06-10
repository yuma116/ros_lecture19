#include <beginner_tutorials/DoDishesAction.h>
#include <actionlib/client/simple_action_client.h>

typedef actionlib::SimpleActionClient<beginner_tutorials::DoDishesAction> Client;
int main(int argc, char **argv)
{
    ros::init(argc, argv, "do_dishes_client");
    Client client("do_dishes", true); // true -> don't need ros::spin()
    client.waitForServer();
    beginner_tutorials::DoDishesGoal goal;
    // Fill in goal here
    client.sendGoal(goal);
    client.waitForResult(ros::Duration(5.0));
    if(client.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
        printf("Yay! The dishes are now clean");
    printf("Current State: %s", client.getState().toString().c_str());
    return 0;
}