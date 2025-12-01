#include <ostream>
#include <vector>
#include "utility.h"

void print_array(std::ostream& os, const std::vector<int>& vec) 
{
	for ( const auto value : vec )
	{
		os << value << ", ";
	}
	os << std::endl;
}