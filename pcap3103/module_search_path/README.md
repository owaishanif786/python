# Module Search Path

0. default libary will be loaded first so we won't accidently overwrite that library.
1. Script running in current directory will be first i.e `import helpers`
2. PYTHONPATH set in env variables will be next
3. third with python default libs installed 

To see the the path use `sys.path`
The `site-packages` will have third party modules installed.

To change PYTHONPATH specify before running script as variable
`PYTHONPATH=/home/user python3.7`
Now `/home/user` will be on the second number after then directory in which script is running.


If you need to import some module from any directory inside interpretor. Then before running interpreter you can set PYTHONPATH. then inside interpreter you can simply import that package without specify full path.



