PROCEDURE FOR RUNNING SPICE SIMULATONS
1. The file ee18btech11034_1.net is circuit netlist for feedback circuit having feedback gain as 0.01
2. Run the command ngspice ee18btech11034_1.net in the terminal of the folder
3. The following command creates ee18btech11034_1.dat file which is output voltage values with respect to time
4. Import the .dat file into ee18btech11034_spice_result1.py and run the file.
5. Plot of step response verses time is observed
6. ee18btech11034_2.net,ee18btech11034_2.dat and ee18btech11034_spice_result2.py are files for feedback gain 0.014
7. ee18btech11034_spice_verify1.py gives the verification of circuit output step response through python for H = 0.01
8. Similarly ee18btech11034_spice_verify2.py is verification for H = 0.014
