---------------------------------------------------
	Code for sorting song recommendations.
---------------------------------------------------
* All required files are included in this folder.
* playlist / recommendation data for krishnan is in the data folder. Those for 2 more users are also available
* First, Rename runtest.bat.txt to runtest.bat
*Usage:
	> runtest <driver_program> <user_prefix> <use_artist_as_field>
	
	where:
		user_prefix is the prefix of the file in the data folder (eg: kg )
* In this case:
	- combosort is the driver program
	- Always use 'yes' for artist as it will be used to generate derived attributes
	- Use the prefix. For my data, it is kg 
* Example usage:
	> runtest combosort kg yes

* To try out the different functions, 
	- Open recommendationsorter/combosorter.py
	- Uncomment the line corresponding to the scoring function you wish to use
* The result will be stored in 
	- results/<user_prefix>/<driver_program>_<use_artist_as_field>.out
