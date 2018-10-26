# Maven Repo 99-empty
A general repository to return empty JAR

Similar to
http://day-to-day-stuff.blogspot.com/2007/10/announcement-version-99-does-not-exist.html


Act like a Maven Remote Repository.  If a valid URL for POM or JAR is requested, empty JAR will be returned

Valid URL means:
- Valid URL based on Maven URL layout
  - https://cwiki.apache.org/confluence/display/MAVENOLD/Repository+Layout+-+Final
  - https://blog.packagecloud.io/eng/2017/03/09/how-does-a-maven-repository-work/
- Version in form of:
  - Starts with 99, 999, 99.0, 999.0
  - Followed by hyphen
  - Ends with `does.not.exist`, `empty`, `EMPTY`, `exclude`, `EXCLUDE`
  - (could be easily updated by changing the regex
  
