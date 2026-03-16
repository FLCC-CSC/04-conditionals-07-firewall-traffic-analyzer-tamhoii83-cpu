# FILE NAME - firewall_traffic_analyzer.py

# NAME: Hoi I Tam
# DATE: March 13, 2026
# BRIEF DESCRIPTION:  Firewall traffic risk analysis to monitor data transfers based on the port number and the size of the transfer as follows:

#The port number as an int (e.g., 80, 22, 443, 3389).
#The data transfer size in megabytes as in int (MB).
#If port 22 (SSH) or port 3389 (RDP) and transfer size >= 100MB output "HIGH RISK: Potential unauthorized remote access detected!"
#Else if port 80 (HTTP) with transfer size > 100MB output "MEDIUM RISK: Large unencrypted data transfer detected."
#Else if port 443 (HTTPS) output "LOW RISK: Secure encrypted transfer detected."
#Else output "UNKNOWN: Unrecognized traffic pattern."
#Print a firewall log message summarizing the risk level.


########## ENTER YER CODE BELOW THIS LINE ##########
# NAME: Hoi I Tam
# DATE: March 13, 2026
# BRIEF DESCRIPTION: Firewall traffic risk analysis to monitor data transfers
# based on the port number and the size of the transfer.

print("=== Network Traffic Security Analyzer ===\n")

port = int(input("Enter the port number (e.g., 80, 22, 443, 3389): "))
size = int(input("Enter the data transfer size in megabytes (MB): "))

print("\nFIREWALL LOG:")
print(f"Port: {port}, Transfer Size: {size} MB")

if (port == 22 or port == 3389) and size >= 100:
    print("Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!")
elif port == 80 and size > 100:
    print("Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.")
elif port == 443:
    print("Risk Assessment: LOW RISK: Secure encrypted transfer detected.")
else:
    print("Risk Assessment: UNKNOWN: Unrecognized traffic pattern.")

print("------------------------")


########### END YER CODE ABOVE THIS LINE ###########

    
########################################
#          SAMPLE OUTPUT
########################################

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 80
Enter the data transfer size in megabytes (MB): 120

FIREWALL LOG:
Port: 80, Transfer Size: 120 MB
Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 22
Enter the data transfer size in megabytes (MB): 1200

FIREWALL LOG:
Port: 22, Transfer Size: 1200 MB
Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 443
Enter the data transfer size in megabytes (MB): 1024

FIREWALL LOG:
Port: 443, Transfer Size: 1024 MB
Risk Assessment: LOW RISK: Secure encrypted transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 1725
Enter the data transfer size in megabytes (MB): 234567

FIREWALL LOG:
Port: 1725, Transfer Size: 234567 MB
Risk Assessment: UNKNOWN: Unrecognized traffic pattern.
------------------------
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Did you get tripped up using the `or` or `and` operators? If so, how?

Yes, I forgot to use 'or' to check for both port 22 and port 3389 in the first condition. I wrote in two separate conditions instead of combining them. 


'''
