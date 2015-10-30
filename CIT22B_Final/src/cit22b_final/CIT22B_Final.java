/*
 * Final Project for CIT 220A
 */
package cit22b_final;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
//import java.util.*;
/**
 *
 * @author Andrew
 */
public class CIT22B_Final {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        String fileName = "C:\\concern.txt";  // open our text file, w       
        String line;    // Temp string to add to our arrayList
        ArrayList aList = new ArrayList();  // aList is our new arrayList to hold the file contents
        
        // This will open the file, unless it's not ready, then we'll have an IO Exception.
        try {
            try (BufferedReader input = new BufferedReader(new FileReader(fileName))) {
                if (!input.ready())
                {
                    throw new IOException();
                }
                while ((line = input.readLine()) != null) {
                    aList.add(line);
                }   
            }
        } catch (IOException e) {
            System.out.println(e);
        }
        
     // Print out each item in the ArrayList.
        int sz = aList.size();
        
        for (int i = 0; i < sz; i++) {      // Loop through each line
              //  System.out.println(aList); // displays everything

                String value = aList.get(i).toString(); // set a new string "value" to hold each index location for output

                String column1 = value.substring(0, 1); // this grabs the 1st value, a 1, 2 or 3.
                String column2 = value.substring(2); // this extends to the rest of the string. If a tab is missing after the "1" this will throw an exception.
                    // We set up s1, s2, and s3 to be a boolean trigger to determine which output we want.
               boolean s1 = column1.contains("1");
               boolean s2 = column1.contains("2");
               boolean s3 = column1.contains("3");
             // Replace letter with underscore.
                if (s1 == true){
             String result = column1.replaceFirst("1", "Everything is Fine");   // We replace the "1" with the text desired
             System.out.println(result);    // Print the replaced string
             System.out.println();         // Add newline

                }
                if (s2 == true){
              String result = column1.replaceFirst("2", "Caution, please look into this: ");      
              System.out.println(result);   // Print the replaced string
                 System.out.println(column2);   // Print the remaining string
                 System.out.println();         // Add newline to format
                }
                 if (s3 == true)
                 {
              String result = column1.replaceFirst("3", "URGENT, this requires immediate attention: ");      

              System.out.println(result);   // Print the replaced string
                 System.out.println(column2);   // Print the remaining string
                 System.out.println();          // Add newline to format
                 }
            }
        }
    }
// End of File

