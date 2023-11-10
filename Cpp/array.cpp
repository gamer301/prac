#include <iostream>
using namespace std;
class arr
{
 public :
  arr()
  {
    cout<<"construc"<<endl;
  }
    arr(char a)
  {
    cout<<"construc para:"<<a<<endl;
  }
  ~arr()
  {
    cout<<"\ndestructor";
  }


}instance('u');

  int main ()
  {
      cout<<"main";
  }