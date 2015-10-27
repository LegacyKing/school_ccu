/* 
 * File:   main.cpp
 * Author: Andrew
 *
 * Created on September 15, 2015, 6:37 AM
 */


#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include <limits>
using namespace std;

// Declarations
int userPromptStatus;       // Value that is written to file, and prompts the three statuses
int biblePromptStatus;
int detailFunction();
int bibleVerses();
string userPromptComment;   // User Input for Caution or Emergency routine
ofstream myfile;            // method to write to file
string finished = "n";
int f = 0;



/*
 * Main Program
 */

int main() 
{
    // create file "concern.txt" to write values to.
   // NOTE! In Windows you must run this program as an ADMINISTRATOR, or else the file cannot be created.
        myfile.open("C:\\concern.txt");
   
    
    // Display message to user to get first prompt. We assume the user will enter a value of 1, 2 or 3.
    // No steps taken to ensure a valid value is used. Any invalid input simply moves to the exit routine.
    cout << "Welcome to the Bible verses review and personal introspection tool.\n";
    while ( f == 0 )
    {
        bibleVerses();  // launch the bibleVerses module as long as f is "0"
    }
    
    // Close the file, as we no longer need it. Proper procedure to make sure value is saved.
    myfile.close(); 
    return 0; // exit program
}

/**
 * bibleVerses module is a Scripture passage displayed upon the screen. Each verse is completely exposed to be read
 * The user is prompted to select their verse and then list the 1, 2, or 3, and then if 2 or 3, they will be prompted to write their concern(s)
 * 
 * 
 **/

int bibleVerses()
{
    cout << "Choose a Bible Verse:\n";
    cout << "1 = Romans 12:2 'Do not conform to the patterns of this world, but be transformed by the renewing of your mind, then you will be able to test and approve of God's will. His good, pleasing and perfect will.'\n";
    cout << "2 = Romans 12:1 'Therefore, I urge you, brothers and sisters, in view of God’s mercy, to offer your bodies as a living sacrifice, holy and pleasing to God—this is your true and proper worship.'\n";
    cout << "3 = John 3:16 'For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.'\n";
    cout << "4 = James 3:16 'For where you have envy and selfish ambition, there you find disorder and every evil practice.'\n";
    cout << "5 = 2 Timothy 3:16-17 'All Scripture is God-breathed and is useful for teaching, rebuking, correcting and training in righteousness, so that the servant of God may be thoroughly equipped for every good work.'\n";
    cout << "6 = 1 Corinthians 6:18-20 'Flee from sexual immorality. All other sins a person commits are outside the body, but whoever sins sexually, sins against their own body. 19 Do you not know that your bodies are temples of the Holy Spirit, who is in you, whom you have received from God? You are not your own; 20 you were bought at a price. Therefore honor God with your bodies.'\n";
    cout << "7 = 1 Thessalonians 4:3-8 'It is God’s will that you should be sanctified: that you should avoid sexual immorality; 4 that each of you should learn to control your own body[a] in a way that is holy and honorable, 5 not in passionate lust like the pagans, who do not know God; 6 and that in this matter no one should wrong or take advantage of a brother or sister.[b] The Lord will punish all those who commit such sins, as we told you and warned you before. 7 For God did not call us to be impure, but to live a holy life. 8 Therefore, anyone who rejects this instruction does not reject a human being but God, the very God who gives you his Holy Spirit.'\n";
    cout << "8 = Titus 3:1-2 'Remind the people to be subject to rulers and authorities, to be obedient, to be ready to do whatever is good, 2 to slander no one, to be peaceable and considerate, and always to be gentle toward everyone.'\n";
    cout << "\nEnter Choice 1-8 please:\n";
    cin >> biblePromptStatus;   // We set up a prompt
    

    // Prompt for level of concern regarding the selected scripture.  
    cout << "Please indicate the numerical status for this Bible verse:\n";
    cout << "1 = normal\n";
    cout << "2 = caution\n";
    cout << "3 = emergency\n";
    cin >> userPromptStatus;
    detailFunction();
    // method to keep screen open for option 1 to get screen shot.
    if (userPromptStatus == 1)
    {
        char temp = 'x';
        while (temp != '\n')
        cin.get(temp);
    }
    // Display message if the UserPromptStatus was 2 or 3
    if (userPromptStatus == 2 || userPromptStatus == 3)
    {
    cout << "\nArea of concern is:\n";
    cout << userPromptComment;
    cout << endl;
    }
    // Keep console open for reading and allow for a screen shot. 
    // cin.get was not a viable option this time, unlike HelloWorld.
    // This solution was found after online research. 
   
    // whether to continue with another Bible verse.
     cout << "\nfinished reviewing Bible verses? (y/n):\n";
     cin >> finished;
     if (finished == "y")
     {
         f = 1;
     }
}

// Prompts user for input only if "2" or "3" was set for 'userPromptStatus'
int detailFunction()
{
   string resume = "n";
   myfile << userPromptStatus << "\t";  // We take the user input for the status and drop it in the file here and add a TAB space.

   if (userPromptStatus == 2)
   {
        while (resume == "n")
        {
        cout << "Please indicate area of concern:\n";
        cin.ignore();                                   // This is a online researched solution
	getline( cin, userPromptComment );  
        myfile << userPromptComment << "\t";    // take the comment and append a TAB space.
       
        cout << "Finished with concerns? (y/n)\n";  // continue loop?
        cin >> resume;
        }
   }
   if (userPromptStatus == 3)
   {
        while (resume == "n"){
        cout << "Please indicate what needs immediate attention:\n";
        cin.ignore();
	getline( cin, userPromptComment );
        myfile << userPromptComment << "\t";       // take the comment and append a TAB space.
        cout << "Finished with concerns? (y/n)\n";  // continue loop?
        cin >> resume;
        }
   } 
   
}


