/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
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
        String fileName = "C:\\projects\\concern.txt";
        String line;
        ArrayList aList = new ArrayList();
        
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
        
        //
//        String[] columnDetail = new String[11]; 
  //      columnDetail = column.split("\\t");
        
        for (int i = 0; i < sz; i++) {
                System.out.println(aList); // displays everything

                String value = aList.get(i).toString();

                String column1 = value.substring(0, 1);
                String column2 = value.substring(2);

               boolean s1 = column1.contains("1");
               boolean s2 = column1.contains("2");
               boolean s3 = column1.contains("3");
             // Replace letter with underscore.
                if (s1 == true){
             String result = column1.replaceFirst("1", "Everything is Fine");
             System.out.println(result);

                }
                if (s2 == true){
              String result = column1.replaceFirst("2", "Caution, please look into this: ");      
              System.out.println(result);
                 System.out.println(column2);
                }
                 if (s3 == true)
                 {
              String result = column1.replaceFirst("3", "URGENT, this requires immediate attention: ");      

              System.out.println(result);
                 System.out.println(column2);
                 }
     
            
            }
        }
           
    }
