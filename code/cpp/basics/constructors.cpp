//
// Created by Lei Ma on 4/5/17.
//

#include <iostream>
using namespace std;



class TheClassYouNeed {

         public:
            TheClassYouNeed(int x) {
               setWeight(x);
            }

            void setWeight(int x) {
               weight = x;
            }

            int getWeight() {
                return weight;
            }


         private:
            int weight;


 };



int main() {

    TheClassYouNeed cs1(42);

    cout << cs1.getWeight() << endl;

	return 0;
}
