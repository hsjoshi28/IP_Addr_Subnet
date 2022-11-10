'''
Author: Himanshu Joshi (hsjoshi28@gmail.com)

For the given set of IPv4 addresses find a minimal spanning subnet.

A minimal spanning subnet is the longest prefix that covers an entire set of addresses.
The way to find this is to calculate all of the addresses in binary. Count the equal bits in both the IP addresses and stop when they are unequal. 
Bitwise AND all of the bits to the left, that would be the longest prefix that covers the set. Append 0's to the right to make it a valid IP address. (8 bits in each octet)
Convert the resultant to decimal and append a '/' followed by the count of equal bits.

References: 
1. https://networkengineering.stackexchange.com/questions/7106/how-do-you-calculate-the-prefix-network-subnet-and-host-numbers/53994#53994
2. https://en.wikipedia.org/wiki/Longest_prefix_match
3. https://www.geeksforgeeks.org/longest-prefix-matching-in-routers/ 
'''
import ipaddress 

class MinimalSpanningSubnet:
    '''
    This method takes two ip addresses each in string and returns none but prints in the end.
    '''
    def findMSS(self, ipAddres1: str, ipAddres2: str) -> None:
        bin_ipAddr1 = '.'.join([bin(int(x)+256)[3:] for x in ipAddres1.split('.')]) # Convert IP address 1 from decimal to binary
        bin_ipAddr2 = '.'.join([bin(int(x)+256)[3:] for x in ipAddres2.split('.')]) # Convert IP address 2 from decimal to binary
        mask = 0
        result = ''

        for i in range(len(bin_ipAddr1)): # In this loop we will iterate through both binary converted ip addresses and break when they are unequal, if they are equal, we will 
                                          # count the mask needed and do Bitwise AND and store in a variable result.
            if bin_ipAddr1[i] == bin_ipAddr2[i]:
                if bin_ipAddr1[i] == '.':
                    result += '.'
                else:
                    mask += 1
                    result += str(int(bin_ipAddr1[i]) & int(bin_ipAddr2[i]))
            else:
                break
        
        if len(result) != len(bin_ipAddr1): # In this loop we will check is the result variable created in above loop is equal to length of bin_ipAddr1, if not, append 0's
            for i in range(len(result), len(bin_ipAddr1) ):
                if bin_ipAddr1[i] == '.':
                    result += '.'
                else:
                    result += '0'

        result = '.'.join(str(int(x, 2)) for x in result.split('.')) # Convert the result variable we calculated above from binary to decimal 
        result += '/' + str(mask) # append the slash (/) and the mask we calculated in first for loop.
        print("The Minimal Spanning Subnet is: " + result)


# Main program
if __name__ == '__main__':
    takeInput = input('Enter set of IPv4 address (seperated by a space): ')
    ipAddr = takeInput.split(' ')
    try: # Validate the entered IP addresses and calculate Minimal Spanning Subnet if valid.
        ipaddress.ip_address(ipAddr[0]) 
        ipaddress.ip_address(ipAddr[1]) 
        MinimalSubnet = MinimalSpanningSubnet()
        MinimalSubnet.findMSS(ipAddr[0], ipAddr[1])
    except :
        print('Invalid IPv4 addresses. Please re-run the code and enter valid IPv4 addresses, seperated by a space.')