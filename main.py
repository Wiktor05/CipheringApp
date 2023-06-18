"""
Functionality:
1. Users types any text and gets it encrypted, e.g
> Hello World!
....encrypts typed in text...
< Hello World! (Xyzdev sad; ---- encrypted)

Menu:
(custom order)
1. Save to file whole encrypted content (file shou.json have n extension)
2. Decrypt (e.g inputs the file which should be encrypted)
3. Encrypt text ------> Choose your algorithm: ROT47, ROT13 ------> type your text: -------> text
gets encrypted and saved to list
4. Exit

-----------------------------------------------------------------------------------------------------

Classes:
- Manager, ROT13, ROT47, ContextMenu (all options), ROTFactory (handles different types of ciphering),
FileSaver (saves data to file), FileReader (reads data from file)

one class per one file, e.g class Manager -> manager.py

- src/
   - ciphering/ (rot13.py, rot47.py)
   - managers/ (manager.py)
   - files/ (reader.py, saver.py)
   - menus/ (context_menu.py, ...)
   - factories/ (rot_factory.py)
- tests/ (imports from src/ this kind of functionality that we want to test)
   - ciphering/ -> test_rot13.py, test_rot47.py
   - manager/ -> test_manager.py
   - files/
   - menus/
   - factories/

Requirements:
- type annotations
- docstrings
- precommit-hook
- testing and ci
- github



{
   rot13: '....',
   rot14: '....'
}
vs
{
  'rot47' : [...]
  'rot13' : [...]
}
vs
<date>.json
{
    'type': 'rot13',
    'content': [...]
}

rot47-<date>.json
{
    'type': 'rot47',
    'content': [...]
}


"""
