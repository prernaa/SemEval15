#include <iostream>
#include <fstream>
#include <string>

const int numchars = 13;

int main(int argc, char* argv[]) 
{ 
	if (argc < 2) {// Tell the user how to run the program
		std::cerr << "Usage: " << argv[0] << " NAME" << std::endl;
	    return 1;
	}
	std::string in_file_str = "";
	in_file_str+=argv[1];
	std::string out_file_str = "";
	out_file_str+=argv[2];
	//std::cout<<"There are "<<argc<<" arguments\n";
    std::ifstream file_in(in_file_str);
	std::ofstream file_out(out_file_str);
    //std::ifstream file_in("input.txt");
	//std::ofstream file_out("output.txt");
	//std::cout<<"Files opened\n";
    std::string input; 
    while (std::getline(file_in, input))
    {
		std::string subinput = input.substr(input.size() - numchars);
		//std::cout<<subinput<<"\n";
        if(subinput.compare("Not Available")!=0){ // if tweet is available
        	file_out<<input<<"\n";
        }
    }
	file_in.close();
	file_out.close();
	return 0;
}