==================================
|| Gnome-Code-Guideline-Checker ||
==================================

This script is useful to check if your code complies with the GNOME guidelines.

This git hook checks errors most people overlook:
     1. Line width,
     2. Lines with,
     3. Trailing whitespaces,
     4. Trailing tabspaces,
     5. Whitespace checks around brackets.

This does NOT check the block structures(like if-else),
as most editors do that for you.(I assume you don’t mess around :P)

HOW TO SETUP
=============
--------------------------
| For personal workspace |
--------------------------
* Copy Gnome-Code-Guideline-Checker/scripts/pre-commit to YOUR_PROJECT/.git/hooks/
* Add execute permission to the pre-commit hook

Commands:
cp Gnome-Code-Guideline-Checker/scripts/pre-commit to YOUR_PROJECT/.git/hooks/
chmod +x YOUR_PROJECT/.git/hooks/pre-commit

------------------
| For a project: |
------------------
* Add a folder called scripts to YOUR_PROJECT
* Copy the pre-commit hook to YOUR_PROJECT/scripts
* autogen.sh should do what we did for a personal workspace

Commands:
cd YOUR_PROJECT
mkdir scripts
cp Gnome-Code-Guideline-Checker/scripts/pre-commit to YOUR_PROJECT/scripts/
(Add in autogen.sh) cp Gnome-Code-Guideline-Checker/scripts/pre-commit to YOUR_PROJECT/.git/hooks/
(Add in autogen.sh) chmod +x YOUR_PROJECT/.git/hooks/pre-commit


BUGS
======
Report bugs to : ssareen [ AT ] gnome [ DOT ] org
