//
// Created by Lei Ma on 4/4/17.
//

#ifndef CPP_ANIMAL_H
#define CPP_ANIMAL_H


class Animal {

private:
    int height;
    int weight;
    string name;

    static int howmany;


public:
    int getHeight(){
        return height;
    }
    int getWeight(){
        return weight;
    }
    string getName(){
        return name;
    }
    void setHeight(int cm) {
        height = cm;
    }
    void setWeight(int kg) {
        weight = kg;
    }
    void setName(int animalName){
        height=animalName;
    }

    void setAll(int, int, string);

    Animal(int,int,string);
    ~Animal();
    Animal();

    static int getHowMany(){return howmany;}

    void toString();

};


#endif //CPP_ANIMAL_H
