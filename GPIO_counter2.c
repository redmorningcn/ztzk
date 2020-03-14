#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h> 
char LED = 25; 
 
int main(void)
{
    int i = 0;
    if(wiringPiSetup() < 0)return 1;
    #pinMode (LED,OUTPUT) ;

    wiringPiSetupGpio();            //³õÊ¼»¯ BCM GPIO 
    pinMode(pin,INPUT);
    pullUpDnControl(pin,PUD_DOWN);
    
    while(1)
    {       
        //printf("test %d",i++);

        digitalWrite(LED, 1) ;
        delay (200);
        digitalWrite(LED, 0) ;
        delay (200);
    }   
}
