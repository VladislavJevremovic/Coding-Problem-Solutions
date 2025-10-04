-- https://leetcode.com/problems/big-countries/
-- Note: SQL solutions are not exercised by the pytest suite (there is no
-- database to run against); they are kept here for reference. See CONVENTIONS.md.

select name, population, area from World where area > 3000000 or population > 25000000 order by name asc;
