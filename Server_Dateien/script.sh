#echo "Test 1 script"
#!/bin/sh

# Localize these. The -G option does nothing before Postfix 2.3.
INSPECT_DIR=/var/spool/filter
SENDMAIL="/usr/sbin/sendmail -G -i" # NEVER NEVER NEVER use -t here.
#SPAM_DIR="/path/to/spam/folder"

#echo "Test 2 script"

# Exit codes from <sysexits.h>
EX_TEMPFAIL=75
EX_UNAVAILABLE=69

#echo "Test 3 script"

# Clean up when done or when aborting.
trap "rm -f in.$$" 0 1 2 3 15

#echo "Test 4 script"

# Start processing.
cd $INSPECT_DIR || {
    echo $INSPECT_DIR does not exist; exit $EX_TEMPFAIL; }

#echo "Test 5 script"

cat >in.$$ || { 
     echo Cannot save mail to file; exit $EX_TEMPFAIL; }

# Specify your content filter here
#OUTPUT=$(/bin/python3 /home/filter/spam.py > in.$$)
#/usr/bin/python3 /home/filter/spam.py  > in.$$ || {
#     echo Message content rejected; exit $EX_UNAVAILABLE; }

/usr/bin/python3 /home/filter/spam.py <in.$$> /tmp/postfix_output.txt || {
     echo Message content rejected; exit $EX_UNAVAILABLE; }

/tmp/postfix_output.txt > /home/filter/output.log

#echo $OUTPUT |
#$SENDMAIL "$@" < in.$$
$SENDMAIL "$@" < /tmp/postfix_output.txt

#echo "Test 8 script"

exit $? 
