# Defining Constants

# The location on your system where OJ folder is placed. It is required to serve static content.
SYS_ROOT   = "/var/www/html/"

MYSQL_HOST = "localhost"           # Host address of MySQL server. Maybe "localhost" or an IP.
MYSQL_PORT = "3306"                # The port on which MySQL server is listening. The default for MySQL is 3306
MYSQL_USER = "root"            # USERNAME to which you have granted the database access.
MYSQL_PASS = "prabhupada1"            # PASSWORD for the abode user.
MYSQL_DB   = "oj"                  # The database to use for OJ.


# Language Support [ Just remove all the corresponding entries in following variables to disable submission in them ]
LANGUAGES = ["GNU G++ 4.3"]
LANG_NICK = ["C++"]
LANG_EXT  = ["cpp"]
TIME_FACTOR = [1]                           # Time limit are multiple by this factor for corresponding language

# Add a entry for each problem
PROBLEMS_ID = ["P1","P2"]                             # ID of problem.
PROBLEMS_NAME = ["P1","P2"]         # Name of problem.
PROBLEMS_PAGE = ["P1.html","P2.html"]                      # File which contains the description of this corresponding entry. It should exists in OJ folder.
PROBLEMS_SCORE = [100,100];                            # Total score attainable for corresponding problem
MAX_SUBMISSION = [1000,1000];                              # Max. Submission allowed for corresponding problem

TIME_DIFF = 5                                    # Minimum gap in seconds between two consecutive submission for same problem.

# Please stick to the time format. Time is in 24-hours format. And month short nick should be used.

startTime = "25 Sep 2014 18:50"                    # The time the contest start, evaluation starts and problems are visible.
endTime   = "25 Sep 2015 20:50"                   # The time contest ends, evaluation stops and submissions are freezed.
regTime   = "25 Sep 2015 18:50"	                  # The time when registration stops. TeamList is freezed.
