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
        String fileName = "C:\\concern.txt";
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
           System.out.println(aList.get(i).toString()); // displays everything
            
        }
    }
    
}


