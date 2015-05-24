  *Currently in use by all GNOME Games 
=======================================

- This script is currently in use by GNOME libgames-support module which is a support module common to all games.
- Is basically a guideline checker pre-commit hook for all GNOME games.

See: https://github.com/GNOME/libgames-support/commit/a6c47620189f0057d7dfb1659274e7860268425e

GNOME Code Guideline Checker 
==================================

This script is useful to check if your code complies with the GNOME guidelines.

This git hook checks errors most people overlook:
- Line width,
- Lines with trailing whitespaces,
- Lines with trailing tabspaces,
- Whitespace checks around brackets.

This does NOT check the block structures(like if-else),
as most editors do that for you.(I assume you don’t mess around :P)

  How to setup
================
| For personal workspace |
--------------------------
- Copy Gnome-Code-Guideline-Checker/scripts/pre-commit to YOUR_PROJECT/.git/hooks/
- Add execute permission to the pre-commit hook

Commands:
```
cp Gnome-Code-Guideline-Checker/scripts/pre-commit to YOUR_PROJECT/.git/hooks/
chmod +x YOUR_PROJECT/.git/hooks/pre-commit
```

| For a project |
------------------
* Add a folder called scripts to YOUR_PROJECT
* Copy the pre-commit hook to YOUR_PROJECT/scripts
* autogen.sh should do what we did for a personal workspace

Commands:
```
cd YOUR_PROJECT
mkdir scripts
cp Gnome-Code-Guideline-Checker/scripts/pre-commit to YOUR_PROJECT/scripts/
(Add in autogen.sh) cp Gnome-Code-Guideline-Checker/scripts/pre-commit to YOUR_PROJECT/.git/hooks/
(Add in autogen.sh) chmod +x YOUR_PROJECT/.git/hooks/pre-commit
```

EXAMPLE
=======
https://git.gnome.org/browse/gnome-chess/commit/?id=8be49c2b4d1b2be921071753cb7697fcfaa77653

  BUGS
========
Report bugs to : ssareen [ AT ] gnome [ DOT ] org
