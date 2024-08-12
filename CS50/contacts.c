#include <stdio.h>
#include <cs50.h>

int main(void)

{
    string name=get_string("what's your name?");
    int age=get_int("how old are you?");
    string number=get_string("what's your phone number?");
    printf("your name is %s,your age is %i,your number is %s\n",name,age,number);
}
